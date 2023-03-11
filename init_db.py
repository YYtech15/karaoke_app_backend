import pandas as pd
from database.mysql_client import MySQLClient
from datetime import datetime

music_data = pd.read_csv("./database/init_data/music.csv").values.tolist()

client = MySQLClient()
mcc = None

try:
    mcc = client.get_connection()
    cursor = mcc.cursor()
    # レコードを挿入
    sql = "INSERT INTO `musics` (`title`, `singer`,`level`, `created_at`, `updated_at`) VALUES (%s, %s, %s, %s, %s)"
    records = [(row[0], row[1], row[2], datetime.now(), datetime.now())
               for row in music_data]
    cursor.executemany(sql, records)
    # コミットしてトランザクション実行
    mcc.commit()

except Exception as e:
    print(f"Error Occurred: {e}")

finally:
    if cursor is not None:
        cursor.close()
    if mcc is not None and mcc.is_connected():
        mcc.close()
