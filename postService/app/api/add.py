import pymysql.cursors
import os
from google.cloud import error_reporting
from google.cloud import logging

def post(instring):
    errorLog = error_reporting.Client(project='gcpoc-173120',
                                 service="GCPOCGetService",
                                 version="1.0.0")
    logClient = logging.Client()
    logger = logClient.logger('GCPOCPostLog')

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
            logger.log_text("Added %s to database" % instring)
        connection.commit()
    except:
        errorLog.report_exception()
        return instring,500
    finally:
        connection.close()
    return instring,201
