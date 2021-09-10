# Healthcare-Group02 - Modified by Group 9

# Purpose

**Business Problem**: \
Disease diagnosis based on patients' symptom declaration and demographic characteristics 

**Potential Solution**: \
Analyze Diseases’ likeliness by looking at Patients’ Gender, Location, Age, Symptoms, etc, and determining trends. \
To do so, we will need to build a data pipeline to perform ETL and present some findings with PowerBI.

# Detail of Work
0. Python script to generate data to [raw-folder](./resources/raw-folder)
1. Design data pipeline [here](./docs/architectural-design.png "Architecture")
2. Build data model
3. Ingest data from flat file (csv)
    - Build a SSIS solution to do migrate and stage data in MSSQL
    - Deploy packages to SSIS Catalog
    - Schedule jobs 
    - Error Handling and tracking
4. Extract and Load into Snowflake Data warehouse
    - Load Dim/Fact tables onto an "Update" database to perform SCD Type 2. Then only the latest data gets sent to the main database, and be viewed accordingly to their role.
    - Assign roles and permissions
    - For each role, a different view is used. E.g. Doctor role can only see the latest updates (Type 1), but DE role can see the history of updates.
5. Visualize your data
6. Extract data or update data again.

# How to setup
*Warning*: Before starting you need to have setup some required things other than Visual Studio, SSIS, SQL Server Management Studio, etc.
- py_requirements.txt: Create and setup environment for Python and call `pip install -r py_requirements.txt`
- ODBC for Snowflake. When you already have a Snowflake account

1. Login into MSSQL and run [init_mssql.sql](./src/mssql/init_mssql.sql)
2. Authen SnowSQL and run [init_snowflake.sql](./src/mssql/init_snowfalke.sql)
3. Generate data: `python data-generator.py`
4. In SSIS, remember that there are a few parameters.