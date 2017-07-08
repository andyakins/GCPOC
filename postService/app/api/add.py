import pymysql.cursors
import os

def post(instring):
    connection = pymysql.connect(
                            host=os.environ['GCPOC_DB_HOST'],
                            user=os.environ['GCPOC_DB_USER'],
                            password=os.environ['GCPOC_DB_PASSWORD'],
                            db=os.environ['GCPOC_DB_DATABASE'],
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.Cursor)
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO gcpoc (instring) VALUES (%s)"
            cursor.execute(sql, (instring,))
        connection.commit()
    finally:
        connection.close()
    return instring,201
