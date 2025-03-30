PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SPECIAL_CHARS_CONNECTION = "APPROVED_SAPHANA_PUSHDOWN"
PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SPECIAL_CHARS_TABLE = (
    r"TEST.SPECIALCHAR_SALES_DATA_10_ROWS_NO_SEMICOLON::$/-@#%^&*?!{}~\+="
)
PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SPECIAL_CHARS_COLUMNS = "*"
PD_SAPH_EXPLORER_SCHEMA_PREVIEW_SPECIAL_CHARS_EXPECTED = [
  {
    "SALES_ID": {
      "INTEGER": 1
    },
    "TRANSACTION_DATE": {
      "DATE": "2022-01-03"
    },
    "TRANSACTION_TIME": {
      "VARCHAR": "8:00 AM"
    },
    "DAILY_ID": {
      "VARCHAR": "1"
    },
    "FIRST_NAME": {
      "VARCHAR": "Waly"
    },
    "LAST_NAME": {
      "VARCHAR": "Measor"
    },
    "EMAIL": {
      "VARCHAR": "wmeasoro@wordpress.org"
    },
    "VENDOR_TYPE": {
      "VARCHAR": "Electrician"
    },
    "COST": {
      "REAL": 1000.53
    },
    "COST_DESCRIPTION": {
      "VARCHAR": "General Electrical"
    },
    "COST_CODE": {
      "VARCHAR": "16-000"
    },
    "SALES_REP": {
      "VARCHAR": "Kal"
    },
    "SALE_STATE": {
      "VARCHAR": "DE"
    },
    "STATE_TAX": {
      "VARCHAR": "0.000"
    },
    "CRM_ID": {
      "VARCHAR": None
    },
    "LOST_COLUMN": {
      "VARCHAR": None
    },
    "TEMP": {
      "VARCHAR": None
    }
  },
  {
    "SALES_ID": {
      "INTEGER": 2
    },
    "TRANSACTION_DATE": {
      "DATE": "2022-01-03"
    },
    "TRANSACTION_TIME": {
      "VARCHAR": "8:01 AM"
    },
    "DAILY_ID": {
      "VARCHAR": "2"
    },
    "FIRST_NAME": {
      "VARCHAR": "Dani"
    },
    "LAST_NAME": {
      "VARCHAR": "Kinkead"
    },
    "EMAIL": {
      "VARCHAR": "dkinkeadce@sitemeter.com"
    },
    "VENDOR_TYPE": {
      "VARCHAR": "Engineer"
    },
    "COST": {
      "REAL": 8979.99
    },
    "COST_DESCRIPTION": {
      "VARCHAR": "Wood Fences and Gates"
    },
    "COST_CODE": {
      "VARCHAR": "02-825"
    },
    "SALES_REP": {
      "VARCHAR": "Sara"
    },
    "SALE_STATE": {
      "VARCHAR": "PA"
    },
    "STATE_TAX": {
      "VARCHAR": "0.085"
    },
    "CRM_ID": {
      "VARCHAR": None
    },
    "LOST_COLUMN": {
      "VARCHAR": None
    },
    "TEMP": {
      "VARCHAR": None
    }
  },
  {
    "SALES_ID": {
      "INTEGER": 3
    },
    "TRANSACTION_DATE": {
      "DATE": "2022-01-03"
    },
    "TRANSACTION_TIME": {
      "VARCHAR": "8:01 AM"
    },
    "DAILY_ID": {
      "VARCHAR": "3"
    },
    "FIRST_NAME": {
      "VARCHAR": "Ryan"
    },
    "LAST_NAME": {
      "VARCHAR": "Bleiman"
    },
    "EMAIL": {
      "VARCHAR": "rbleimancs@arstechnica.com"
    },
    "VENDOR_TYPE": {
      "VARCHAR": "Surveyor"
    },
    "COST": {
      "REAL": 2886.53
    },
    "COST_DESCRIPTION": {
      "VARCHAR": "General Electrical"
    },
    "COST_CODE": {
      "VARCHAR": "16-000"
    },
    "SALES_REP": {
      "VARCHAR": "Kal"
    },
    "SALE_STATE": {
      "VARCHAR": "NY"
    },
    "STATE_TAX": {
      "VARCHAR": "0.115"
    },
    "CRM_ID": {
      "VARCHAR": None
    },
    "LOST_COLUMN": {
      "VARCHAR": None
    },
    "TEMP": {
      "VARCHAR": None
    }
  },
  {
    "SALES_ID": {
      "INTEGER": 4
    },
    "TRANSACTION_DATE": {
      "DATE": "2022-01-03"
    },
    "TRANSACTION_TIME": {
      "VARCHAR": "8:01 AM"
    },
    "DAILY_ID": {
      "VARCHAR": "4"
    },
    "FIRST_NAME": {
      "VARCHAR": "Henry"
    },
    "LAST_NAME": {
      "VARCHAR": "Putton"
    },
    "EMAIL": {
      "VARCHAR": "hputtonqs@amazon.com"
    },
    "VENDOR_TYPE": {
      "VARCHAR": "Construction Worker"
    },
    "COST": {
      "REAL": 4607.17
    },
    "COST_DESCRIPTION": {
      "VARCHAR": "Transportation Control Instrumentation"
    },
    "COST_CODE": {
      "VARCHAR": "13-550"
    },
    "SALES_REP": {
      "VARCHAR": "John"
    },
    "SALE_STATE": {
      "VARCHAR": "NY"
    },
    "STATE_TAX": {
      "VARCHAR": "0.115"
    },
    "CRM_ID": {
      "VARCHAR": None
    },
    "LOST_COLUMN": {
      "VARCHAR": None
    },
    "TEMP": {
      "VARCHAR": None
    }
  },
  {
    "SALES_ID": {
      "INTEGER": 5
    },
    "TRANSACTION_DATE": {
      "DATE": "2022-01-03"
    },
    "TRANSACTION_TIME": {
      "VARCHAR": "8:02 AM"
    },
    "DAILY_ID": {
      "VARCHAR": "5"
    },
    "FIRST_NAME": {
      "VARCHAR": "Sterne"
    },
    "LAST_NAME": {
      "VARCHAR": "Telford"
    },
    "EMAIL": {
      "VARCHAR": "stelford5e@army.mil"
    },
    "VENDOR_TYPE": {
      "VARCHAR": "Construction Expeditor"
    },
    "COST": {
      "REAL": 1852.66
    },
    "COST_DESCRIPTION": {
      "VARCHAR": "Plumbing Fixtures and Equipment"
    },
    "COST_CODE": {
      "VARCHAR": "15-400"
    },
    "SALES_REP": {
      "VARCHAR": "Sara"
    },
    "SALE_STATE": {
      "VARCHAR": "DE"
    },
    "STATE_TAX": {
      "VARCHAR": "0.000"
    },
    "CRM_ID": {
      "VARCHAR": None
    },
    "LOST_COLUMN": {
      "VARCHAR": None
    },
    "TEMP": {
      "VARCHAR": None
    }
  },
  {
    "SALES_ID": {
      "INTEGER": 6
    },
    "TRANSACTION_DATE": {
      "DATE": "2022-01-03"
    },
    "TRANSACTION_TIME": {
      "VARCHAR": "8:02 AM"
    },
    "DAILY_ID": {
      "VARCHAR": "6"
    },
    "FIRST_NAME": {
      "VARCHAR": "Michelina"
    },
    "LAST_NAME": {
      "VARCHAR": "Rowat"
    },
    "EMAIL": {
      "VARCHAR": "mrowatek@baidu.com"
    },
    "VENDOR_TYPE": {
      "VARCHAR": "Construction Foreman"
    },
    "COST": {
      "REAL": 8010.6
    },
    "COST_DESCRIPTION": {
      "VARCHAR": "Site Amenities"
    },
    "COST_CODE": {
      "VARCHAR": "02-800"
    },
    "SALES_REP": {
      "VARCHAR": "Kal"
    },
    "SALE_STATE": {
      "VARCHAR": "NJ"
    },
    "STATE_TAX": {
      "VARCHAR": "0.090"
    },
    "CRM_ID": {
      "VARCHAR": None
    },
    "LOST_COLUMN": {
      "VARCHAR": None
    },
    "TEMP": {
      "VARCHAR": None
    }
  },
  {
    "SALES_ID": {
      "INTEGER": 7
    },
    "TRANSACTION_DATE": {
      "DATE": "2022-01-03"
    },
    "TRANSACTION_TIME": {
      "VARCHAR": "8:02 AM"
    },
    "DAILY_ID": {
      "VARCHAR": "7"
    },
    "FIRST_NAME": {
      "VARCHAR": "Evangelia"
    },
    "LAST_NAME": {
      "VARCHAR": "Epelett"
    },
    "EMAIL": {
      "VARCHAR": "eepelettla@yellowpages.com"
    },
    "VENDOR_TYPE": {
      "VARCHAR": "Project Manager"
    },
    "COST": {
      "REAL": 3534.56
    },
    "COST_DESCRIPTION": {
      "VARCHAR": "Retaining Walls"
    },
    "COST_CODE": {
      "VARCHAR": "02-830"
    },
    "SALES_REP": {
      "VARCHAR": "John"
    },
    "SALE_STATE": {
      "VARCHAR": "NY"
    },
    "STATE_TAX": {
      "VARCHAR": "0.115"
    },
    "CRM_ID": {
      "VARCHAR": None
    },
    "LOST_COLUMN": {
      "VARCHAR": None
    },
    "TEMP": {
      "VARCHAR": None
    }
  },
  {
    "SALES_ID": {
      "INTEGER": 8
    },
    "TRANSACTION_DATE": {
      "DATE": "2022-01-03"
    },
    "TRANSACTION_TIME": {
      "VARCHAR": "8:02 AM"
    },
    "DAILY_ID": {
      "VARCHAR": "8"
    },
    "FIRST_NAME": {
      "VARCHAR": "Myriam"
    },
    "LAST_NAME": {
      "VARCHAR": "Buesnel"
    },
    "EMAIL": {
      "VARCHAR": "mbuesnelox@fotki.com"
    },
    "VENDOR_TYPE": {
      "VARCHAR": "Electrician"
    },
    "COST": {
      "REAL": 6380.28
    },
    "COST_DESCRIPTION": {
      "VARCHAR": "General Landscaping"
    },
    "COST_CODE": {
      "VARCHAR": "02-900"
    },
    "SALES_REP": {
      "VARCHAR": "Sara"
    },
    "SALE_STATE": {
      "VARCHAR": "NY"
    },
    "STATE_TAX": {
      "VARCHAR": "0.115"
    },
    "CRM_ID": {
      "VARCHAR": None
    },
    "LOST_COLUMN": {
      "VARCHAR": None
    },
    "TEMP": {
      "VARCHAR": None
    }
  },
  {
    "SALES_ID": {
      "INTEGER": 9
    },
    "TRANSACTION_DATE": {
      "DATE": "2022-01-03"
    },
    "TRANSACTION_TIME": {
      "VARCHAR": "8:04 AM"
    },
    "DAILY_ID": {
      "VARCHAR": "9"
    },
    "FIRST_NAME": {
      "VARCHAR": "Nikki"
    },
    "LAST_NAME": {
      "VARCHAR": "Chatres"
    },
    "EMAIL": {
      "VARCHAR": "nchatres8l@epa.gov"
    },
    "VENDOR_TYPE": {
      "VARCHAR": "Construction Worker"
    },
    "COST": {
      "REAL": 7968.29
    },
    "COST_DESCRIPTION": {
      "VARCHAR": "General Electrical"
    },
    "COST_CODE": {
      "VARCHAR": "16-000"
    },
    "SALES_REP": {
      "VARCHAR": "Kal"
    },
    "SALE_STATE": {
      "VARCHAR": "NJ"
    },
    "STATE_TAX": {
      "VARCHAR": "0.090"
    },
    "CRM_ID": {
      "VARCHAR": None
    },
    "LOST_COLUMN": {
      "VARCHAR": None
    },
    "TEMP": {
      "VARCHAR": None
    }
  },
  {
    "SALES_ID": {
      "INTEGER": 10
    },
    "TRANSACTION_DATE": {
      "DATE": "2022-01-03"
    },
    "TRANSACTION_TIME": {
      "VARCHAR": "8:04 AM"
    },
    "DAILY_ID": {
      "VARCHAR": "A"
    },
    "FIRST_NAME": {
      "VARCHAR": "Guido"
    },
    "LAST_NAME": {
      "VARCHAR": "Bricket"
    },
    "EMAIL": {
      "VARCHAR": "gbricketc3@digg.com"
    },
    "VENDOR_TYPE": {
      "VARCHAR": "Construction Worker"
    },
    "COST": {
      "REAL": 2279.2
    },
    "COST_DESCRIPTION": {
      "VARCHAR": "Masonry Assemblies"
    },
    "COST_CODE": {
      "VARCHAR": "04-800"
    },
    "SALES_REP": {
      "VARCHAR": "John"
    },
    "SALE_STATE": {
      "VARCHAR": "CT"
    },
    "STATE_TAX": {
      "VARCHAR": "0.110"
    },
    "CRM_ID": {
      "VARCHAR": None
    },
    "LOST_COLUMN": {
      "VARCHAR": None
    },
    "TEMP": {
      "VARCHAR": None
    }
  }
]
