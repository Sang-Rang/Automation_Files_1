from payloads.pushdown.rules.pl_pd_dbrks_rules_basic import PD_DBRKS_RULES_BASIC_DATASET

PD_DBRKS_RULES_BASIC_RULE_DEFINITIONS = [
    {
        "dataset": PD_DBRKS_RULES_BASIC_DATASET,
        "ruleNm": "if_zip_code_is_NULL",
        "ruleType": "NULLCHECK",
        "ruleValue": "zip_code",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "zip_code",
        "businessCategory": None,
        "businessDesc": None,
        "dimId": 1,
        "dimName": "COMPLETENESS",
        "ruleValueBuilder": None,
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PD_DBRKS_RULES_BASIC_DATASET,
        "ruleNm": "if_gender_is_GENDER",
        "ruleType": "CUSTOM",
        "ruleValue": "gender",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "GENDER",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "gender",
        "businessCategory": None,
        "businessDesc": None,
        "dimId": 4,
        "dimName": "VALIDITY",
        "ruleValueBuilder": None,
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PD_DBRKS_RULES_BASIC_DATASET,
        "ruleNm": "FF_exception",
        "ruleType": "SQLF",
        "ruleValue": "This rule will cause an exception.",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": "Unexpected exception: \"[Databricks][JDBCDriver](500051) ERROR processing "
                     "query/statement. Error Code: 0, SQL state: 42601, Query: SELECT 'FF***, "
                     "Error message from Server: org.apache.hive.service.cli.HiveSQLException: "
                     "Error running query: [PARSE_SYNTAX_ERROR] org.apache.spark.sql.catalyst."
                     "parser.ParseException:  [PARSE_SYNTAX_ERROR] Syntax error at or near 'will': "
                     "missing ')'. SQLSTATE: 42601 (line 1, pos 68)  == SQL == SELECT "
                     "'FF_exception' AS rule_name, COUNT(*) AS cnt FROM (This rule will cause an "
                     "exception.) GROUP BY rule_name "
                     "--------------------------------------------------------------------^^^  "
                     "\tat org.apache.spark.sql.hive.thriftserver.HiveThriftServerErrors$"
                     ".runningQueryError(HiveThriftServerErrors.scala:49) \tat org.apache.spark.sql"
                     ".hive.thriftserver.SparkExecuteStatementOperation.$anonfun$execute$1("
                     "SparkExecuteStatementOperation.scala:786) \tat scala.runtime.java8."
                     "JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23) \tat com.databricks.unity."
                     "UCSEphemeralState$Handle.runWith(UCSEphemeralState.scala:51) \tat "
                     "com.databricks.unity.HandleImpl.runWith(UCSHandle.scala:104) \tat org.apache."
                     "spark.sql.hive.thriftserver.SparkExecuteStatementOperation.org"
                     "$apache$spark$sql$hive$thriftserver$SparkExecuteStatementOperation$$execute"
                     "(SparkExecuteStatementOperation.scala:624) \tat org.apache.spark.sql.hive."
                     "thriftserver.SparkExecuteStatementOperation$$anon$2$$anon$3."
                     "$anonfun$run$5(SparkExecuteStatementOperation.scala:469) \tat scala.runtime."
                     "java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23) \tat org.apache."
                     "spark.sql.execution.SQLExecution$.withRootExecution(SQLExecution.scala:704) "
                     "\tat org.apache.spark.sql.hive.thriftserver."
                     "SparkExecuteStatementOperation$$anon$2$$anon$3."
                     "$anonfun$run$2(SparkExecuteStatementOperation.scala:469) \tat scala.runtime."
                     "java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23) \tat com.databricks."
                     "logging.AttributionContextTracing."
                     "$anonfun$withAttributionContext$1(AttributionContextTracing.scala:48) "
                     "\tat com.databricks.logging.AttributionContext$."
                     "$anonfun$withValue$1(AttributionContext.scala:276) "
                     "\tat scala.util.DynamicVariable.withValue(DynamicVariable.scala:62) \tat "
                     "com.databricks.logging.AttributionContext$.withValue(AttributionContext."
                     "scala:272) \tat com.databricks.logging.AttributionContextTracing."
                     "withAttributionContext(AttributionContextTracing.scala:46) \tat com."
                     "databricks.logging.AttributionContextTracing."
                     "withAttributionContext$(AttributionContextTracing.scala:43) \tat "
                     "com.databricks.spark.util.PublicDBLogging."
                     "withAttributionContext(DatabricksSparkUsageLogger.scala:27) \tat "
                     "com.databricks.logging.AttributionContextTracing."
                     "withAttributionTags(AttributionContextTracing.scala:95) \tat "
                     "com.databricks.logging.AttributionContextTracing."
                     "withAttributionTags$(AttributionContextTracing.scala:76) \tat "
                     "com.databricks.spark.util.PublicDBLogging."
                     "withAttributionTags(DatabricksSparkUsageLogger.scala:27) \tat "
                     "com.databricks.spark.util.PublicDBLogging."
                     "withAttributionTags0(DatabricksSparkUsageLogger.scala:74) \tat "
                     "com.databricks.spark.util.DatabricksSparkUsageLogger."
                     "withAttributionTags(DatabricksSparkUsageLogger.scala:174) \tat "
                     "com.databricks.spark.util.UsageLogging."
                     "$anonfun$withAttributionTags$1(UsageLogger.scala:617) \tat "
                     "com.databricks.spark.util.UsageLogging$."
                     "withAttributionTags(UsageLogger.scala:729) \tat com.databricks.spark.util."
                     "UsageLogging$.withAttributionTags(UsageLogger.scala:738) \tat com.databricks."
                     "spark.util.UsageLogging.withAttributionTags(UsageLogger.scala:617) \tat "
                     "com.databricks.spark.util.UsageLogging.withAttributionTags$(UsageLogger."
                     "scala:615) \tat org.apache.spark.sql.hive.thriftserver."
                     "SparkExecuteStatementOperation."
                     "withAttributionTags(SparkExecuteStatementOperation.scala:71) \tat org.apache."
                     "spark.sql.hive.thriftserver.ThriftLocalProperties."
                     "$anonfun$withLocalProperties$12(ThriftLocalProperties.scala:234) \tat "
                     "com.databricks.spark.util.IdentityClaim$.withClaim(IdentityClaim.scala:48) "
                     "\tat org.apache.spark.sql.hive.thriftserver.ThriftLocalProperties."
                     "withLocalProperties(ThriftLocalProperties.scala:229) \tat org.apache.spark."
                     "sql.hive.thriftserver.ThriftLocalProperties."
                     "withLocalProperties$(ThriftLocalProperties.scala:89) \tat org.apache.spark."
                     "sql.hive.thriftserver.SparkExecuteStatementOperation."
                     "withLocalProperties(SparkExecuteStatementOperation.scala:71) \tat org.apache."
                     "spark.sql.hive.thriftserver.SparkExecuteStatementOperation$$anon$2$$anon$3."
                     "run(SparkExecuteStatementOperation.scala:446) \tat org.apache.spark.sql.hive."
                     "thriftserver.SparkExecuteStatementOperation$$anon$2$$anon$3."
                     "run(SparkExecuteStatementOperation.scala:432) \tat java.base/java.security."
                     "AccessController.doPrivileged(AccessController.java:712) \tat "
                     "java.base/javax.security.auth.Subject.doAs(Subject.java:439) \tat org.apache."
                     "hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1899) "
                     "\tat org.apache.spark.sql.hive.thriftserver."
                     "SparkExecuteStatementOperation$$anon$2.run(SparkExecuteStatementOperation."
                     "scala:482) \tat java.base/java.util.concurrent.Executors$RunnableAdapter."
                     "call(Executors.java:539) \tat java.base/java.util.concurrent.FutureTask."
                     "run(FutureTask.java:264) \tat java.base/java.util.concurrent."
                     "ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1136) \tat java."
                     "base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor."
                     "java:635) \tat java.base/java.lang.Thread.run(Thread.java:840) Caused by: "
                     "org.apache.spark.sql.catalyst.parser.ParseException:  [PARSE_SYNTAX_ERROR] "
                     "Syntax error at or near 'will': missing ')'. SQLSTATE: 42601 (line 1, pos 68)"
                     "  == SQL == SELECT 'FF_exception' AS rule_name, COUNT(*) AS cnt FROM "
                     "(This rule will cause an exception.) GROUP BY rule_name "
                     "--------------------------------------------------------------------^^^  "
                     "\tat org.apache.spark.sql.catalyst.parser.ParseException."
                     "withCommand(parsers.scala:308) \tat org.apache.spark.sql.catalyst.parser."
                     "AbstractParser.parse(parsers.scala:114) \tat org.apache.spark.sql.execution."
                     "SparkSqlParser.parse(SparkSqlParser.scala:137) \tat org.apache.spark.sql."
                     "catalyst.parser.AbstractSqlParser.parsePlan(AbstractSqlParser.scala:106) "
                     "\tat com.databricks.sql.parser.DatabricksSqlParser."
                     "$anonfun$parsePlan$1(DatabricksSqlParser.scala:80) \tat com.databricks.sql."
                     "parser.DatabricksSqlParser.parse(DatabricksSqlParser.scala:101) \tat com."
                     "databricks.sql.parser.DatabricksSqlParser.parsePlan(DatabricksSqlParser."
                     "scala:77) \tat com.databricks.sql.QueryRuntimePredictionUtils$."
                     "$anonfun$getParsedPlanWithTracking$2(QueryRuntimePrediction.scala:383) "
                     "\tat com.databricks.spark.util.FrameProfiler$.record(FrameProfiler.scala:94) "
                     "\tat org.apache.spark.sql.catalyst.QueryPlanningTracker."
                     "measurePhase(QueryPlanningTracker.scala:453) \tat com.databricks.sql."
                     "QueryRuntimePredictionUtils$."
                     "$anonfun$getParsedPlanWithTracking$1(QueryRuntimePrediction.scala:382) "
                     "\tat org.apache.spark.sql.execution.SQLExecution$."
                     "withExecutionPhase(SQLExecution.scala:143) \tat com.databricks.sql."
                     "QueryRuntimePredictionUtils$."
                     "getParsedPlanWithTracking(QueryRuntimePrediction.scala:382) \tat "
                     "com.databricks.sql.QueryRuntimePrediction."
                     "$anonfun$getQueryExecutionWithParsedPlan$1(QueryRuntimePrediction.scala:668) "
                     "\tat org.apache.spark.sql.SparkSession.withActive(SparkSession.scala:1180) "
                     "\tat com.databricks.sql.QueryRuntimePrediction."
                     "getQueryExecutionWithParsedPlan(QueryRuntimePrediction.scala:665) \tat "
                     "com.databricks.sql.QueryRuntimePrediction."
                     "getRuntimeCategory(QueryRuntimePrediction.scala:485) \tat com.databricks.sql."
                     "ClusterLoadMonitor."
                     "$anonfun$getRuntimeCategory$3(ClusterLoadMonitor.scala:602) \tat com."
                     "databricks.unity.UCSEphemeralState$Handle.runWith(UCSEphemeralState.scala:51)"
                     " \tat com.databricks.unity.HandleImpl.runWith(UCSHandle.scala:104) \tat "
                     "com.databricks.unity.HandleImpl.$anonfun$runWithAndClose$1(UCSHandle."
                     "scala:109) \tat scala.util.Using$.resource(Using.scala:269) \tat com."
                     "databricks.unity.HandleImpl.runWithAndClose(UCSHandle.scala:108) \tat "
                     "com.databricks.sql.ClusterLoadMonitor."
                     "$anonfun$getRuntimeCategory$2(ClusterLoadMonitor.scala:598) \tat java."
                     "base/java.util.concurrent.CompletableFuture$AsyncSupply."
                     "run(CompletableFuture.java:1768) \tat org.apache.spark.util.threads."
                     "SparkThreadLocalCapturingRunnable."
                     "$anonfun$run$1(SparkThreadLocalForwardingThreadPoolExecutor.scala:157) \tat "
                     "scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23) \tat "
                     "com.databricks.spark.util.IdentityClaim$.withClaim(IdentityClaim.scala:48) "
                     "\tat org.apache.spark.util.threads.SparkThreadLocalCapturingHelper."
                     "$anonfun$runWithCaptured$4(SparkThreadLocalForwardingThreadPoolExecutor."
                     "scala:113) \tat com.databricks.unity."
                     "UCSEphemeralState$Handle.runWith(UCSEphemeralState.scala:51) \tat org.apache."
                     "spark.util.threads.SparkThreadLocalCapturingHelper."
                     "runWithCaptured(SparkThreadLocalForwardingThreadPoolExecutor.scala:112) "
                     "\tat org.apache.spark.util.threads.SparkThreadLocalCapturingHelper."
                     "runWithCaptured$(SparkThreadLocalForwardingThreadPoolExecutor.scala:89) \tat "
                     "org.apache.spark.util.threads.SparkThreadLocalCapturingRunnable."
                     "runWithCaptured(SparkThreadLocalForwardingThreadPoolExecutor.scala:154) \tat "
                     "org.apache.spark.util.threads.SparkThreadLocalCapturingRunnable."
                     "run(SparkThreadLocalForwardingThreadPoolExecutor.scala:157) \t... 3 more .\"",
        "columnName": None,
        "businessCategory": "",
        "businessDesc": "",
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": None,
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PD_DBRKS_RULES_BASIC_DATASET,
        "ruleNm": "stat_rule",
        "ruleType": "SQLF",
        "ruleValue": f"select * from @{PD_DBRKS_RULES_BASIC_DATASET} where $rowCount > 1000",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": None,
        "businessCategory": None,
        "businessDesc": None,
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": "condition,rules,not,valid",
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PD_DBRKS_RULES_BASIC_DATASET,
        "ruleNm": "FF_long",
        "ruleType": "SQLF",
        "ruleValue": f"select * from @{PD_DBRKS_RULES_BASIC_DATASET} where auto_year = 2001",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": None,
        "businessCategory": None,
        "businessDesc": None,
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": "condition,rules,not,valid",
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    },
    {
        "dataset": PD_DBRKS_RULES_BASIC_DATASET,
        "ruleNm": "SIMPLE_STRING",
        "ruleType": "SQLG",
        "ruleValue": "auto_make = 'Ford'",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": None,
        "businessCategory": None,
        "businessDesc": None,
        "dimId": None,
        "dimName": None,
        "ruleValueBuilder": "condition,rules,not,valid",
        "previewLimit": 6,
        "runTimeLimit": 30.0,
        "scoringScheme": 0,
        "filterQuery": None,
        "tolerance": 0,
        "active": True
    }
]

PD_DBRKS_RULES_BASIC_EXPECTED_RULE_OUTPUT = {
    "data": [
        {
            "dataset": PD_DBRKS_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "stat_rule",
            "ruleType": "SQLF",
            "ruleValue": "select * from (select * from public.customers) where 1044 > 1000",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585958,
                "uuid": "76dd44c9-df02-4c64-9a01-08441759d166"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"select * from @{PD_DBRKS_RULES_BASIC_DATASET} "
                             f"where $rowCount > 1000",
            "totalCount": 1044,
            "rowsBreaking": 1044,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_DBRKS_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "SIMPLE_STRING",
            "ruleType": "SQLG",
            "ruleValue": "auto_make = 'Ford'",
            "filterQuery": None,
            "score": 8,
            "perc": 8.237547892720306,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585959,
                "uuid": "f70d9970-a4e2-4d2e-818e-c78c0bf5c278"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "auto_make = 'Ford'",
            "totalCount": 1044,
            "rowsBreaking": 86,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_DBRKS_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "if_zip_code_is_NULL",
            "ruleType": "NULLCHECK",
            "ruleValue": "zip_code",
            "filterQuery": None,
            "score": 48,
            "perc": 48.85057471264368,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585960,
                "uuid": "4500fd75-d269-4128-9430-c865025ea749"
            },
            "dimId": 1,
            "dimName": "COMPLETENESS",
            "ruleCondition": "zip_code",
            "totalCount": 1044,
            "rowsBreaking": 510,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_DBRKS_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "if_gender_is_GENDER",
            "ruleType": "CUSTOM",
            "ruleValue": "gender",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "PASSING",
            "assignmentId": {
                "id": 1585963,
                "uuid": "61453998-439a-44a2-bb50-da57b6b49100"
            },
            "dimId": 4,
            "dimName": "VALIDITY",
            "ruleCondition": "gender",
            "totalCount": 1044,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_DBRKS_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_long",
            "ruleType": "SQLF",
            "ruleValue": "select * from (select * from public.customers) where auto_year = 2001",
            "filterQuery": None,
            "score": 4,
            "perc": 4.597701149425287,
            "exception": None,
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 1585962,
                "uuid": "90ddb466-0220-4249-ba55-eee2a41b12ff"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": f"select * from @{PD_DBRKS_RULES_BASIC_DATASET} "
                             f"where auto_year = 2001",
            "totalCount": 1044,
            "rowsBreaking": 48,
            "tolerance": 0,
            "ruleStatus": None
        },
        {
            "dataset": PD_DBRKS_RULES_BASIC_DATASET,
            "runId": "2024-10-31T00:00:00.000+0000",
            "ruleNm": "FF_exception",
            "ruleType": "SQLF",
            "ruleValue": "This rule will cause an exception.",
            "filterQuery": None,
            "score": 0,
            "perc": 0.0,
            "exception": "Unexpected exception: \"[Databricks][JDBCDriver](500051) "
                         "ERROR processing query/statement. Error Code: 0, SQL state: 42601, "
                         "Query: SELECT 'FF***, Error message from Server: org.apache.hive.service."
                         "cli.HiveSQLException: Error running query: [PARSE_SYNTAX_ERROR] "
                         "org.apache.spark.sql.catalyst.parser.ParseException:  "
                         "[PARSE_SYNTAX_ERROR] Syntax error at or near 'will': missing ')'. "
                         "SQLSTATE: 42601 (line 1, pos 68)  == SQL == SELECT 'FF_exception' "
                         "AS rule_name, COUNT(*) AS cnt FROM (This rule will cause an exception.) "
                         "GROUP BY rule_name "
                         "--------------------------------------------------------------------^^^  "
                         "\tat org.apache.spark.sql.hive.thriftserver.HiveThriftServerErrors$."
                         "runningQueryError(HiveThriftServerErrors.scala:49) \tat "
                         "org.apache.spark.sql.hive.thriftserver.SparkExecuteStatementOperation."
                         "$anonfun$execute$1(SparkExecuteStatementOperation.scala:786) \tat scala."
                         "runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23) \tat "
                         "com.databricks.unity.UCSEphemeralState$Handle.runWith(UCSEphemeralState."
                         "scala:51) \tat com.databricks.unity.HandleImpl."
                         "runWith(UCSHandle.scala:104) \tat org.apache.spark.sql.hive."
                         "thriftserver.SparkExecuteStatementOperation."
                         "org$apache$spark$sql$hive$thriftserver$SparkExecuteStatementOperation$$"
                         "execute(SparkExecuteStatementOperation.scala:624) \tat org.apache.spark."
                         "sql.hive.thriftserver.SparkExecuteStatementOperation$$anon$2$$anon$3."
                         "$anonfun$run$5(SparkExecuteStatementOperation.scala:469) \tat scala."
                         "runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23) \tat "
                         "org.apache.spark.sql.execution.SQLExecution$.withRootExecution"
                         "(SQLExecution.scala:704) \tat org.apache.spark.sql.hive.thriftserver."
                         "SparkExecuteStatementOperation$$anon$2$$anon$3.$anonfun$run$2("
                         "SparkExecuteStatementOperation.scala:469) \tat scala.runtime.java8."
                         "JFunction0$mcV$sp.apply(JFunction0$mcV$sp.java:23) \tat com.databricks."
                         "logging.AttributionContextTracing.$anonfun$withAttributionContext$1"
                         "(AttributionContextTracing.scala:48) \tat com.databricks.logging."
                         "AttributionContext$.$anonfun$withValue$1(AttributionContext.scala:276) "
                         "\tat scala.util.DynamicVariable.withValue(DynamicVariable.scala:62) "
                         "\tat com.databricks.logging.AttributionContext$.withValue("
                         "AttributionContext.scala:272) \tat com.databricks.logging."
                         "AttributionContextTracing.withAttributionContext("
                         "AttributionContextTracing.scala:46) \tat com.databricks.logging."
                         "AttributionContextTracing.withAttributionContext$("
                         "AttributionContextTracing.scala:43) \tat com.databricks.spark.util."
                         "PublicDBLogging.withAttributionContext(DatabricksSparkUsageLogger."
                         "scala:27) \tat com.databricks.logging.AttributionContextTracing."
                         "withAttributionTags(AttributionContextTracing.scala:95) \tat com."
                         "databricks.logging.AttributionContextTracing.withAttributionTags$("
                         "AttributionContextTracing.scala:76) \tat com.databricks.spark.util."
                         "PublicDBLogging.withAttributionTags(DatabricksSparkUsageLogger.scala:27) "
                         "\tat com.databricks.spark.util.PublicDBLogging.withAttributionTags0("
                         "DatabricksSparkUsageLogger.scala:74) \tat com.databricks.spark.util."
                         "DatabricksSparkUsageLogger.withAttributionTags(DatabricksSparkUsageLogger"
                         ".scala:174) \tat com.databricks.spark.util.UsageLogging.$anonfun$"
                         "withAttributionTags$1(UsageLogger.scala:617) \tat com.databricks.spark."
                         "util.UsageLogging$.withAttributionTags(UsageLogger.scala:729) \tat "
                         "com.databricks.spark.util.UsageLogging$.withAttributionTags(UsageLogger."
                         "scala:738) \tat com.databricks.spark.util.UsageLogging.withAttribution"
                         "Tags(UsageLogger.scala:617) \tat com.databricks.spark.util.UsageLogging."
                         "withAttributionTags$(UsageLogger.scala:615) \tat org.apache.spark.sql."
                         "hive.thriftserver.SparkExecuteStatementOperation.withAttributionTags("
                         "SparkExecuteStatementOperation.scala:71) \tat org.apache.spark.sql.hive."
                         "thriftserver.ThriftLocalProperties.$anonfun$withLocalProperties$12("
                         "ThriftLocalProperties.scala:234) \tat com.databricks.spark.util.Identity"
                         "Claim$.withClaim(IdentityClaim.scala:48) \tat org.apache.spark.sql.hive."
                         "thriftserver.ThriftLocalProperties.withLocalProperties("
                         "ThriftLocalProperties.scala:229) \tat org.apache.spark.sql.hive."
                         "thriftserver.ThriftLocalProperties.withLocalProperties$("
                         "ThriftLocalProperties.scala:89) \tat org.apache.spark.sql.hive."
                         "thriftserver.SparkExecuteStatementOperation.withLocalProperties("
                         "SparkExecuteStatementOperation.scala:71) \tat org.apache.spark.sql.hive."
                         "thriftserver.SparkExecuteStatementOperation$$anon$2$$anon$3.run("
                         "SparkExecuteStatementOperation.scala:446) \tat org.apache.spark.sql.hive."
                         "thriftserver.SparkExecuteStatementOperation$$anon$2$$anon$3.run("
                         "SparkExecuteStatementOperation.scala:432) \tat java.base/java.security."
                         "AccessController.doPrivileged(AccessController.java:712) \tat "
                         "java.base/javax.security.auth.Subject.doAs(Subject.java:439) \tat org."
                         "apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation."
                         "java:1899) \tat org.apache.spark.sql.hive.thriftserver."
                         "SparkExecuteStatementOperation$$anon$2.run(SparkExecuteStatementOperation"
                         ".scala:482) \tat java.base/java.util.concurrent.Executors$RunnableAdapter"
                         ".call(Executors.java:539) \tat java.base/java.util.concurrent.FutureTask"
                         ".run(FutureTask.java:264) \tat java.base/java.util.concurrent."
                         "ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1136) \tat "
                         "java.base/java.util.concurrent.ThreadPoolExecutor$Worker."
                         "run(ThreadPoolExecutor.java:635) \tat java.base/java.lang.Thread."
                         "run(Thread.java:840) Caused by: org.apache.spark.sql.catalyst.parser."
                         "ParseException:  [PARSE_SYNTAX_ERROR] Syntax error at or near 'will': "
                         "missing ')'. SQLSTATE: 42601 (line 1, pos 68)  == SQL == SELECT "
                         "'FF_exception' AS rule_name, COUNT(*) AS cnt FROM (This rule will cause "
                         "an exception.) GROUP BY rule_name "
                         "--------------------------------------------------------------------^^^  "
                         "\tat org.apache.spark.sql.catalyst.parser.ParseException.withCommand("
                         "parsers.scala:308) \tat org.apache.spark.sql.catalyst.parser."
                         "AbstractParser.parse(parsers.scala:114) \tat org.apache.spark.sql."
                         "execution.SparkSqlParser.parse(SparkSqlParser.scala:137) \tat org.apache."
                         "spark.sql.catalyst.parser.AbstractSqlParser.parsePlan(AbstractSqlParser."
                         "scala:106) \tat com.databricks.sql.parser.DatabricksSqlParser."
                         "$anonfun$parsePlan$1(DatabricksSqlParser.scala:80) \tat com.databricks."
                         "sql.parser.DatabricksSqlParser.parse(DatabricksSqlParser.scala:101) \tat "
                         "com.databricks.sql.parser.DatabricksSqlParser.parsePlan("
                         "DatabricksSqlParser.scala:77) \tat com.databricks.sql."
                         "QueryRuntimePredictionUtils$.$anonfun$getParsedPlanWithTracking$2("
                         "QueryRuntimePrediction.scala:383) \tat com.databricks.spark.util."
                         "FrameProfiler$.record(FrameProfiler.scala:94) \tat org.apache.spark.sql."
                         "catalyst.QueryPlanningTracker.measurePhase(QueryPlanningTracker."
                         "scala:453) \tat com.databricks.sql.QueryRuntimePredictionUtils$."
                         "$anonfun$getParsedPlanWithTracking$1(QueryRuntimePrediction.scala:382) "
                         "\tat org.apache.spark.sql.execution.SQLExecution$.withExecutionPhase("
                         "SQLExecution.scala:143) \tat com.databricks.sql."
                         "QueryRuntimePredictionUtils$.getParsedPlanWithTracking("
                         "QueryRuntimePrediction.scala:382) \tat com.databricks.sql."
                         "QueryRuntimePrediction.$anonfun$getQueryExecutionWithParsedPlan$1("
                         "QueryRuntimePrediction.scala:668) \tat org.apache.spark.sql.SparkSession."
                         "withActive(SparkSession.scala:1180) \tat com.databricks.sql."
                         "QueryRuntimePrediction.getQueryExecutionWithParsedPlan("
                         "QueryRuntimePrediction.scala:665) \tat com.databricks.sql."
                         "QueryRuntimePrediction.getRuntimeCategory(QueryRuntimePrediction.scala:"
                         "485) \tat com.databricks.sql.ClusterLoadMonitor."
                         "$anonfun$getRuntimeCategory$3(ClusterLoadMonitor.scala:602) \tat com."
                         "databricks.unity.UCSEphemeralState$Handle.runWith(UCSEphemeralState."
                         "scala:51) \tat com.databricks.unity.HandleImpl.runWith(UCSHandle."
                         "scala:104) \tat com.databricks.unity.HandleImpl."
                         "$anonfun$runWithAndClose$1(UCSHandle.scala:109) \tat scala.util.Using$."
                         "resource(Using.scala:269) \tat com.databricks.unity.HandleImpl."
                         "runWithAndClose(UCSHandle.scala:108) \tat com.databricks.sql."
                         "ClusterLoadMonitor.$anonfun$getRuntimeCategory$2(ClusterLoadMonitor."
                         "scala:598) \tat java.base/java.util.concurrent."
                         "CompletableFuture$AsyncSupply.run(CompletableFuture.java:1768) \tat "
                         "org.apache.spark.util.threads.SparkThreadLocalCapturingRunnable."
                         "$anonfun$run$1(SparkThreadLocalForwardingThreadPoolExecutor.scala:157) "
                         "\tat scala.runtime.java8.JFunction0$mcV$sp.apply(JFunction0$mcV$sp."
                         "java:23) \tat com.databricks.spark.util.IdentityClaim$.withClaim("
                         "IdentityClaim.scala:48) \tat org.apache.spark.util.threads."
                         "SparkThreadLocalCapturingHelper.$anonfun$runWithCaptured$4("
                         "SparkThreadLocalForwardingThreadPoolExecutor.scala:113) \tat com."
                         "databricks.unity.UCSEphemeralState$Handle.runWith(UCSEphemeralState."
                         "scala:51) \tat org.apache.spark.util.threads."
                         "SparkThreadLocalCapturingHelper.runWithCaptured("
                         "SparkThreadLocalForwardingThreadPoolExecutor.scala:112) \tat org.apache."
                         "spark.util.threads.SparkThreadLocalCapturingHelper.runWithCaptured$("
                         "SparkThreadLocalForwardingThreadPoolExecutor.scala:89) \tat org.apache."
                         "spark.util.threads.SparkThreadLocalCapturingRunnable.runWithCaptured("
                         "SparkThreadLocalForwardingThreadPoolExecutor.scala:154) \tat org.apache."
                         "spark.util.threads.SparkThreadLocalCapturingRunnable.run("
                         "SparkThreadLocalForwardingThreadPoolExecutor.scala:157) \t... 3 more .\"",
            "owlId": "1",
            "breakMsg": "EXCEPTION",
            "assignmentId": {
                "id": 1585961,
                "uuid": "beb61aac-6fc6-4312-8ec5-10e7f595db8b"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "This rule will cause an exception.",
            "totalCount": 1044,
            "rowsBreaking": 0,
            "tolerance": 0,
            "ruleStatus": None
        }
    ]
}
