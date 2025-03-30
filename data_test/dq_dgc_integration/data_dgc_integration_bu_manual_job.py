from payloads.dq_dgc_integration.pl_dq_dgc_manual_job_run import (
    DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME,
    DS_DEF_DGC_INTEGRATION_WITH_BU_JOB_NAME,
)

DQ_DGC_FREEFORM_RULE_DEFINITION = [
    {
        "dataset": DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME,
        "ruleNm": "close_is_not_null",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM @dataset WHERE close is NOT Null",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "close",
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
    }
]

DQ_DGC_FREEFORM_RULE_OUTPUT = {
    "data": [
        {
            "dataset": DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "close_is_not_null",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {DS_DEF_DGC_INTEGRATION_NO_BU_JOB_NAME}_dataset "
                         f"WHERE close is NOT Null ",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 434000,
                "uuid": "14404320-4793-4895-a753-4d41f17c4017"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM @dataset WHERE close is NOT Null",
            "totalCount": 102815,
            "rowsBreaking": 102815,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}

DQ_DGC_FREEFORM_RULE_DEFINITION_2 = [
    {
        "dataset": DS_DEF_DGC_INTEGRATION_WITH_BU_JOB_NAME,
        "ruleNm": "close_is_not_null",
        "ruleType": "SQLF",
        "ruleValue": "SELECT * FROM @dataset WHERE close is NOT Null",
        "points": 1,
        "perc": 1.0,
        "ruleRepo": "",
        "isActive": 1,
        "userNm": None,
        "exception": None,
        "columnName": "close",
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
    }
]

DQ_DGC_FREEFORM_RULE_OUTPUT_2 = {
    "data": [
        {
            "dataset": DS_DEF_DGC_INTEGRATION_WITH_BU_JOB_NAME,
            "runId": "2024-11-13T00:00:00.000+0000",
            "ruleNm": "close_is_not_null",
            "ruleType": "SQLF",
            "ruleValue": f"SELECT * FROM {DS_DEF_DGC_INTEGRATION_WITH_BU_JOB_NAME}_dataset "
                         f"WHERE close is NOT Null ",
            "filterQuery": None,
            "score": 100,
            "perc": 100.0,
            "exception": "",
            "owlId": "1",
            "breakMsg": "BREAKING",
            "assignmentId": {
                "id": 433895,
                "uuid": "233196eb-ad37-4c99-b840-ec517ad07f89"
            },
            "dimId": None,
            "dimName": None,
            "ruleCondition": "SELECT * FROM @dataset WHERE close is NOT Null",
            "totalCount": 102815,
            "rowsBreaking": 102815,
            "tolerance": 0,
            "ruleStatus": "BREAKING"
        }
    ]
}


DQ_BREADCRUMBS_BEFORE_UPDATE = {
    "dgcAssetUrl": "https://dg-qa-prevnew.collibra.com/asset/3b7bf38e-5c05-434f-8ab4-9a407120f949",
    "dgcUuid": "3b7bf38e-5c05-434f-8ab4-9a407120f949",
    "active": True,
    "communities": [
        {
            "id": "d5d036de-3e17-4216-a7dc-4509953a1eac",
            "resourceType": "Community",
            "name": "DQ_INTEGRATION_COMMUNITY",
        },
        {
            "id": "253384d6-165b-4698-8e1a-36d273ce146b",
            "resourceType": "Community",
            "name": "Unassigned DQ Job - DQ_INTEGRATION_COMMUNITY",
        },
        {
            "id": "0e3bf0f7-2392-473e-89e7-c87655ef643d",
            "resourceType": "Domain",
            "name": "DQ Job",
        },
    ],
}

DGC_BREADCRUMBS_BEFORE_UPDATE = [
    {
        "id": "d5d036de-3e17-4216-a7dc-4509953a1eac",
        "resourceType": "Community",
        "resourceDiscriminator": "Community",
        "name": "DQ_INTEGRATION_COMMUNITY",
    },
    {
        "id": "253384d6-165b-4698-8e1a-36d273ce146b",
        "resourceType": "Community",
        "resourceDiscriminator": "Community",
        "name": "Unassigned DQ Job - DQ_INTEGRATION_COMMUNITY",
    },
    {
        "id": "0e3bf0f7-2392-473e-89e7-c87655ef643d",
        "resourceType": "Domain",
        "resourceDiscriminator": "Domain",
        "name": "DQ Job",
    },
]

DQ_BREADCRUMBS_AFTER_UPDATE = {
    "dgcAssetUrl": "https://dg-qa-prevnew.collibra.com/asset/ec43c766-a7fb-45c8-88a9-4f3ab9aa1d5b",
    "dgcUuid": "ec43c766-a7fb-45c8-88a9-4f3ab9aa1d5b",
    "active": True,
    "communities": [
        {
            "id": "d5d036de-3e17-4216-a7dc-4509953a1eac",
            "resourceType": "Community",
            "name": "DQ_INTEGRATION_COMMUNITY",
        },
        {
            "id": "018d142a-159c-7cee-9457-7dba1fe297e2",
            "resourceType": "Community",
            "name": "JP",
        },
        {
            "id": "0191e81a-08b8-76fa-9665-10aae14ad539",
            "resourceType": "Community",
            "name": "Unassigned DQ Job - JP",
        },
        {
            "id": "c61b665f-6e66-4f8c-91e9-070d5fdd07e7",
            "resourceType": "Domain",
            "name": "DQ Job",
        },
    ],
}

DGC_BREADCRUMBS_AFTER_UPDATE = [
    {
        "id": "d5d036de-3e17-4216-a7dc-4509953a1eac",
        "resourceType": "Community",
        "resourceDiscriminator": "Community",
        "name": "DQ_INTEGRATION_COMMUNITY",
    },
    {
        "id": "018d142a-159c-7cee-9457-7dba1fe297e2",
        "resourceType": "Community",
        "resourceDiscriminator": "Community",
        "name": "JP",
    },
    {
        "id": "0191e81a-08b8-76fa-9665-10aae14ad539",
        "resourceType": "Community",
        "resourceDiscriminator": "Community",
        "name": "Unassigned DQ Job - JP",
    },
    {
        "id": "c61b665f-6e66-4f8c-91e9-070d5fdd07e7",
        "resourceType": "Domain",
        "resourceDiscriminator": "Domain",
        "name": "DQ Job",
    },
]

DQ_BREADCRUMBS_BEFORE_UPDATE_WITH_BU = {
    "dgcAssetUrl": "https://dg-qa-prevnew.collibra.com/asset/55fe5776-ac0e-479e-93ba-8142ae05ec22",
    "dgcUuid": "55fe5776-ac0e-479e-93ba-8142ae05ec22",
    "active": True,
    "communities": [
        {
            "id": "d5d036de-3e17-4216-a7dc-4509953a1eac",
            "resourceType": "Community",
            "name": "DQ_INTEGRATION_COMMUNITY",
        },
        {
            "id": "01902a12-b54e-7887-8a5c-78731c7e45f9",
            "resourceType": "Community",
            "name": "DQ_DGC_INTEGRATION_E2E_TEST",
        },
        {
            "id": "e0f782ba-31fe-492c-89b9-3155d9f6196f",
            "resourceType": "Domain",
            "name": "DQ Job",
        },
    ],
}

DGC_BREADCRUMBS_BEFORE_UPDATE_WITH_BU = [
    {
        "id": "d5d036de-3e17-4216-a7dc-4509953a1eac",
        "resourceType": "Community",
        "resourceDiscriminator": "Community",
        "name": "DQ_INTEGRATION_COMMUNITY",
    },
    {
        "id": "01902a12-b54e-7887-8a5c-78731c7e45f9",
        "resourceType": "Community",
        "resourceDiscriminator": "Community",
        "name": "DQ_DGC_INTEGRATION_E2E_TEST",
    },
    {
        "id": "e0f782ba-31fe-492c-89b9-3155d9f6196f",
        "resourceType": "Domain",
        "resourceDiscriminator": "Domain",
        "name": "DQ Job",
    },
]

DQ_BREADCRUMBS_AFTER_UPDATE_WITH_BU = {
    "dgcAssetUrl": "https://dg-qa-prevnew.collibra.com/asset/55fe5776-ac0e-479e-93ba-8142ae05ec22",
    "dgcUuid": "55fe5776-ac0e-479e-93ba-8142ae05ec22",
    "active": True,
    "communities": [
        {
            "id": "d5d036de-3e17-4216-a7dc-4509953a1eac",
            "resourceType": "Community",
            "name": "DQ_INTEGRATION_COMMUNITY",
        },
        {
            "id": "018d142a-159c-7cee-9457-7dba1fe297e2",
            "resourceType": "Community",
            "name": "JP",
        },
        {
            "id": "01902a12-b54e-7887-8a5c-78731c7e45f9",
            "resourceType": "Community",
            "name": "DQ_DGC_INTEGRATION_E2E_TEST",
        },
        {
            "id": "e0f782ba-31fe-492c-89b9-3155d9f6196f",
            "resourceType": "Domain",
            "name": "DQ Job",
        },
    ],
}

DGC_BREADCRUMBS_AFTER_UPDATE_WITH_BU = [
    {
        "id": "d5d036de-3e17-4216-a7dc-4509953a1eac",
        "resourceType": "Community",
        "resourceDiscriminator": "Community",
        "name": "DQ_INTEGRATION_COMMUNITY",
    },
    {
        "id": "018d142a-159c-7cee-9457-7dba1fe297e2",
        "resourceType": "Community",
        "resourceDiscriminator": "Community",
        "name": "JP",
    },
    {
        "id": "01902a12-b54e-7887-8a5c-78731c7e45f9",
        "resourceType": "Community",
        "resourceDiscriminator": "Community",
        "name": "DQ_DGC_INTEGRATION_E2E_TEST",
    },
    {
        "id": "e0f782ba-31fe-492c-89b9-3155d9f6196f",
        "resourceType": "Domain",
        "resourceDiscriminator": "Domain",
        "name": "DQ Job",
    },
]
