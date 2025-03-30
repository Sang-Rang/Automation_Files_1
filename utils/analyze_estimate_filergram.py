import time

import pytest
from assertpy import assert_that, soft_assertions

from endpoints.v2.controller_agent import V2_GET_AGENT
from endpoints.v2.controller_connections import V2_GET_CONNECTION_BY_ALIAS
from endpoints.v2.controller_explorer import (
    V2_GET_DAYS_WITH_DATA1,
    V2_JOB_ESTIMATOR,
    V2_FILES_JOB_ESTIMATE,
    V2_GET_DAYS_WITH_DATA_FILE,
    V2_GET_READ_REMOTE_FILE_SYSTEMS,
)
from endpoints.v2.controller_hoot import (
    V2_GET_TABLE_STATS,
    V2_GET_DATASET_SCAN,
    V2_GET_DATASET_SCORING,
)
from endpoints.v2.controller_profile import V2_GET_FILTERGRAM
from utils.api_utils import APIUtils


class AnalyzeEstimateFiltergram:
    @pytest.fixture(scope="class")
    def api_utils(self, base_url, get_auth_headers):
        return APIUtils(base_url=base_url, headers=get_auth_headers)

    @staticmethod
    def rename_dataset_defs(dataset, new_name):
        ds_defs_new = dataset.copy()
        ds_defs_new["dataset"] = new_name
        ds_defs_new["load"]["dataset"] = new_name
        ds_defs_new["profile"]["dataset"] = new_name
        ds_defs_new["spark"]["dataset"] = new_name
        ds_defs_new["profile"]["profilePushDown"] = new_name
        return ds_defs_new

    @staticmethod
    def analyze(api_utils, pl_days_with_data, expected_days_with_data):
        """Requests and validates output of getDaysWithData1,
        if connection is databricks add re-try logic"""
        if pl_days_with_data["cxn"] == "APPROVED_CDATA_DATABRICKS_UP":
            max_retries = 50
            timeout = 3
            attempt = 0
            while attempt < max_retries:
                get_days_with_data = api_utils.get(V2_GET_DAYS_WITH_DATA1, params=pl_days_with_data)
                if any("rowcount" in item for item in get_days_with_data):
                    return get_days_with_data
                attempt += 1
                time.sleep(timeout)
        else:
            get_days_with_data = api_utils.get(V2_GET_DAYS_WITH_DATA1, params=pl_days_with_data)

        # If there is issue with connection, status is still 200,
        # so check for the different possible errors it could return.
        if ("message" in get_days_with_data) or (
            len(get_days_with_data) > 0 and "error" in get_days_with_data[0]
        ):
            raise ConnectionError(f"Connection problem detected. Result: {get_days_with_data}")

        for index, day in enumerate(get_days_with_data):
            for key, expected_value in expected_days_with_data[index].items():
                assert_that(day, f"Key not found. Data: {get_days_with_data}").contains_key(key)
                # Day format can be either date or timestamp and can switch between the two
                if key == "day":
                    assert_that(str(expected_value), f"Days With Data {key}").is_in(
                        str(day[key]),
                        str(day[key])[0:10],
                        str(day[key])[0:10] + "T00:00:00.000+0000",
                    )
                else:
                    assert_that(str(expected_value), f"Days With Data {key}").is_equal_to(
                        str(day[key])
                    )
        return get_days_with_data

    @staticmethod
    def analyze_file(api_utils, pl_days_with_data, expected_days_with_data):
        """Requests and validates output of getDaysWithDataFile"""
        get_days_with_data = api_utils.get(V2_GET_DAYS_WITH_DATA_FILE, params=pl_days_with_data)

        for index, day in enumerate(get_days_with_data):
            for key, expected_value in expected_days_with_data[index].items():
                assert_that(str(expected_value), f"Days With Data {key}").is_equal_to(str(day[key]))
        return get_days_with_data

    @staticmethod
    def job_estimator(api_utils, pl_job_estimator, expected_job_estimator):
        """Requests and validates output of jobEstimator
        Evaluates job estimator data, normally done before running job"""

        # Note: Typically only validate row & col counts in AEF tests.
        # Expected example =  {"rowCount": 1, "colCount": 1}

        # Update the job estimator driver and host name data
        connection_info = api_utils.get(
            V2_GET_CONNECTION_BY_ALIAS, params={"alias": pl_job_estimator["aliasname"]}
        )
        pl_job_estimator["drivername"] = connection_info["drivername"]
        pl_job_estimator["hostname"] = connection_info["hostname"]

        call_job_est = api_utils.post(V2_JOB_ESTIMATOR, params=pl_job_estimator)

        for key, expected_value in expected_job_estimator.items():
            assert_that(expected_value, f"Job Estimator {key}:").is_equal_to(call_job_est[key])
        return call_job_est

    @staticmethod
    def job_estimator_file(api_utils, pl_job_estimator, expected_job_estimator):
        """Requests and validates output of job file estimator
        Evaluates job estimator data, normally done before running job"""
        call_job_est = api_utils.post(V2_FILES_JOB_ESTIMATE, params=pl_job_estimator)

        for key, expected_value in expected_job_estimator.items():
            assert_that(expected_value, f"Job Estimator {key}:").is_equal_to(call_job_est[key])
        return call_job_est

    @staticmethod
    def row_count(api_utils, pl_dataset_stats, expected_row_count):
        """Requests and validates output of rowcount in getTableStats
        Evaluates finding's page table data"""
        call_table_stats = api_utils.get(V2_GET_TABLE_STATS, params=pl_dataset_stats)
        assert_that(call_table_stats["rows"], "Table Stats Row Count").is_equal_to(
            expected_row_count
        )
        return call_table_stats

    @staticmethod
    def dataset_scan(api_utils, payload_dataset_stats, expected_dataset_scan):
        """Requests and validates output of getDatasetScan
        Evaluates Finding page dataset data"""
        # Note: Remove variable data in expected results: updtTs, loadTimeDiff
        call_dataset_scan = api_utils.get(V2_GET_DATASET_SCAN, params=payload_dataset_stats)

        for key, expected_value in expected_dataset_scan.items():
            assert_that(expected_value, f"DS Scan {key}").is_equal_to(call_dataset_scan[key])
        return call_dataset_scan

    @staticmethod
    def scoring(api_utils, payload, expected_dataset_scoring):
        """Requests and validates output of getDatasetScoring
        Evaluates Finding page dataset data"""
        call_dataset_scoring = api_utils.get(V2_GET_DATASET_SCORING, params=payload)

        for key, expected_value in expected_dataset_scoring.items():
            assert_that(expected_value, f"Scoring {key}").is_equal_to(call_dataset_scoring[key])
        return call_dataset_scoring

    @staticmethod
    def filtergram(api_utils, pl_filtergram, expected_filtergram):
        """Requests and validates output of getFiltergram
        Evaluates profile page's Data Preview tab for given column"""
        call_filtergram = api_utils.get(V2_GET_FILTERGRAM, params=pl_filtergram)

        for key, expected_value in expected_filtergram.items():
            assert_that(call_filtergram, "Results did not contain expected data").contains_key(key)
            assert_that(expected_value, f"Filtergram {key}").is_equal_to(call_filtergram[key])
        return call_filtergram

    @staticmethod
    def read_remote_file(api_utils, pl_read_remote_file, expected_remote_file_data):
        """Requests and validates output of getReadRemoteFile
        Evaluates file being loaded before job begins"""
        resp_get_read_status = api_utils.get(
            V2_GET_READ_REMOTE_FILE_SYSTEMS, pl_read_remote_file, return_json=False
        )

        # Some remote connections often go down. Validate the read succeeded / report a clear error
        assert_that(
            resp_get_read_status.status_code,
            "Unable to load the data file, the connection may be down.",
        ).is_equal_to(200)

        resp_get_read = resp_get_read_status.json()
        for i, expected in enumerate(expected_remote_file_data):
            for key, expected_value in expected.items():
                assert_that(
                    str(expected_value), f"Read Remote FIle - {key} on item #{i}"
                ).is_equal_to(str(resp_get_read[i][key]))

    @staticmethod
    def validate_job_cmdline(api_utils, job_result):
        cmdline = job_result["cmdLine"]
        agent = api_utils.get(
            V2_GET_AGENT, {"agentid": job_result["agentId"], "agentuuid": job_result["agentUuid"]}
        )
        exec_memory = agent["executorMemory"]
        num_cores = agent["numCores"]
        num_executors = agent["numExecutors"]
        driver_memory = agent["driverMemory"]

        with soft_assertions():
            assert_that(cmdline, "Job cmd line numexecutors").contains(
                f"numexecutors {num_executors}"
            )
            assert_that(cmdline, "Job cmd line executor memory").contains(
                f"executormemory {exec_memory}"
            )
            assert_that(cmdline, "Job cmd line driver memory").contains(
                f"drivermemory {driver_memory}"
            )
            if num_cores is None or num_cores == 1:
                assert_that(cmdline, "Job cmd line executor cores null or 1").does_not_contain(
                    "executorcores"
                )
            else:
                assert_that(cmdline, "Job cmd line executor cores").contains(
                    f"executorcores {num_cores}"
                )
