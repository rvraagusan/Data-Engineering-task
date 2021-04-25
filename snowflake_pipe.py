import snowflake.connector as snow
from snowflake.connector.pandas_tools import write_pandas
from initial import load_file 
from author_data import create_table

dbPassword = ''

if dbPassword == '':
    import getpass
    dbPassword = getpass.getpass('Password: ')

conn = snow.connect(
    user='ragul',
    account='qs31224.ap-southeast-1',
    password=dbPassword,
    warehouse='COMPUTE_WH',
    database='DATA_ENG',
    schema='STAR_SCHEMA'
)

curs = conn.cursor()

author, course, subject, fact = create_table()
# course = load_file()

# write_pandas(conn, author, "AUTHOR_DIM")
# write_pandas(conn, course, "COURSE_DIM")
write_pandas(conn, subject, "SUBJECT_DIM")
# write_pandas(conn, fact, "FACT_SALES")
# curs.execute('select * from"WTRAINER"."PUBLIC"."SAMPLE"')
# print(curs.fetchone()[0])