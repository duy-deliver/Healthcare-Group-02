CREATE OR REPLACE TABLE PIPELINE_GROUP02.DATAWAREHOUSE_DIAGNOSIS.Dim_Disease(
	Disease_iD varchar(2) NOT NULL,
	Disease_name varchar(20) NOT NULL,
	Blood_pressure_mmHg varchar(10) NULL,
	Blood_sugar_mgdL varchar(10) NULL
  );


CREATE OR REPLACE TABLE PIPELINE_GROUP02.DATAWAREHOUSE_DIAGNOSIS.Dim_Insurance(
	Insurance_iD varchar(10) NOT NULL,
	Insurance_cover_amount int NULL,
	Insurance_type varchar(3) NULL,
	Insurance_expired datetime NULL
  );
  
  
CREATE OR REPLACE TABLE PIPELINE_GROUP02.DATAWAREHOUSE_DIAGNOSIS.Dim_Medical(
    Medical_iD varchar(10) NOT NULL,
	Patient_iD varchar(10) NULL,
	Appointment_date datetime NULL
  );
  
  
CREATE OR REPLACE TABLE PIPELINE_GROUP02.DATAWAREHOUSE_DIAGNOSIS.Dim_MedicalDetail(
	Medical_iD varchar(10) NOT NULL,
	Symptom_iD varchar(10) NULL,
	Allergies_flag int NULL
  );
  
  
CREATE OR REPLACE TABLE PIPELINE_GROUP02.DATAWAREHOUSE_DIAGNOSIS.Dim_Patient(
	Patient_iD varchar(10) NOT NULL,
	Insurance_iD varchar(10) NULL,
	Patient_name varchar(50) NULL,
	Patient_gender varchar(6) NULL,
	Patient_age int NULL,
	Patient_bloodtype varchar(2) NULL,
	Patient_weight_kg int NULL,
	History_covid int NULL,
	Blood_pressure_mmHG int NULL,
	Blood_sugar_mgdL int NULL,
	Patient_zip int NULL,
	Patient_state varchar(30) NULL
  );
  

CREATE OR REPLACE TABLE PIPELINE_GROUP02.DATAWAREHOUSE_DIAGNOSIS.Dim_Symptom(
	Symptom_iD varchar(10) NOT NULL,
	Disease_iD varchar(2) NULL,
	Symptom_name varchar(50) NULL,
	Symptom_stage int NULL
  );
  
  
CREATE OR REPLACE TABLE PIPELINE_GROUP02.DATAWAREHOUSE_DIAGNOSIS.Fact_Diagnosis (
   Medical_iD varchar(10) NULL,
   Patient_iD varchar(10) NOT NULL,
   Symptom_iD varchar(10) NULL,
   Appointment_date datetime NULL,
   Patient_age int NULL,
   Patient_weight_kg int NULL,
   Patient_bloodtype varchar(2) NULL,
   History_covid int NULL,
   Blood_pressure_mmHG int NULL,
   Blood_sugar_mgdL int NULL
 );

--Insert databsase into FACT DIAGNOSIS
--drop table "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS"."FACT_DIAGNOSIS" 

INSERT INTO "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS"."FACT_DIAGNOSIS" (Medical_iD,
   Patient_iD, Symptom_iD ,Appointment_date, Patient_age, Patient_weight_kg, Patient_bloodtype, History_covid,
   Blood_pressure_mmHG, Blood_sugar_mgdL )

select D.MEDICAL_ID, D.PATIENT_ID,DT. Symptom_iD, D.Appointment_date , P.Patient_age, P.Patient_weight_kg, P.Patient_bloodtype,
P.History_covid, P.Blood_pressure_mmHG, P.Blood_sugar_mgdL
from "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS"."DIM_MEDICAL" D
JOIN "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS"."DIM_MEDICALDETAIL" DT on D.Medical_id = DT.Medical_iD
JOIN "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS"."DIM_PATIENT" P on D.Patient_iD = P.Patient_iD
;
-------------------------------------
--CREATE SNOWPIPE ENDPOINT"PIPELINE_GROUP02"

--show stages in database "PIPELINE_GROUP02"
--show file formats in database "PIPELINE_GROUP02"

alter user HANK0720 set rsa_public_key = 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAxP20oUpVwtPYPuGnsyou
ySuD685+YMOUEQI583TSom5f4GBikCRGmrrF6oFMQjj74iYNULxGe2pYCnDOzPnF
VAZSt5uq+Mg70yopks+GSzVIkaXSYJIk0A2zC3VrTF6iS3ze8pwsF2sfludgI0um
kwcY+iTgnkNj000rm3LswMoN3Y/7/aUniDmB3OYHdUZkSi4/pIlrwhgBgxU1qwA/
uEYNJ27RB0J7VrIGVDuxjY/NDtkrEepuQqtv/o7zhtr4SnLC4EBGg9QhkehHRcJN
0rAkPzWFok9Q3JAGpG0JTuD3LBV08X5+CLGXQlSwiA+0/tqekuvRZZ9i/YpIAtJZ
mQIDAQAB'


CREATE or REPLACE table PIPELINE_GROUP02.DATAWAREHOUSE_DIAGNOSIS.Disease_Stagging
( Disease_ID string, Disease_Name string,Blood_Pressure_mmHg string ,Blood_Sugar_mgdL string );


CREATE STAGE "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS".SNOWPIPE;

create pipe "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS".mypipe
if not exists as copy into "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS".Disease_Stagging from @"PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS".SNOWPIPE 
file_format = CSV;

--drop STAGE "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS".SNOWPIPE;
--desc user HANK0720
--drop pipe "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS".mypipe

LIST @SNOWPIPE
SELECT * FROM  "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS".Disease_Stagging

select SYSTEM$PIPE_STATUS('"PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS".mypipe')

------------------------------TASK SCHEDULE
--set up context 
use role sysadmin;
use database "PIPELINE_GROUP02";
use schema "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS";
use warehouse compute_wh;


--GRANT TASK exucute to Account 
create role taskadmin;

--set the active role to ACCOUNTADMIN before granting the EXECUTE TASK privilege to the new role
use role accountadmin;

grant execute task on account to role taskadmin;

--set the active role to SECURITYADMIN to show that this role can grant a role to another role
use role securityadmin;

grant role taskadmin to role sysadmin;

//CDC ON STAGGING TALBE
// Append_only for insert statement
create stream disease_Stage on table "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS"."DISEASE_STAGGING"
append_only = true ;

create or replace task disease_merge
    warehouse = COMPUTE_WH
    schedule = '1 minutes'
    when system$stream_has_data('disease_Stage')
as
     merge into "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS"."DIM_DISEASE" pd
     using "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS"."DISEASE_STAGGING" stg
  on pd.DISEASE_ID = stg.DISEASE_ID
  when matched then
  update set pd.BLOOD_SUGAR_MGDL = stg.BLOOD_SUGAR_MGDL
  when not matched then
  insert (DISEASE_ID, DISEASE_NAME,BLOOD_PRESSURE_MMHG,BLOOD_SUGAR_MGDL)
   values (stg.DISEASE_ID, stg.DISEASE_NAME,stg.BLOOD_PRESSURE_MMHG,stg.BLOOD_SUGAR_MGDL);

alter task disease_merge suspend;

--Test Enviroment SQL 
--INSERT INTO PIPELINE_GROUP02.DATAWAREHOUSE_DIAGNOSIS.Disease_Stagging
--VALUES ('D5','HIV','<120','>160')

--delete from "PIPELINE_GROUP02"."DATAWAREHOUSE_DIAGNOSIS"."DISEASE_STAGGING" where DISEASE_ID = 'D5'


select *
  from table(information_schema.task_history())
  order by scheduled_time;
