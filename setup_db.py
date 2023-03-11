import os
from dotenv import load_dotenv
from database.mysql_client import MySQLClient

load_dotenv()


client = MySQLClient()
mcc = None

try:
    mcc = client.get_init_connection()

    cursor = mcc.cursor()

    db_name = os.getenv('DB_NAME')

    cursor.execute(f"CREATE DATABASE {db_name}")

    cursor.execute("SHOW DATABASES")
    print(cursor.fetchall())

    cursor.close()

except Exception as e:
    print(f"Error Occurred: {e}")

finally:
    if mcc is not None and mcc.is_connected():
        mcc.close()
