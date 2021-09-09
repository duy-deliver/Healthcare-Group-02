# Healthcare-Group02
Disease diagnosis based on patients' symptom declaration and demographic characteristics

# Purpose

Building the data pipeline

# Detail of Work

1. Design data pipeline [here](./docs/design.png "Architecture")
2. Normalize and Denormalize data
3. Build data model
4. Ingest data from flat file
5. Extract and Load into Data warehouse
6. Load data onto Cloud with the transformation
7. Enrich data with different data sources
8. Visualize your data

# How to setup
1. Login into MSSQL and run [init_mssql.sql](./src/mssql/init_mssql.sql)
2. Authen SnowSQL and run [init_snowflake.sql](./src/mssql/init_snowfalke.sql)
3. Generate data: `python data-generator.py`


# Setup for Dev
in SQL SERVER Management Studio, follow [this tutorial](https://docs.microsoft.com/en-us/sql/integration-services/catalog/ssis-catalog?view=sql-server-ver15#to-create-the-ssisdb-catalog-in-sql-server-management-studio) to create a SSIS Catalog

SSIS Catalog:
- SSISDB
- Password: Pipeline1234