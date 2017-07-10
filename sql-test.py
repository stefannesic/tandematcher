"""
Inspired by this tutorial:

https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
"""
from datetime import date, datetime, timedelta
import mysql.connector
from mysql.connector import errorcode
import config
from create_log import add_err_msg

# global variabel log file
logfile = open("tandematcher.log", "w");

def connect_db():
    try:
        
        cnx = mysql.connector.connect(user=connection_id.user,
                                      password=connection_id.password,
                                      host=connection_id.host,
                                      database=connection_id.database)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            err_msg = "Something is wrong with your user name or password"
            add_err_msg(1, "connect_db", err_msg)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            err_msg = "Database does not exist"
            add_err_msg(2, "connect_db", err_msg)
        else:
            err_msg = "Unidentified error"
            add_err_msg(3, "connect_db", err_msg)

    cursor = cnx.cursor();
    return cursor

def disconnect_db(cursor):
    cursor.close()
    cnx.close()
    
