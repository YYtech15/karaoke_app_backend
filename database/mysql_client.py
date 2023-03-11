import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

user = os.getenv('DB_USER', 'root')
password = os.getenv('DB_PASSWORD', '')
host = os.getenv('DB_HOST', 'localhost')
port = os.getenv('DB_PORT', '3306')
database = os.getenv('DB_NAME')

auth_plugin = 'mysql_native_password'

class MySQLClient():

    def __init__(self):        
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.auth_plugin = auth_plugin

    def get_init_connection(self):
        return mysql.connector.connect(
                                        user=self.user,
                                        password=self.password,
                                        host=self.host,
                                        port=self.port,
                                        auth_plugin=self.auth_plugin
                                        )
    
    def get_connection(self):
        return mysql.connector.connect(
                                        user=self.user,
                                        password=self.password,
                                        host=self.host,
                                        port=self.port,
                                        database=database,
                                        auth_plugin=self.auth_plugin
                                        )