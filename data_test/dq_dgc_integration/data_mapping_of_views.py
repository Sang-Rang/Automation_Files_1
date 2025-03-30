MAPPING_OF_SCHEMAS_BEFORE_ADDING_VIEWS = {
  "dqName": "APPROVED_POSTGRES_UP",
  "dgcName": "APPROVED_POSTGRES_UP>postgres",
  "dgcUuid": "d4ae34d5-171c-402b-b4df-51cb0cb030c7",
  "id": "56dd03c4-b79e-4f4f-b57d-72686982ecfd",
  "credentialId": "c235a51d-7477-4a4a-a13d-9cea3b854b1e",
  "schemaMapping": [
    {
      "dgcSchema": "public",
      "dqSchema": "public",
      "dgcUuid": "09f2d6bf-0caf-408c-872b-ffbf7972810d",
      "id": "7ac9e67e-640e-4c4b-8925-20ab811d8db1",
      "tableMapping": [
        {
          "dqTable": "nyse",
          "dgcTable": "nyse",
          "dgcUuid": "d2990b93-cc02-49d2-9e72-cbdd1bb916af",
          "id": "3c174a5e-315b-4f6e-927e-1b1702fd63bd",
          "columnMapping": [
            {
              "dqColumn": "close(column)",
              "dgcColumn": "close(column)",
              "dgcUuid": "32aac647-d6e7-4e0a-a462-2f2ac72f9a57",
              "id": "0489db0b-5a24-4a89-8a05-aaef6e68eca9"
            },
            {
              "dqColumn": "exch(column)",
              "dgcColumn": "exch(column)",
              "dgcUuid": "781bd57b-c595-4e3b-b5d7-90bd974a148e",
              "id": "e6959953-9101-41ed-9bcc-54e55a3f1c91"
            },
            {
              "dqColumn": "high(column)",
              "dgcColumn": "high(column)",
              "dgcUuid": "97bb9afe-66ba-4388-b61c-dfc594ce3185",
              "id": "aa27ee94-4f04-4645-ac4e-c4aee7a8f7f9"
            },
            {
              "dqColumn": "low(column)",
              "dgcColumn": "low(column)",
              "dgcUuid": "07aa356f-3e8e-4594-b8dd-57265ff027da",
              "id": "ca125885-30a1-448f-8611-8306bb516f3d"
            },
            {
              "dqColumn": "open(column)",
              "dgcColumn": "open(column)",
              "dgcUuid": "216dadd8-d31c-4550-89f6-57c1748a3b56",
              "id": "32361d51-421a-46bf-9b4b-a7b979e51a8b"
            },
            {
              "dqColumn": "part_date_str(column)",
              "dgcColumn": "part_date_str(column)",
              "dgcUuid": "bb99591f-e207-4a16-afd0-94436fc245eb",
              "id": "d1238a2a-56b9-45c8-8655-1e704539f6d6"
            },
            {
              "dqColumn": "symbol(column)",
              "dgcColumn": "symbol(column)",
              "dgcUuid": "a8c02a09-8613-4a07-a2d7-ed8f2eab4917",
              "id": "c74f9c87-730e-4e10-9a34-ecad4c465537"
            },
            {
              "dqColumn": "trade_date(column)",
              "dgcColumn": "trade_date(column)",
              "dgcUuid": "61476882-04cc-4fac-8f18-868416b667ab",
              "id": "1b8ba03b-660b-457a-9464-8776add3fae7"
            },
            {
              "dqColumn": "volume(column)",
              "dgcColumn": "volume(column)",
              "dgcUuid": "175abb62-4762-4762-ba92-4bdf6446a6fc",
              "id": "3c4b2980-688a-4939-94e4-f1a07a40867a"
            }
          ],
          "totalRecords": 9,
          "mappedRecord": 9
        }
      ],
      "totalRecords": 372,
      "mappedRecord": 1
    }
  ]
}


MAPPING_OF_SCHEMAS_AFTER_ADDING_VIEWS = {
    "dqName": "APPROVED_POSTGRES_UP",
    "dgcName": "APPROVED_POSTGRES_UP>postgres",
    "dgcUuid": "d4ae34d5-171c-402b-b4df-51cb0cb030c7",
    "id": "89b04cec-36c6-4d82-b110-24865028cd3e",
    "credentialId": "57b797f4-464b-4487-bf2f-3fbedf64cdd2",
    "schemaMapping": [
        {
            "dgcSchema": "public",
            "dqSchema": "public",
            "dgcUuid": "09f2d6bf-0caf-408c-872b-ffbf7972810d",
            "id": "46258268-183c-4c24-b55d-b1da9f914ad4",
            "tableMapping": [
                {
                    "dqTable": "nyse",
                    "dgcTable": "nyse",
                    "dgcUuid": "d2990b93-cc02-49d2-9e72-cbdd1bb916af",
                    "id": "2ba2c914-e1f0-4908-9f88-ac1c3fb8b79d",
                    "columnMapping": [
                        {
                            "dqColumn": "close(column)",
                            "dgcColumn": "close(column)",
                            "dgcUuid": "32aac647-d6e7-4e0a-a462-2f2ac72f9a57",
                            "id": "c0bd23a6-9322-4672-9663-4735220b0d8f",
                        },
                        {
                            "dqColumn": "exch(column)",
                            "dgcColumn": "exch(column)",
                            "dgcUuid": "781bd57b-c595-4e3b-b5d7-90bd974a148e",
                            "id": "fed38817-a2bc-48ae-aba9-70342e23927a",
                        },
                        {
                            "dqColumn": "high(column)",
                            "dgcColumn": "high(column)",
                            "dgcUuid": "97bb9afe-66ba-4388-b61c-dfc594ce3185",
                            "id": "25a2d8d6-5729-4dfa-b006-5ac224a11601",
                        },
                        {
                            "dqColumn": "low(column)",
                            "dgcColumn": "low(column)",
                            "dgcUuid": "07aa356f-3e8e-4594-b8dd-57265ff027da",
                            "id": "d1b25d73-a86b-4d37-a6ca-a576533a9b2d",
                        },
                        {
                            "dqColumn": "open(column)",
                            "dgcColumn": "open(column)",
                            "dgcUuid": "216dadd8-d31c-4550-89f6-57c1748a3b56",
                            "id": "d90fcced-f9aa-4aa0-a23c-8d8b78162f83",
                        },
                        {
                            "dqColumn": "part_date_str(column)",
                            "dgcColumn": "part_date_str(column)",
                            "dgcUuid": "bb99591f-e207-4a16-afd0-94436fc245eb",
                            "id": "a0c7d227-dbc8-497b-b886-57fcaaf6edc9",
                        },
                        {
                            "dqColumn": "symbol(column)",
                            "dgcColumn": "symbol(column)",
                            "dgcUuid": "a8c02a09-8613-4a07-a2d7-ed8f2eab4917",
                            "id": "f9f211c5-81aa-4ec6-b7ed-66dbe72f388f",
                        },
                        {
                            "dqColumn": "trade_date(column)",
                            "dgcColumn": "trade_date(column)",
                            "dgcUuid": "61476882-04cc-4fac-8f18-868416b667ab",
                            "id": "c426397d-8a6e-4234-b037-42374cf5a7ee",
                        },
                        {
                            "dqColumn": "volume(column)",
                            "dgcColumn": "volume(column)",
                            "dgcUuid": "175abb62-4762-4762-ba92-4bdf6446a6fc",
                            "id": "9c3c95df-332a-4083-8229-acb9dea03251",
                        },
                    ],
                    "totalRecords": 9,
                    "mappedRecord": 9,
                }
            ],
            "totalRecords": 372,
            "mappedRecord": 1,
        },
        {
            "dgcSchema": "samples",
            "dqSchema": "samples",
            "dgcUuid": "018ce8b4-b9d2-7bec-91ab-a390d3dc4031",
            "id": "188cb9b9-8a28-460f-9c34-53dd52cfae0e",
            "tableMapping": [
                {
                    "dqTable": "sales_view_table",
                    "dgcTable": "sales_view_table",
                    "dgcUuid": "018ce8b5-2f8e-7037-90e1-f2905011d89e",
                    "id": "95f0b9bd-6345-4486-9889-836269dc3053",
                    "columnMapping": [
                        {
                            "dqColumn": "costcode",
                            "dgcColumn": "costcode",
                            "dgcUuid": "018ce8b5-2f8e-7037-90e1-f2905011d867",
                            "id": "6f9b1b53-c4e7-4733-af87-f30aa310765e",
                        },
                        {
                            "dqColumn": "firstname",
                            "dgcColumn": "firstname",
                            "dgcUuid": "018ce8b5-2f8e-7037-90e1-f2905011d8c8",
                            "id": "23526d9d-2edf-4658-8325-fc912a09cdc9",
                        },
                        {
                            "dqColumn": "lastname",
                            "dgcColumn": "lastname",
                            "dgcUuid": "018ce8b5-2f8e-7037-90e1-f2905011d8a6",
                            "id": "2d0fa6af-6a91-4b26-8668-1ff5e891b5ed",
                        },
                        {
                            "dqColumn": "tax",
                            "dgcColumn": "tax",
                            "dgcUuid": "018ce8b5-2f8e-7037-90e1-f2905011d89b",
                            "id": "6a2d3216-e861-409a-bda0-972182fc118c",
                        },
                        {
                            "dqColumn": "vendor",
                            "dgcColumn": "vendor",
                            "dgcUuid": "018ce8b5-2f8e-7037-90e1-f2905011d8a4",
                            "id": "86e4efa1-d205-4046-b550-60db42f5d5b7",
                        },
                    ],
                    "totalRecords": None,
                    "mappedRecord": None,
                }
            ],
            "totalRecords": None,
            "mappedRecord": None,
        },
    ],
}

SAMPLES_VIEW_SCHEMA = {
    "dqName": "APPROVED_POSTGRES_UP",
    "dgcName": "APPROVED_POSTGRES_UP>postgres",
    "dgcUuid": "d4ae34d5-171c-402b-b4df-51cb0cb030c7",
    "credentialId": "",
    "schemaMapping": [
        {
            "dgcSchema": "samples",
            "dqSchema": "samples",
            "dgcUuid": "018ce8b4-b9d2-7bec-91ab-a390d3dc4031",
            "tableMapping": [
                {
                    "dqTable": "sales_view_table",
                    "dgcTable": "sales_view_table",
                    "dgcUuid": "018ce8b5-2f8e-7037-90e1-f2905011d89e",
                    "columnMapping": [
                        {
                            "dqColumn": "vendor",
                            "dgcColumn": "vendor",
                            "dgcUuid": "018ce8b5-2f8e-7037-90e1-f2905011d8a4",
                        },
                        {
                            "dqColumn": "firstname",
                            "dgcColumn": "firstname",
                            "dgcUuid": "018ce8b5-2f8e-7037-90e1-f2905011d8c8",
                        },
                        {
                            "dqColumn": "lastname",
                            "dgcColumn": "lastname",
                            "dgcUuid": "018ce8b5-2f8e-7037-90e1-f2905011d8a6",
                        },
                        {
                            "dqColumn": "costcode",
                            "dgcColumn": "costcode",
                            "dgcUuid": "018ce8b5-2f8e-7037-90e1-f2905011d867",
                        },
                        {
                            "dqColumn": "tax",
                            "dgcColumn": "tax",
                            "dgcUuid": "018ce8b5-2f8e-7037-90e1-f2905011d89b",
                        },
                    ],
                }
            ],
        }
    ],
}
