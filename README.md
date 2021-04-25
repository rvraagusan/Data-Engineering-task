# Data-Engineering-task
this is a sample ETL pipeline task 


# installed package 
Pandas
snowflake-connector-python
snowflake-connector-python[pandas]

assumptions.
Course_data.json is a flat json files import pandas and covert json file to a dataframe it easy to upload the data into snowflake.
   
Create a python connectivity with snowflake and upload data files into a table and check data have duplicate or not and snowflake connectivity.

Star schema diagram












Sql Query 
Create this star schema tables 

CREATE OR REPLACE TABLE AUTHOR_DIM (
  AUTHOR_ID int,
  FIRST_NAME string,
  LAST_NAME string,
  AUTHOR_CODE string
);



CREATE OR REPLACE TABLE COURSE_DIM (
  COURSE_ID int,
  COURSE_NAME string,
  LEVELS string,
  PRICE float,
  CONTENT_DURATION float
);

CREATE OR REPLACE TABLE SUBJECT_DIM (
  SUBJECT_ID int,
  SUBJECT string
);

CREATE OR REPLACE TABLE FACT_SALES (
  AUTHOR_ID int,
  COURSE_ID int,
  SUBJECT_ID int,
  IS_PAID boolean,
  NUM_SUBCRIBERS int,
  NUM_REVIEWS int,
  NUM_LECTURES int,
  PUBLISHED_TIMESTAMPS date
); 


