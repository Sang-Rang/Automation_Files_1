from data_test.dq_dgc_integration.data_complex_rule_queries import ALIAS_RULE_NAME, \
    DERIVED_RULE_NAME, INNERJOIN_RULE_NAME, LOOKUP_RULE_NAME

DQ_DGC_GOVERNS_COLUMN_EXPECTED_RULE_1 = {
    "total": 3,
    "offset": 0,
    "limit": 1000,
    "results": [
        {
            "id": "0190cc38-9f21-72bc-b7f5-83ea54f58d8a",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1721413181217,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1721413181271,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "40e54081-7527-4a96-8676-7854a6e22349",
                "resourceType": "Asset",
                "name": DERIVED_RULE_NAME,
            },
            "target": {
                "id": "216dadd8-d31c-4550-89f6-57c1748a3b56",
                "resourceType": "Asset",
                "name":
                    "APPROVED_POSTGRES_UP\u003Epostgres\u003Epublic\u003Enyse\u003Eopen(column)",
            },
            "type": {"id": "00000000-0000-0000-0000-090000010022", "resourceType": "RelationType"},
        },
        {
            "id": "0190cc38-9f21-72bc-b7f5-83ea54f58d8c",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1721413181217,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1721413181271,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "40e54081-7527-4a96-8676-7854a6e22349",
                "resourceType": "Asset",
                "name": DERIVED_RULE_NAME,
            },
            "target": {
                "id": "32aac647-d6e7-4e0a-a462-2f2ac72f9a57",
                "resourceType": "Asset",
                "name":
                    "APPROVED_POSTGRES_UP\u003Epostgres\u003Epublic\u003Enyse\u003Eclose(column)",
            },
            "type": {"id": "00000000-0000-0000-0000-090000010022", "resourceType": "RelationType"},
        },
        {
            "id": "0190cc38-9f21-72bc-b7f5-83ea54f58d8e",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1721413181217,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1721413181271,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "40e54081-7527-4a96-8676-7854a6e22349",
                "resourceType": "Asset",
                "name": DERIVED_RULE_NAME,
            },
            "target": {
                "id": "a8c02a09-8613-4a07-a2d7-ed8f2eab4917",
                "resourceType": "Asset",
                "name":
                    "APPROVED_POSTGRES_UP\u003Epostgres\u003Epublic\u003Enyse\u003Esymbol(column)",
            },
            "type": {"id": "00000000-0000-0000-0000-090000010022", "resourceType": "RelationType"},
        },
    ],
}

DQ_DGC_GOVERNS_COLUMN_EXPECTED_RULE_2 = {
    "total": 2,
    "offset": 0,
    "limit": 1000,
    "results": [
        {
            "id": "0190cc38-9f21-72bc-b7f5-83ea54f58d94",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1721413181217,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1721413181271,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "c3a62733-e4aa-474a-b553-bdf1c9554511",
                "resourceType": "Asset",
                "name": ALIAS_RULE_NAME,
            },
            "target": {
                "id": "32aac647-d6e7-4e0a-a462-2f2ac72f9a57",
                "resourceType": "Asset",
                "name":
                    "APPROVED_POSTGRES_UP\u003Epostgres\u003Epublic\u003Enyse\u003Eclose(column)",
            },
            "type": {"id": "00000000-0000-0000-0000-090000010022", "resourceType": "RelationType"},
        },
        {
            "id": "0190cc38-9f21-72bc-b7f5-83ea54f58d96",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1721413181217,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1721413181270,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "c3a62733-e4aa-474a-b553-bdf1c9554511",
                "resourceType": "Asset",
                "name": ALIAS_RULE_NAME,
            },
            "target": {
                "id": "a8c02a09-8613-4a07-a2d7-ed8f2eab4917",
                "resourceType": "Asset",
                "name":
                    "APPROVED_POSTGRES_UP\u003Epostgres\u003Epublic\u003Enyse\u003Esymbol(column)",
            },
            "type": {"id": "00000000-0000-0000-0000-090000010022", "resourceType": "RelationType"},
        },
    ],
}

DQ_DGC_GOVERNS_COLUMN_EXPECTED_RULE_3 = {
    "total": 2,
    "offset": 0,
    "limit": 1000,
    "results": [
        {
            "id": "0190cc38-9f21-72bc-b7f5-83ea54f58d9c",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1721413181217,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1721413181271,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "19f42647-ecb8-47c4-8d60-d481f905f5bf",
                "resourceType": "Asset",
                "name": INNERJOIN_RULE_NAME,
            },
            "target": {
                "id": "781bd57b-c595-4e3b-b5d7-90bd974a148e",
                "resourceType": "Asset",
                "name":
                    "APPROVED_POSTGRES_UP\u003Epostgres\u003Epublic\u003Enyse\u003Eexch(column)",
            },
            "type": {"id": "00000000-0000-0000-0000-090000010022", "resourceType": "RelationType"},
        },
        {
            "id": "0190cc38-9f21-72bc-b7f5-83ea54f58d9e",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1721413181217,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1721413181270,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "19f42647-ecb8-47c4-8d60-d481f905f5bf",
                "resourceType": "Asset",
                "name": INNERJOIN_RULE_NAME,
            },
            "target": {
                "id": "a8c02a09-8613-4a07-a2d7-ed8f2eab4917",
                "resourceType": "Asset",
                "name":
                    "APPROVED_POSTGRES_UP\u003Epostgres\u003Epublic\u003Enyse\u003Esymbol(column)",
            },
            "type": {"id": "00000000-0000-0000-0000-090000010022", "resourceType": "RelationType"},
        },
    ],
}

DQ_DGC_GOVERNS_COLUMN_EXPECTED_RULE_4 = {
    "total": 2,
    "offset": 0,
    "limit": 1000,
    "results": [
        {
            "id": "0190cc05-5c2c-715f-a6df-bb037cf703e4",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1721409821740,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1721409821802,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "e419fe7b-1b3f-4445-9d15-d677aeccc72d",
                "resourceType": "Asset",
                "name": LOOKUP_RULE_NAME,
            },
            "target": {
                "id": "32aac647-d6e7-4e0a-a462-2f2ac72f9a57",
                "resourceType": "Asset",
                "name":
                    "APPROVED_POSTGRES_UP\u003Epostgres\u003Epublic\u003Enyse\u003Eclose(column)",
            },
            "type": {"id": "00000000-0000-0000-0000-090000010022", "resourceType": "RelationType"},
        },
        {
            "id": "0190cc05-5c2c-715f-a6df-bb037cf703e6",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1721409821740,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1721409821801,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "e419fe7b-1b3f-4445-9d15-d677aeccc72d",
                "resourceType": "Asset",
                "name": LOOKUP_RULE_NAME,
            },
            "target": {
                "id": "a8c02a09-8613-4a07-a2d7-ed8f2eab4917",
                "resourceType": "Asset",
                "name":
                    "APPROVED_POSTGRES_UP\u003Epostgres\u003Epublic\u003Enyse\u003Esymbol(column)",
            },
            "type": {"id": "00000000-0000-0000-0000-090000010022", "resourceType": "RelationType"},
        },
    ],
}
