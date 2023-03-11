# karaoke_app_backend

# setup command lists
1. pip install -r requirements.txt
2. create mysql user
   1. create user your_name@localhost identified with mysql_native_password by 'your_password';
   2. grant all on *.* to your_name@localhost;
3. create file .env
   1. DB_USER = your_name
   2. DB_PASSWORD = your_password
   3. DB_HOST = localhost
   4. DB_PORT = 3306
   5. DB_NAME = (ex)karaoke_API_development
4. python setup_db.py
5. pythom migrate_db.py
6. uvicorn main:app --host localhost
