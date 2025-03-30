import copy
import time
from datetime import datetime, timedelta, timezone
import json

import pytest
from assertpy import assert_that

from endpoints.v2.controller_catalog import V2_DELETE_DATASET
from endpoints.v2.controller_job import (
    V2_GET_OWL_CHECK_Q_BY_ID,
    V2_POST_RUN_JOB_JSON,
)
from endpoints.v2.controller import (
    V2_GET_LATEST_DATASET_HISTORY,
    V2_GET_RUN_IDS_BY_DATASET,
)
from endpoints.v2.controller_agent import (
    V2_GET_AGENT,
    V2_GET_AGENTS,
    V2_GET_LIST_AGENTS_DETAILS_BY_CONNECTION_ALIAS,
)
from endpoints.v2.controller_connections import (
    V2_CHECK_CORE_SPECIFIC_DRIVER,
    V2_GET_CONNECTION_BY_ALIAS,
)
from endpoints.v2.controller_explorer import V2_GET_DATASETS_BY_DATASET
from endpoints.v2.controller_hoot import V2_GET_ISSUE_COUNTS, V2_GET_SQL_RESULT
from endpoints.v2.controller_label import V2_REMOVE_ITEM_LABEL, V2_VIEW_ITEM_LABELS
from endpoints.v2.controller_outlier_opt import (
    V2_DELETE_OUTLIER_OPT,
    V2_OUTLIER_OPT,
    V2_UPSERT_OUTLIER_OPT,
)
from endpoints.v2.controller_owl_options import V2_OWL_OPTIONS_GET
from endpoints.v2.controller_pattern_opt import V2_DELETE_PATTERN_OPT, V2_UPSERT_PATTERN_OPT
from endpoints.v2.controller_rule import V2_CREATE_RULE, V2_GET_RULES, V2_AI_GENERATE

from endpoints.v3.job_api import V3_JOBS_JOBID_WAITFORCOMPLETION, V3_JOBS_RUN
from endpoints.v3.dataset_def_api import V3_DATASETDEFS
from endpoints.v3.rule_api import V3_RULES
from payloads.pullup.pl_alerts import PL_JOB_PAYLOAD_DEFAULT
from payloads.pushdown.dq_job.pl_pd_dataset_metatags import PL_PD_NEW_DATASET_DEFAULT
from utils import constants
from utils.api_utils import APIUtils
from utils.constants import (
    BASE_CREDS,
    PROD_AGENT_ID,
    PROD_AGENT_NAME,
    PROD_AGENT_UUID,
    PROD_HOST,
    PROD_RUN_ID,
)


# pylint: disable=too-many-public-methods
class BaseHelper:
    """Basic helper methods to use in tests."""

    @pytest.fixture(scope="session")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def delete_dataset_outlier_configurations(api_utils, dataset):
        """Removes all outlier configurations associated with the specified dataset"""
        deleted_outlier_count = 0
        get_outlier_opt_response = api_utils.get(V2_OUTLIER_OPT, params={"dataset": dataset})

        if get_outlier_opt_response["result"] is not None:
            for outlier in get_outlier_opt_response["result"]:
                outlier_id = str(outlier["id"])
                del_response = api_utils.delete(V2_DELETE_OUTLIER_OPT, params={"id": outlier_id})
                if del_response["result"] == "true":
                    deleted_outlier_count += 1

        return deleted_outlier_count

    @staticmethod
    def delete_dataset_pattern_configurations(api_utils, dataset):
        """Removes all pattern configurations associated with the specified dataset"""
        deleted_pattern_count = 0
        dataset_count = len(api_utils.get(V2_GET_DATASETS_BY_DATASET, params={"dataset": dataset}))
        if dataset_count > 0:
            get_opts_response = api_utils.get(V2_OWL_OPTIONS_GET, params={"dataset": dataset})

            if get_opts_response["result"] is not None:
                for pattern in get_opts_response["result"]["patterns"]:
                    pattern_id = str(pattern["id"])
                    del_response = api_utils.delete(
                        V2_DELETE_PATTERN_OPT, params=({"id": pattern_id})
                    )
                    if del_response["result"] == "true":
                        deleted_pattern_count += 1

        return deleted_pattern_count

    def run_source_job(self, api_utils, dataset_defs):
        """
        Run the job, get issue counts-returns run_id, issue_counts and
        job_status, dataset score.
        """
        self.setup_dataset(api_utils, dataset_defs)

        data = self.get_dataset_history_issues(api_utils, dataset_defs["dataset"])
        return data

    # noinspection PyMethodMayBeStatic
    def get_dataset_history_issues(self, api_utils, dataset_name):
        """Returns issue_counts, dataset score, features scores."""
        dataset_history_response = api_utils.get(
            V2_GET_LATEST_DATASET_HISTORY, params={"dataset": dataset_name}
        )

        run_id = dataset_history_response["runId"]

        issue_counts = api_utils.get(
            V2_GET_ISSUE_COUNTS, {"dataset": dataset_name, "runId": run_id}
        )

        data = {
            "source": issue_counts["SOURCE"],
            "dupe": issue_counts["DUPE"],
            "score": dataset_history_response["score"],
            "scoreSource": dataset_history_response["scoreSource"],
            "scoreDatashape": dataset_history_response["scoreDatashape"],
            "shape": issue_counts["SHAPE"],
            "runId": run_id,
        }
        return data

    @staticmethod
    def get_minimum_job_payload(
        api_utils,
        connection_name,
        dataset_name,
        query,
        run_id=PROD_RUN_ID,
        run_id_end="",
    ):
        """Create a payload with bare minimum data based on connection alias"""
        conn = connection_name.replace(" ", "_")

        resp = api_utils.get(V2_GET_CONNECTION_BY_ALIAS, params={"alias": conn})

        if "message" in resp and resp["message"] is None:
            raise ConnectionError(f"Connection {conn} not found")

        return {
            "dataset": dataset_name,
            "runId": run_id,
            "runIdEnd": run_id_end,
            "host": PROD_HOST,
            "agentId": {
                "id": PROD_AGENT_ID if resp["isPushdown"] == 0 else 0,
                "uuid": PROD_AGENT_UUID,
            },
            "load": {
                "query": query,
                "lib": resp["driverlocation"],
                "driverName": resp["drivername"],
                "connectionName": conn,
            },
            "spark": {
                "dataset": dataset_name,
                "numExecutors": 2,
                "driverMemory": "4g",
                "executorMemory": "6g",
                "executorCores": 2,
                "conf": "spark.executor.memoryOverhead=1g",
                "master": "k8s://",
                "deployMode": "cluster",
            },
            "pushdown": {
                "connectionName": "" if resp["isPushdown"] == 0 else conn,
                "sourceQuery": "" if resp["isPushdown"] == 0 else query,
            },
        }

    def setup_dataset(
        self, api_utils, dataset_defs, run_date=None, run_date_end=None, update_spark_sizing=True
    ):
        """Update dataset definitions with environment, connection, and dataset specific values,
        create/update the dataset, run a job, and wait for completion."""
        dataset_defs = self.update_pullup_dataset_agent_config(
            api_utils, dataset_defs, update_spark_sizing
        )
        dataset_defs = self.update_pullup_dataset_connection_config(api_utils, dataset_defs)
        dataset_defs = self.update_pullup_dataset_additional_lib(api_utils, dataset_defs)
        dataset_defs = self.update_dataset_defs_outlier_config(api_utils, dataset_defs)
        dataset_defs = self.update_dataset_defs_pattern_config(api_utils, dataset_defs)
        dataset_defs["host"] = constants.PROD_HOST
        dataset_defs["port"] = constants.PROD_PORT
        dataset_defs["user"] = BASE_CREDS["username"]
        api_utils.put(V3_DATASETDEFS, json.dumps(dataset_defs))
        if not run_date:
            run_date = dataset_defs["runId"]

        return self.setup_post_dataset(api_utils, dataset_defs, run_date, run_date_end)

    @staticmethod
    def update_pullup_dataset_connection_config(api_utils, dataset_defs):
        """Update connection information for a dataset based on details of the connection.
        This allows definitions created on one environment type to be used on other environments"""
        if "connectionName" not in dataset_defs["load"]:
            return dataset_defs
        if dataset_defs["load"]["connectionName"] is not None:
            dataset_connection_details = api_utils.get(
                V2_GET_CONNECTION_BY_ALIAS, params={"alias": dataset_defs["load"]["connectionName"]}
            )

            if (
                "message" in dataset_connection_details
                and dataset_connection_details["message"] is None
            ):
                raise ConnectionError(
                    f'Connection {dataset_defs["load"]["connectionName"]} not found'
                )

            core_subdirectory = api_utils.get(
                V2_CHECK_CORE_SPECIFIC_DRIVER,
                params={"aliasname": dataset_defs["load"]["connectionName"]},
            )["useCoreSubDir"]
            if dataset_connection_details["connType"] == "JDBC":
                dataset_defs["load"]["lib"] = dataset_connection_details["driverlocation"]
                dataset_defs["load"]["driverName"] = dataset_connection_details["drivername"]
                dataset_defs["load"]["connectionUrl"] = dataset_connection_details["hostname"]
                dataset_defs["load"]["userName"] = dataset_connection_details["username"]
                # Profile pushdown can use different drivers from standard pullup jobs
                if (
                    "profile" not in dataset_defs
                    or "profilePushDown" not in dataset_defs["profile"]
                ) and core_subdirectory:
                    dataset_defs["load"]["lib"] += core_subdirectory
                elif core_subdirectory and not dataset_defs["profile"]["profilePushDown"]:
                    dataset_defs["load"]["lib"] += core_subdirectory

        return dataset_defs

    def update_pullup_dataset_agent_config(self, api_utils, dataset_defs, update_spark_sizing=True):
        """
        Update agent information for a dataset to a specific agent or to match the agent assigned
        to its connection. This allows definitions created on one environment to be used on other
        environments.
        :param api_utils: API Utils
        :param dataset_defs: The dataset definitions tu update
        :param update_spark_sizing: Boolean controlling whether to update spark resources
        :return: updated dataset definitions or original dataset definitions if update was not
        possible
        """
        if "agentId" not in dataset_defs or "spark" not in dataset_defs:
            return dataset_defs

        if PROD_AGENT_ID or PROD_AGENT_NAME:
            all_agents_details = api_utils.get(V2_GET_AGENTS)
            for agent_details in all_agents_details:
                if agent_details["agentId"]["id"] == PROD_AGENT_ID:
                    specified_agent_details = agent_details
                    dataset_defs = self.update_dataset_agent_settings(
                        dataset_defs, specified_agent_details, update_spark_sizing
                    )
                    return dataset_defs
            for agent_details in all_agents_details:
                if agent_details["agentName"] == PROD_AGENT_NAME:
                    specified_agent_details = agent_details
                    dataset_defs = self.update_dataset_agent_settings(
                        dataset_defs, specified_agent_details, update_spark_sizing
                    )
                    return dataset_defs

        if "connectionName" not in dataset_defs["load"]:
            return dataset_defs

        if dataset_defs["load"]["connectionName"] is not None:
            connection_agents_details = self.get_agent_details_for_connection(
                api_utils, dataset_defs["load"]["connectionName"]
            )
            if (
                dataset_defs["agentId"] is None
                or "id" not in dataset_defs["agentId"]
                or "uuid" not in dataset_defs["agentId"]
            ):
                dataset_defs["agentId"] = {"id": "", "uuid": ""}

            dataset_defs = self.update_dataset_agent_settings(
                dataset_defs, connection_agents_details, update_spark_sizing
            )
        return dataset_defs

    def update_dataset_agent_settings(self, dataset_defs, agent_details, update_spark_sizing=True):
        dataset_defs["agentId"]["id"] = agent_details["agentId"]["id"]
        dataset_defs["agentId"]["uuid"] = agent_details["agentId"]["uuid"]
        dataset_defs["spark"]["master"] = agent_details["masterDefault"]
        dataset_defs["spark"]["deployMode"] = agent_details["deployModeDefault"]

        if update_spark_sizing:
            dataset_defs = self.update_spark_sizing(dataset_defs, agent_details)

        return dataset_defs

    @staticmethod
    def update_spark_sizing(dataset_defs, agent_details):
        dataset_defs["spark"]["numExecutors"] = agent_details["numExecutors"]
        dataset_defs["spark"]["driverMemory"] = agent_details["driverMemory"]
        dataset_defs["spark"]["executorMemory"] = agent_details["executorMemory"]
        dataset_defs["spark"]["executorCores"] = agent_details["numCores"]

        return dataset_defs

    def update_pullup_dataset_additional_lib(self, api_utils, dataset_defs):
        """Support rules with SQL joins between two datasets using different connection drivers by
        setting the additionalLib field on a dataset to the lib value from a secondary dataset in
        a rule's SQL join"""
        dataset = dataset_defs["dataset"]
        dataset_lib = dataset_defs["load"]["lib"]
        dataset_rules = api_utils.get(V3_RULES + "/" + dataset, params={"dataset": dataset})

        # Find all secondary datasets referenced in rules
        secondary_datasets = []
        dataset_name_indicator = "@"
        newline_character = "\n"
        characters_to_strip = dataset_name_indicator + newline_character + ")"
        for rule in dataset_rules:
            rule_value_terms = rule["ruleValue"].rsplit(" ")
            for term in rule_value_terms:
                if len(term) > 0 and term[0] == dataset_name_indicator:
                    dataset_name_in_rule = term.strip(characters_to_strip)
                    dataset_name_in_rule = self.remove_statistic_from_dataset_name(
                        dataset_name_in_rule
                    )
                    if dataset_name_in_rule not in [
                        dataset,
                        "dataset",
                        "t1",
                        "t2",
                        "t3",
                        "t4",
                        "t5",
                    ]:
                        secondary_datasets.append(dataset_name_in_rule)

        # In any secondary datasets, find the first jdbc driver location that differs from
        # that of the primary dataset and write it to the primary dataset's additionalLib value
        if secondary_datasets:
            for secondary_dataset_name in secondary_datasets:
                secondary_dataset_defs = api_utils.get(
                    V3_DATASETDEFS + "/" + secondary_dataset_name,
                    params={"dataset": secondary_dataset_name},
                )
                secondary_dataset_lib = secondary_dataset_defs["load"]["lib"]
                if secondary_dataset_lib not in [dataset_lib, "remoteFileConndriverlocation"]:
                    dataset_defs["load"]["additionalLib"] = secondary_dataset_lib
                    break

        return dataset_defs

    @staticmethod
    def setup_post_dataset(api_utils, dataset_defs, run_date=None, run_date_end=None):
        if not run_date:
            run_date = dataset_defs["runId"]

        agent_details = api_utils.get(
            V2_GET_AGENT, params={"agentid": dataset_defs["agentId"]["id"]}
        )

        # Run the job
        job_creation_params = {
            "dataset": dataset_defs["dataset"],
            "runDate": run_date,
            "runDateEnd": run_date_end,
            "agentName": agent_details["agentName"],
        }
        job_creation_response = api_utils.post(V3_JOBS_RUN, params=job_creation_params)
        job_id = job_creation_response["jobId"]

        # Wait for job to complete
        job_output = api_utils.get(V3_JOBS_JOBID_WAITFORCOMPLETION.format(jobId=job_id))

        return job_output

    def run_pullup_job_if_dataset_does_not_exist(
        self, api_utils, dataset_defs, run_date=None, run_date_end=None, update_spark_sizing=True
    ):
        """Creates and runs a pullup job if the dataset does not exist"""
        dataset_check_params = {"dataset": dataset_defs["dataset"]}
        dataset_runids = api_utils.get(V2_GET_RUN_IDS_BY_DATASET, params=dataset_check_params)
        dataset_job_run_count = len(dataset_runids)
        if dataset_job_run_count == 0:
            if not run_date:
                run_date = dataset_defs["runId"]
            self.setup_dataset(api_utils, dataset_defs, run_date, run_date_end, update_spark_sizing)

    def run_pushdown_job(self, api_utils, job_creation_payload):
        """Creates and runs a pushdown job"""
        job_creation_payload["host"] = constants.PROD_HOST
        job_creation_payload["user"] = constants.BASE_CREDS["username"]
        has_saved_outlier_config = self.outliers_config_contains_id(job_creation_payload)
        if has_saved_outlier_config:
            self.delete_dataset_outlier_configurations(api_utils, job_creation_payload["dataset"])
            job_creation_payload = self.update_dataset_defs_outlier_config(
                api_utils, job_creation_payload
            )
        job_creation_response = api_utils.post(
            V2_POST_RUN_JOB_JSON, data=(json.dumps(job_creation_payload))
        )
        get_job_response = api_utils.get(
            V2_GET_OWL_CHECK_Q_BY_ID,
            params=({"jobUUID": job_creation_response["uuid"]}),
        )
        job_id = get_job_response["jobId"]["id"]

        job_output = api_utils.get(V3_JOBS_JOBID_WAITFORCOMPLETION.format(jobId=job_id))

        return job_output

    def run_pushdown_job_if_dataset_does_not_exist(self, api_utils, job_creation_payload):
        """Creates and runs a pushdown job only if the dataset doesn't exist"""
        dataset_check_params = {"dataset": job_creation_payload["dataset"]}
        dataset_runids = api_utils.get(V2_GET_RUN_IDS_BY_DATASET, params=dataset_check_params)
        dataset_job_run_count = len(dataset_runids)
        if dataset_job_run_count == 0:
            self.run_pushdown_job(api_utils, job_creation_payload)

    def update_dataset_defs_outlier_config(self, api_utils, dataset_defs, outlier_list=None):
        """Create new outlier configurations based on those contained in a
        dataset definition or specified list.  Update and return the dataset definition."""
        if "outliers" not in dataset_defs or not dataset_defs["outliers"]:
            return dataset_defs

        if not outlier_list:
            outlier_list = dataset_defs["outliers"]

        new_outlier_list = []
        for outlier in outlier_list:
            # The upsert outlier API requires column list parameters to be strings
            key_columns = self.iterable_to_comma_separated_string(outlier["key"])
            include_columns = self.iterable_to_comma_separated_string(outlier["include"])
            exclude_columns = self.iterable_to_comma_separated_string(outlier["exclude"])

            # Only settings defined here will be configured as specified.  Others will be default.
            upsert_outlier_params = {
                "dataset": dataset_defs["dataset"],
                "on": True,
                "lookback": outlier["lookback"],
                "categorical": outlier["categorical"],
                "q1": outlier["q1"],
                "q3": outlier["q3"],
                "key": key_columns,
                "include": include_columns,
                "exclude": exclude_columns,
                "datecolumn": outlier["dateColumn"],
                "historylimit": outlier["historyLimit"],
                "timeBin": outlier["timeBin"],
                "by": outlier["by"],
            }
            new_outlier = api_utils.put(V2_UPSERT_OUTLIER_OPT, params=upsert_outlier_params)
            if new_outlier["result"]["include"] is None:
                new_outlier["result"]["include"] = []
            if new_outlier["result"]["exclude"] is None:
                new_outlier["result"]["exclude"] = []
            new_outlier_list.append(new_outlier["result"])

        dataset_defs["outliers"] = new_outlier_list
        if "outlierConfiguration" in dataset_defs.keys():
            dataset_defs["outlierConfiguration"]["configurations"] = new_outlier_list

        return dataset_defs

    def update_dataset_defs_pattern_config(self, api_utils, dataset_defs, pattern_list=None):
        """Create new pattern configurations based on those contained in a
        dataset definition or specified list.  Update and return the dataset definition."""
        if "patterns" not in dataset_defs or not dataset_defs["patterns"]:
            return dataset_defs

        if not pattern_list:
            pattern_list = dataset_defs["patterns"]

        new_pattern_list = []
        for pattern in pattern_list:
            # The upsert pattern API requires column list parameters to be strings
            key_columns = self.iterable_to_comma_separated_string(pattern["key"])
            include_columns = self.iterable_to_comma_separated_string(pattern["include"])
            exclude_columns = self.iterable_to_comma_separated_string(pattern["exclude"])

            upsert_pattern_params = {
                "dataset": dataset_defs["dataset"],
                "on": pattern["on"],
                "key": key_columns,
                "include": include_columns,
                "exclude": exclude_columns,
                "datecolumn": pattern["dateColumn"],
                "lookback": pattern["lookback"],
                "timeBin": pattern["timeBin"],
            }
            new_pattern = api_utils.put(V2_UPSERT_PATTERN_OPT, params=upsert_pattern_params)
            new_pattern_list.append(new_pattern["result"])

        dataset_defs["patterns"] = new_pattern_list

        return dataset_defs

    @staticmethod
    def iterable_to_comma_separated_string(input_iterable):
        """Some API parameters require lists of values to be submitted in a comma separated string.
        Convert an iterable, such as a list, to a string of comma separated values."""
        if not input_iterable:
            return ""
        output_string = ",".join(str(element) for element in input_iterable)
        return output_string

    @staticmethod
    def set_rules_on_dataset(api_utils, dataset_name, rule_definitions, v2_create_rule=False):
        """Delete existing rules and set new rules on a dataset"""
        api_utils.delete(V3_RULES + "/" + dataset_name, return_json=False)

        rule_count = api_utils.get(V2_GET_RULES, params={"dataset": dataset_name})

        assert_that(
            len(rule_count), "set_rules_on_dataset expected no rules after delete"
        ).is_equal_to(0)

        for rule_def in rule_definitions:
            if v2_create_rule:
                api_utils.post(V2_CREATE_RULE, params=rule_def)
            else:
                api_utils.post(V3_RULES, data=json.dumps(rule_def))

    @staticmethod
    def update_rules_on_dataset(api_utils, dataset_name, rule_definitions, v2_create_rule=False):
        rule_count = api_utils.get(V2_GET_RULES, params={"dataset": dataset_name})
        (assert_that(len(rule_count), "The rule is missing on the dataset").is_equal_to(1))

        for rule_def in rule_definitions:
            if v2_create_rule:
                api_utils.post(V2_CREATE_RULE, params=rule_def)
            else:
                api_utils.post(V3_RULES, data=json.dumps(rule_def))

    @staticmethod
    def add_scheduled_run_date_time_zoned_to_parameters(parameters):
        """/v2/postjobschedule requires the scheduledRunDateTimeZoned parameter.
        Add this to a parameter list by calculating value from scheduled run time"""
        now = datetime.now().astimezone()
        current_time = now.time()
        schedule_time = datetime.strptime(parameters["scheduledRunTime"], "%H:%M:%S").time()
        if current_time < schedule_time:
            run_date_time = datetime.combine(now, schedule_time).replace(tzinfo=now.tzinfo)
        else:
            tomorrow = now + timedelta(days=1)
            run_date_time = datetime.combine(tomorrow, schedule_time).replace(tzinfo=now.tzinfo)

        scheduled_run_date = run_date_time.astimezone(timezone.utc)
        scheduled_run_string = scheduled_run_date.strftime("%a, %d %b %Y %H:%M:%S %Z")
        parameters["scheduledRunDateTimeZoned"] = scheduled_run_string

        return parameters

    @staticmethod
    def extract_sql_result_from_data_preview(data_preview_output):
        """Extract a list of dictionaries representing rows of the SQL output from data preview.
        Extract only the column and row name using the schema information in the output."""
        sql_result = []
        for _index, row in enumerate(data_preview_output["rows"]):
            result_dict = {}
            for column, schema in zip(row, data_preview_output["schema"]):
                column_name = schema["name"]
                column_value = column["colValue"]
                result_dict[column_name] = column_value
            sql_result.append(result_dict)

        return sql_result

    @staticmethod
    def run_sql(api_utils, sql, connection, limit=-1):
        """Execute SQL against a specified connection with no limit on rows returned unless
        specified."""
        run_sql_params = {
            "sql": sql,
            "cxn": connection,
            "limit": limit,
        }
        sql_output = api_utils.post(V2_GET_SQL_RESULT, params=run_sql_params)

        return sql_output

    @staticmethod
    def run_query_and_extract_result(api_utils, query, connection, limit=-1):
        """Run a specified SQL query using an API in the application to access the datastore
        then extract the results into a more usable format."""
        sql_output = BaseHelper.run_sql(api_utils, query, connection, limit)
        output_dictionary = BaseHelper.extract_sql_result_from_data_preview(sql_output)

        return output_dictionary

    @staticmethod
    def get_agent_details_for_connection(api_utils, connection_name):
        """Return the agent details for a connection.  Returns only one agent per connection."""
        dataset_agents_details = api_utils.get(
            V2_GET_LIST_AGENTS_DETAILS_BY_CONNECTION_ALIAS,
            params={"connectionalias": connection_name},
        )

        if len(dataset_agents_details) == 0:
            raise ConnectionError(
                f"No agent found for connection {connection_name}. "
                f"The connection may be down or absent."
            )

        # In test environments, generally only one agent exists per connection.  Use first agent
        # returned until a test scenario involving multiple agents per connection is encountered.
        agent_details = dataset_agents_details[0]

        return agent_details

    def backrun_dataset_if_needed(self, api_utils, dataset_defs, backrun_count):
        """Check if a dataset has the required run_ids to fulfil a specified backrun count.
        Run jobs for required backruns if condition is not met.  This will only fill in prior dates
        , it will not run a job for the runId specified in the dataset definitions.
        Note that this will only detect 7 or fewer existing backruns due to a limit on the API
        which checks existing runs in the system.  With a higher backrun count, this method will
        always execute backruns."""
        is_pushdown_dataset = self.is_pushdown_dataset_defs(dataset_defs)
        existing_run_ids = api_utils.get(
            V2_GET_RUN_IDS_BY_DATASET, {"dataset": dataset_defs["dataset"]}
        )
        dataset_defs_run_date = datetime.strptime(dataset_defs["runId"][0:10], "%Y-%m-%d")

        run_date_list = []
        for run_id in existing_run_ids:
            run_date = run_id[0:10]
            run_date_list.append(run_date)

        required_run_dates = []
        for backrun_day_number in range(1, backrun_count, 1):
            expected_run_date = (
                dataset_defs_run_date - timedelta(days=backrun_day_number)
            ).strftime("%Y-%m-%d")
            required_run_dates.append(expected_run_date)

        if not all(run_id in run_date_list for run_id in required_run_dates):
            backrun_dataset_defs = copy.deepcopy(dataset_defs)
            backrun_dataset_defs["runId"] = (dataset_defs_run_date - timedelta(days=1)).strftime(
                "%Y-%m-%d"
            )
            if is_pushdown_dataset:
                backrun_dataset_defs["pushdown"]["backRuns"] = backrun_count - 1
                self.run_pushdown_job(api_utils, backrun_dataset_defs)
            else:
                backrun_dataset_defs["load"]["backRun"] = backrun_count - 1
                self.setup_dataset(api_utils, backrun_dataset_defs)

    @staticmethod
    def is_pushdown_dataset_defs(dataset_defs):
        """Checks if a dataset definition is pushdown."""
        if "connectionType" in dataset_defs.keys():
            if dataset_defs["connectionType"] == "PUSHDOWN":
                return True
            if dataset_defs["connectionType"] == "PULLUP":
                return False
        if (
            "pushdown" in dataset_defs
            and "connectionName" in dataset_defs["pushdown"]
            and len(dataset_defs["pushdown"]["connectionName"]) > 0
        ):
            return True

        return False

    @staticmethod
    def delete_labels_if_exist(api_utils, dataset):
        resp_labels1 = api_utils.get(V2_VIEW_ITEM_LABELS, params={"dataset": dataset["dataset"]})
        pl_ds_run_id1 = {"dataset": dataset["dataset"], "runId": dataset["runId"]}

        if len(resp_labels1["data"]) > 0:
            for data in resp_labels1["data"]:
                pl_remove_item_label1 = {
                    "dataset": pl_ds_run_id1["dataset"],
                    "runid": pl_ds_run_id1["runId"],
                    "itemkey": data["itemKey"],
                    "itemtype": data["itemType"],
                    "itemvalue": data["itemValue"],
                    "itemcount": str(data["itemCount"]),
                    "assignmentUUID": data["assignmentId"]["uuid"],
                }
                resp_remove_item_label1 = api_utils.post(
                    V2_REMOVE_ITEM_LABEL, params=pl_remove_item_label1
                )
                assert_that(
                    resp_remove_item_label1["msg"], "Pre-condition: Remove Item Label failed"
                ).is_equal_to("Item Label Removed")
                resp_labels2 = api_utils.get(
                    V2_VIEW_ITEM_LABELS, params={"dataset": dataset["dataset"]}
                )
                assert_that(
                    len(resp_labels2["data"]), "Remove of the Item Label failed"
                ).is_equal_to(0)

    @staticmethod
    def wait_for_issue_count(
        api_utils,
        issue_type,
        issue_count,
        expected_count,
        issue_count_params,
        sleep_interval,
        timeout,
    ):
        """
        In some cases, the DQ application requires additional time to return the proper issue count.
        Perform retries per specified parameters.
        :param api_utils: Standard api_utils
        :param issue_type: The type of issue to check.
        :param issue_count: The returned issue count
        :param expected_count: The expected issue count
        :param issue_count_params: Parameters for the /v2/getissuecounts API call.  Example:
        issue_count_params = {"dataset": dataset, "runId": run_id}
        :param sleep_interval: Time in seconds to wait between retries
        :param timeout: Time in seconds after which to cease retrying
        :return: The issue count if/when it matches expected or the retry window has elapsed
        """
        if issue_count < expected_count:
            start_time = time.time()
            elapsed_time = 0
            while elapsed_time < timeout and issue_count < expected_count:
                time.sleep(sleep_interval)
                issue_count_response = api_utils.get(V2_GET_ISSUE_COUNTS, params=issue_count_params)
                issue_count = issue_count_response[issue_type]
                elapsed_time = time.time() - start_time

        return issue_count

    @staticmethod
    def build_pushdown_bigquery_rule_validation_response(dataset_def, rule_definition, rule_output):
        """BigQuery rule validation has limitations. Build custom text and return a 400 status
        code as expected results to match the application behavior."""
        expected_message = "default bigquery rule validation message, something went wrong"
        query = dataset_def["pushdown"]["sourceQuery"]

        if rule_definition["ruleType"] == "SQLF":
            expected_message = (
                "Please run on BigQuery console: SELECT 'TestRule' AS rule_name, * "
                "FROM (" + rule_output["ruleValue"] + ")"
            )
        elif rule_definition["ruleType"] == "SQLG":
            modified_query = str(query).replace("select ", "SELECT ")
            expected_message = (
                "Please run on BigQuery console: SELECT 'TestRule' AS rule_name, * "
                "FROM (" + modified_query + ")" + " WHERE (" + rule_output["ruleValue"] + ")"
            )

        # BigQuery rule validation always returns status code 400.  See DEV-61985 for details.
        expected_status_code = 400
        return {
            "expected_status_code": expected_status_code,
            "expected_message": expected_message,
        }

    @staticmethod
    def filter_dupes_occurs(
        dupes_archive_breaks_enabled,
        compare_link_ds_to_nolink_ds,
        dupe_list_in,
    ):
        """
        :param dupes_archive_breaks_enabled: Boolean value is archive breaks is enabled?
        :param compare_link_ds_to_nolink_ds: Boolean value comparing archive breaks to non archive?
        :param dupe_list_in: List of dupes findings
        :return: A copy of the input list of dupes potentially having some results removed

        With archive breaks enabled, pushdown dupe detection returns all rows from the table.
        Due to this, rows returned may be different when there are more than 2 occurrences.
        Remove affected records from both expected and actual results prior to processing
        to ensure consistent results
        Full validation of archived break records can occur separately to cover these values
        Skip modification if comparing archive breaks to non archive breaks as we limit the columns
        compared when comparing between archive breaks and non archive breaks datasets
        """
        dupe_list_out = copy.deepcopy(dupe_list_in)
        if dupes_archive_breaks_enabled and not compare_link_ds_to_nolink_ds:
            for dupe in dupe_list_in:
                if "occurs" in dupe.keys() and int(dupe["occurs"]) > 2:
                    dupe_list_out.remove(dupe)

        return dupe_list_out

    @staticmethod
    def float_if_possible(val_in):
        """
        Convert an input value to float if possible.  If not, return the original value unconverted.
        :param val_in: Value to be converted to number if possible
        :return: Converted value or original value
        """
        try:
            float(val_in)
            return float(val_in)
        except ValueError:
            return val_in

    @staticmethod
    def run_id_to_date_time(run_id):
        """
        Convert a runId to date time format
        :param run_id: runId YYYY-MM-DDTHH:MI:SS with or without milliseconds and UTC offset
        :return: date time YYYY-MM-DD HH:MI:SS
        """
        date_time = run_id[0:10] + " " + run_id[11:19]

        return date_time

    @staticmethod
    def rule_exists_in_rule_definitions(data, dataset_name, rule_name, rule_description):
        """
        :param data: List of Rule Definitions.
        :param dataset_name: Name of the dataset to check in the list.
        :param rule_name: Name of the rule to check in the list.
        :param rule_description: Business description value set in the rule.
        :return: bool true (in case rule exists) or false (in case doesn't exist).

        Checks whether a rule exists in the response data.
        If yes, returns true. Else, returns false.
        """
        return any(
            item.get("dataset") == dataset_name
            and item.get("ruleNm") == rule_name
            and item.get("businessDesc") == rule_description
            for item in data
        )

    @staticmethod
    def prepare_dupe_list_for_validation(
        dupe_list, ignore_case, included_columns, max_displayed_dupe_detail_count
    ):
        """
        Prepares a list of dupes findings for validation.  Removes information that is not
        consistent between runs, modifies case of text that is expected to vary in capitalization.
        :param dupe_list: List of dupes to prepare for validation.
        :param ignore_case: Boolean indicating whether case was ignored in dupe detection which
        generated the list of dupes.
        :param included_columns: List of columns that are included for dupe validation.
        :param max_displayed_dupe_detail_count: Integer indicating the maximum number of duplicate
        records returned for each dupe finding.
        :return:
        """
        # Fuzzy dupe match appends owl_id to field values to form item_values while exact match
        # prepends "occurs" values to field values to form item_values.  Since owl_id is not
        # guaranteed to be the same each run, check for owl_id column existing as an indicator
        # of fuzzy match and modify item_values removing owl_id prior to sorting and validating
        # the lists.  Do not modify exact match/occurs values because they are relevant.
        for dupe in dupe_list:
            if "owl_id" in dupe:
                new_item_value = dupe["item_value"].replace("," + dupe["owl_id"], "")
                dupe["item_value"] = new_item_value
            # When a column has more than 2 occurrences with different cases, any 2 may be returned
            # Convert to lower in this case to ensure reliable validation at the expense of
            # some precision in validation.
            # Remove this if output redesigned to show all variations
            if (
                ignore_case
                and "occurs" in dupe
                and int(dupe["occurs"]) > max_displayed_dupe_detail_count
            ):
                for column in dupe:
                    if column in included_columns:
                        dupe[column] = str(dupe[column]).lower()

        return dupe_list

    @staticmethod
    def remove_statistic_from_dataset_name(dataset_name):
        """
        Remove statistics from dataset names.  When parsing dataset names in rules, statistics may
        be included.  To isolate the dataset name, remove the statistic from the string in the rule.
        :param dataset_name: String representing a dataset name in a rule
        :return: The dataset name without any statistic that had been appended to it
        """
        if dataset_name.find(".$") > 0:
            dataset_name = dataset_name[0 : dataset_name.index(".$")]

        return dataset_name

    @staticmethod
    def format_datetime_for_break_run_id_download(date_time):
        """Format a date for download of break records.  This format could change and there will
        likely be many references so perform the update in a helper method."""
        date_time = date_time + " 00:00:00.0"
        return date_time

    @staticmethod
    def outliers_config_contains_id(dataset_defs):
        """
        Determine if a dataset contains outliers configurations that have an id.  This is
        useful to know as when an outlier configuration contains an id value, it should not be
        submitted as it exists since that id may or may not be present in the environment which
        is under test and if present, the id may point to a different configuration.
        :param dataset_defs: The dataset definition to scan
        :return: Boolean indicating if the dataset contains saved outlier configurations
        """
        dataset_defs_contains_outlier_config_with_id = False
        if "outliers" in dataset_defs.keys():
            for outlier_config in dataset_defs["outliers"]:
                if "id" in outlier_config.keys():
                    dataset_defs_contains_outlier_config_with_id = True
                    break

        return dataset_defs_contains_outlier_config_with_id

    @staticmethod
    def delete_dataset_if_exists(api_utils, dataset):
        dataset_count = len(api_utils.get(V2_GET_DATASETS_BY_DATASET, params={"dataset": dataset}))

        if dataset_count > 0:
            api_utils.post(V2_DELETE_DATASET, params={"dataset": dataset})

    def create_dataset_runs_for_run_id_values(self, api_utils, dataset_defs, run_id_values):
        """
        Creates runs for the specified dataset definition with each of the runId values in the
        submitted list.
        :param api_utils: API Utils
        :param dataset_defs: The dataset definition to be used for the runs.
        :param run_id_values: A list of runId values to create runs using the supplied dataset
        definition.
        :return:
        """
        run_jobs_dataset_defs = copy.deepcopy(dataset_defs)
        is_pushdown_dataset = self.is_pushdown_dataset_defs(run_jobs_dataset_defs)
        for run_id in run_id_values:
            run_jobs_dataset_defs["runId"] = run_id
            if is_pushdown_dataset:
                self.run_pushdown_job(api_utils, run_jobs_dataset_defs)
            else:
                self.setup_dataset(api_utils, run_jobs_dataset_defs)

    @staticmethod
    def generate_ai_rule(api_utils, ai_prompt_payload, rule_definition):
        """
        Sends payload to the AI rule generator and returns the response
        :param api_utils: API Utils
        :param ai_prompt_payload: The payload sent in the AI Prompt
        :param rule_definition: Payload for rule syntax validation
        :return: Generated syntax for the rule
        """
        ai_generate = api_utils.post(V2_AI_GENERATE, params=ai_prompt_payload, return_json=False)
        rule_definition["ruleValue"] = ai_generate.text

        return rule_definition

    @staticmethod
    def determine_expected_source_finding_count(
        source_count_comparison,
        source_schema_comparison,
        source_value_comparison=None,
    ):
        """
        Validate Source has three components.  Determine the expected finding count from output of
        the three API calls.
        :param source_count_comparison: Expected output of /v2/get-source-count-comparison.
        :param source_schema_comparison: Expected output of /v2/get-source-schema-comparison.
        :param source_value_comparison: Expected output of /v2/get-source-value-comparison.
        :return: The expected count of source findings reported.
        """
        expected_source_count = 0

        if "data" in source_count_comparison.keys():
            for count_data in source_count_comparison["data"]:
                if count_data["change"] != 0:
                    expected_source_count += 1

        if "data" in source_schema_comparison.keys():
            non_matching_schema_records = 0
            for schema_record in source_schema_comparison["data"]:
                if schema_record["itemLabel"] != "Passing":
                    non_matching_schema_records += 1
            expected_source_count += non_matching_schema_records

        if source_value_comparison is not None and "data" in source_value_comparison.keys():
            value_findings_ids = []
            for value_finding in source_value_comparison["data"]:
                value_findings_ids.append(value_finding["id"])
            unique_value_finding_ids = set(value_findings_ids)
            expected_source_count += len(unique_value_finding_ids)

        return expected_source_count

    @staticmethod
    def get_pd_job_payload_sales(connection, dataset_name, include_columns, source_query):
        """Returns the job payload for PD job
        based on the connection, dataset name, table columns and source query."""
        job_payload = copy.deepcopy(PL_PD_NEW_DATASET_DEFAULT)
        job_payload["dataset"] = dataset_name
        job_payload["env"]["dataset"] = dataset_name
        job_payload["profile"]["include"] = include_columns
        job_payload["pushdown"]["connectionName"] = connection
        job_payload["pushdown"]["dataset"] = dataset_name
        job_payload["pushdown"]["sourceQuery"] = source_query
        return job_payload

    @staticmethod
    def get_pu_job_payload_sales(dataset_name):
        """Returns the job payload for a PU job by setting the given DS name"""
        job_payload = copy.deepcopy(PL_JOB_PAYLOAD_DEFAULT)
        job_payload["dataset"] = dataset_name
        job_payload["load"]["dataset"] = dataset_name
        job_payload["pushdown"]["dataset"] = dataset_name
        job_payload["profile"]["dataset"] = dataset_name
        job_payload["colMatch"]["dataset"] = dataset_name
        job_payload["spark"]["dataset"] = dataset_name
        job_payload["env"]["dataset"] = dataset_name
        return job_payload

    @staticmethod
    def run_pushdown_job_v3(api_utils, dataset_creation_payload):
        """
        Creates and runs a pushdown job using the V3 apis
        :param api_utils: API Utils
        :param dataset_creation_payload: dataset definition for creating a job
        :return: status of the job
        """
        dataset_creation_payload["host"] = constants.PROD_HOST
        dataset_creation_payload["user"] = constants.BASE_CREDS["username"]
        dataset_creation_response = api_utils.post(
            V3_DATASETDEFS, data=(json.dumps(dataset_creation_payload))
        )

        job_params = {
            "dataset": dataset_creation_response["dataset"],
            "runDate": dataset_creation_response["runId"],
            "agentName": "0",
        }
        job_creation_response = api_utils.post(V3_JOBS_RUN, params=job_params)

        job_id = job_creation_response["jobId"]

        job_output = api_utils.get(V3_JOBS_JOBID_WAITFORCOMPLETION.format(jobId=job_id))

        return job_output
