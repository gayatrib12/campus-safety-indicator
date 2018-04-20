import cx_Oracle
from backend import db_cred;

def db_cursor():
    connection = cursor = None
    try:
        connection = cx_Oracle.connect(db_cred.username, db_cred.password, f"{db_cred.host}/{db_cred.sid}")
        connection.current_schema = 'asj'
        cursor = connection.cursor()
        return cursor
    except Exception as e:
        print('Error occurred')
        raise e
    # finally:
    #     if connection:
    #         connection.close()
    #     if cursor:
    #         cursor.close()

cursor = db_cursor()