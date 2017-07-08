import pymysql.cursors
import os

def search() -> list:
    connection = pymysql.connect(
                            host=os.environ['GCPOC_DB_HOST'],
                            user=os.environ['GCPOC_DB_USER'],
                            password=os.environ['GCPOC_DB_PASSWORD'],
                            db=os.environ['GCPOC_DB_DATABASE'],
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.Cursor)
    try:
        with connection.cursor() as cursor:
            sql = "SELECT instring from gcpoc"
            cursor.execute(sql)
            result = [item[0] for item in cursor.fetchall()]
            print(result)
    except:
        return None,500
    finally:
        connection.close

    return result,200
