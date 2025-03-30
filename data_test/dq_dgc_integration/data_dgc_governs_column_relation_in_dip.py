from payloads.dq_dgc_integration.pl_dq_dgc_column_relation_in_dic import (
    DS_DEF_DGC_COLUMN_RELATION_JOB_NAME,
)

OUTLIERS_GOVERNS_COLUMN_OUTPUT = {
    "total": 4,
    "offset": 0,
    "limit": 1000,
    "results": [
        {
            "id": "0191e202-40bc-79af-8b50-9803610d9525",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1726073684156,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1726073684212,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "42e3ce7e-ba3d-4ef2-b97b-b6415f3991e4",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "Outlier Finding",
            },
            "target": {
                "id": "018e8a91-dfef-78d3-bcd1-e50a8e40e61c",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002>first_name(column)",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010022",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        },
        {
            "id": "0191e202-40bc-79af-8b50-9803610d9527",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1726073684156,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1726073684212,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "42e3ce7e-ba3d-4ef2-b97b-b6415f3991e4",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "Outlier Finding",
            },
            "target": {
                "id": "018e8a91-dfef-78d3-bcd1-e50a8e40e624",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002>email(column)",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010022",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        },
        {
            "id": "0191e202-40bc-79af-8b50-9803610d9529",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1726073684156,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1726073684212,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "42e3ce7e-ba3d-4ef2-b97b-b6415f3991e4",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "Outlier Finding",
            },
            "target": {
                "id": "018e8a91-dfef-78d3-bcd1-e50a8e40e621",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002>last_name(column)",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010022",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        },
        {
            "id": "0191e202-40bc-79af-8b50-9803610d952b",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1726073684156,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1726073684212,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "42e3ce7e-ba3d-4ef2-b97b-b6415f3991e4",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "Outlier Finding",
            },
            "target": {
                "id": "018e8a91-dff0-7a55-91d1-d5878a132c18",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002>sales_id(column)",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010022",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        },
    ],
}

CUSTOM_RULE_GOVERNS_COLUMN_OUTPUT = {
    "total": 1,
    "offset": 0,
    "limit": 1000,
    "results": [
        {
            "id": "0191e240-8398-7b72-8142-a302eeb476f5",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1726077764504,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1726077764637,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "2d67b5c6-97c7-4b77-8282-2a8352bc6001",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "sales_rep_rule",
            },
            "target": {
                "id": "018e8a91-dff0-7a55-91d1-d5878a132c17",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002>sales_rep(column)",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010022",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        }
    ],
}

PATTERNS_RULE_GOVERNS_COLUMN_OUTPUT = {
    "total": 1,
    "offset": 0,
    "limit": 1000,
    "results": [
        {
            "id": "0191e240-8397-7856-84de-fab69b7f9a96",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1726077764503,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1726077764638,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "14de040d-18a4-48cd-8e07-398a3b339f52",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "Pattern Finding",
            },
            "target": {
                "id": "018e8a91-dfef-78d3-bcd1-e50a8e40e625",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002>state_tax(column)",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010022",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        }
    ],
}

SOURCE_RULE_GOVERNS_COLUMN_OUTPUT = {
    "total": 1,
    "offset": 0,
    "limit": 1000,
    "results": [
        {
            "id": "0194d2d5-b13a-79a7-aea7-e7fbe70fc96c",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1738704007482,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1738704007589,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "fa4ad10b-c008-4685-8ed3-1f11f05da75a",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "Source Finding",
            },
            "target": {
                "id": "018e8a91-dfef-78d3-bcd1-e50a8e40e620",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002>lost_column(column)",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010022",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        }
    ],
}

RECORD_RULE_GOVERNS_COLUMN_OUTPUT = {
    "total": 1,
    "offset": 0,
    "limit": 1000,
    "results": [
        {
            "id": "0191e240-8397-7856-84de-fab69b7f9aa2",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1726077764503,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1726077764637,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "306101a9-7ea5-40aa-83dc-5c57f7d1163a",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "Record Finding",
            },
            "target": {
                "id": "018e8a91-dff0-7a55-91d1-d5878a132c15",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002>daily_id(column)",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010022",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        }
    ],
}

SCHEMA_RULE_GOVERNS_COLUMN_OUTPUT = {
    "total": 1,
    "offset": 0,
    "limit": 1000,
    "results": [
        {
            "id": "0191e240-8397-7856-84de-fab69b7f9aa8",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1726077764503,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1726077764637,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "252caa32-84fb-402f-8027-a94d3a0cb754",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "Schema Finding",
            },
            "target": {
                "id": "018e8a91-dfef-78d3-bcd1-e50a8e40e622",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002>vendor_type(column)",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010022",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        }
    ],
}

DUPES_RULE_GOVERNS_COLUMN_OUTPUT = {
    "total": 3,
    "offset": 0,
    "limit": 1000,
    "results": [
        {
            "id": "0191e240-8397-7856-84de-fab69b7f9aae",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1726077764503,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1726077764638,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "cc7133a5-9fec-4963-b6b2-eddbbca00567",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "Duplicate Finding",
            },
            "target": {
                "id": "018e8a91-dfef-78d3-bcd1-e50a8e40e624",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002>email(column)",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010022",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        },
        {
            "id": "0191e240-8397-7856-84de-fab69b7f9ab0",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1726077764503,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1726077764638,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "cc7133a5-9fec-4963-b6b2-eddbbca00567",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "Duplicate Finding",
            },
            "target": {
                "id": "018e8a91-dfef-78d3-bcd1-e50a8e40e61c",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002>first_name(column)",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010022",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        },
        {
            "id": "0191e240-8397-7856-84de-fab69b7f9ab2",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1726077764503,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1726077764638,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "cc7133a5-9fec-4963-b6b2-eddbbca00567",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "Duplicate Finding",
            },
            "target": {
                "id": "018e8a91-dfef-78d3-bcd1-e50a8e40e621",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002>last_name(column)",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010022",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        },
    ],
}

SHAPES_RULE_GOVERNS_COLUMN_OUTPUT = {
    "total": 1,
    "offset": 0,
    "limit": 1000,
    "results": [
        {
            "id": "0191e240-8397-7856-84de-fab69b7f9aba",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1726077764503,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1726077764638,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "dd27aaae-4c9a-489c-bd2e-05c97183f693",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "Shape Finding",
            },
            "target": {
                "id": "018e8a91-dff0-7a55-91d1-d5878a132c11",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002>cost_code(column)",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010022",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        }
    ],
}

SALES_REP_ADAPTIVE_RULE_GOVERNS_COLUMN_OUTPUT = {
    "total": 1,
    "offset": 0,
    "limit": 1000,
    "results": [
        {
            "id": "0191e240-8398-7b72-8142-a302eeb476bf",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1726077764504,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1726077764637,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "4f5551f7-ee01-4ef3-aec3-56a1fd43da6b",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "sales_rep:Empty Range",
            },
            "target": {
                "id": "018e8a91-dff0-7a55-91d1-d5878a132c17",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002>sales_rep(column)",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010022",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        }
    ],
}

SALE_STATE_ADAPTIVE_RULE_GOVERNS_COLUMN_OUTPUT = {
    "total": 1,
    "offset": 0,
    "limit": 1000,
    "results": [
        {
            "id": "0191e240-8398-7b72-8142-a302eeb47675",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1726077764504,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1726077764638,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "492fa888-4a5e-4047-83e9-9db9f8aeced5",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "sale_state:Null Range",
            },
            "target": {
                "id": "018e8a91-dfef-78d3-bcd1-e50a8e40e623",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002>sale_state(column)",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010022",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        }
    ],
}

REPRESENTS_TABLE_OUTPUT = {
    "total": 1,
    "offset": 0,
    "limit": 1000,
    "results": [
        {
            "id": "0191e240-8397-7856-84de-fab69b7f9a84",
            "createdBy": "00000000-0000-0000-0000-000000900002",
            "createdOn": 1726077764503,
            "lastModifiedBy": "00000000-0000-0000-0000-000000900002",
            "lastModifiedOn": 1726077764638,
            "system": False,
            "resourceType": "Relation",
            "source": {
                "id": "112d3070-6202-493c-8a6e-931cfb7b8085",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": DS_DEF_DGC_COLUMN_RELATION_JOB_NAME,
            },
            "target": {
                "id": "018e8a91-dff0-7a55-91d1-d5878a132c13",
                "resourceType": "Asset",
                "resourceDiscriminator": "Asset",
                "name": "APPROVED_POSTGRES_UP>postgres>public>sales_data_002",
            },
            "type": {
                "id": "00000000-0000-0000-0000-090000010026",
                "resourceType": "RelationType",
                "resourceDiscriminator": "RelationType",
            },
        }
    ],
}
