import pymysql.cursors
import os
from google.cloud import error_reporting
from google.cloud import logging

def search() -> list:
    errorLog = error_reporting.Client(project='gcpoc-173120',
                                 service="GCPOCGetService",
                                 version="1.0.0")
    logClient = logging.Client()
    logger = logClient.logger('GCPOCGetLog')

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
            logger.log_text("Found %d items in database" % len(result))
    except:
        errorLog.report_exception()
        return None,500
    finally:
        connection.close

    return result,200
