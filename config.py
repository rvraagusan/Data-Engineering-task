import snowflake.connector as sf 

sfAccount = "qs31224.ap-southeast-1"
sfUser = "ragul"
sfPassword=""
sfWarehouse= "COMPUTE_WH"
sfDatabase ="DATA_ENG"
sfSchema = "STAR_SCHEMA"
sfStage = "DATA_STAGE"

def create_snow_flake(sfAccount, sfUser, sfPassword, sfDatabase, sfSchema, sfStage, sfWarehouse):
    if sfPassword == "":
        import getpass
        sfPassword = getpass.getpass('Password: ')

    try:
        sfConnection =sf.connect(
            user= sfUser,
            account = sfAccount,
            password = sfPassword
        )

        sfq = sfConnection.cursor()

        sfq.execute('USE WAREHOUSE {0}'.format(sfWarehouse))
        sfq.execute('CREATE DATABASE IF NOT EXISTS {0}'.format(sfDatabase))
        sfq.execute('CREATE SCHEMA IF NOT EXISTS {0}.{1}'.format(sfDatabase, sfSchema))


        sfq.close()
        sfConnection.close()

        result = "Database Created "

    except:
        result= "Connection failed. Check it"
    
    print(result)

create_snow_flake(sfAccount, sfUser, sfPassword, sfDatabase, sfSchema, sfStage, sfWarehouse)
