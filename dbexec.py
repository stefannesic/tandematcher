"""
Inspired by this tutorial:

https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
"""
import mysql.connector
from mysql.connector import errorcode
import config
import create_log

# global variabel log file
logfile = open("tandematcher.log", "w");

# starts database connection
def connect_db():
    try:
        
        cnx = mysql.connector.connect(user=config.connection_id['user'],
                                      password=config.connection_id['password'],
                                      host=config.connection_id['host'],
                                      database=config.connection_id['database'])

        return cnx
    
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


# ends database connection
def disconnect_db(cnx):
    cnx.cursor().close()
    cnx.close()
    
# generates a new id from the database
def getid(table):
    # filters table parameter
    if (table == 'binomes'):
        statement = "SELECT MAX(id)+1 AS newid FROM binomes"
    elif (table == 'filiere_f'):
        statement = "SELECT MAX(id)+1 AS newid FROM filiere_f"
    elif (table == 'filiere_p'):
        statement = "SELECT MAX(id)+1 AS newid FROM filiere_p"
    elif (table == 'filieres'):
        statement = "SELECT MAX(id)+1 AS newid FROM filieres"
    elif (table == 'filleuls'):
        statement = "SELECT MAX(id)+1 AS newid FROM filleuls"
    elif (table == 'langues'):
        statement = "SELECT MAX(id)+1 AS newid FROM langues"
    elif (table == 'langues_p'):
        statement = "SELECT MAX(id)+1 AS newid FROM langues_p"
    elif (table == 'loisirs'):
        statement = "SELECT MAX(id)+1 AS newid FROM loisirs"
    elif (table == 'loisirs_f'):
        statement = "SELECT MAX(id)+1 AS newid FROM loisirs_f"
    elif (table == 'loisirs_p'):
        statement = "SELECT MAX(id)+1 AS newid FROM loisirs_p"
    elif (table == 'parrains'):
        statement = "SELECT MAX(id)+1 AS newid FROM parrains"
    elif (table == 'pays'):
        statement = "SELECT MAX(id)+1 AS newid FROM pays"
    elif (table == 'universites'):
        statement = "SELECT MAX(id)+1 AS newid FROM universites"
    elif (table == 'universites_f'):
        statement = "SELECT MAX(id)+1 AS newid FROM universites_f"
    elif (table == 'universites_p'):
        statement = "SELECT MAX(id)+1 AS newid FROM universites_p"
    else:
         create_log.add_err_msg(300,"getid",
                                "Table %s n'existe pas" % (table))
         return;
        
         

    tableID = 0
    
    cnx = connect_db()
    cursor = cnx.cursor()

    cursor.execute(statement)
    
    for newid in cursor:
        if (newid != (None,)):
            tableID =  newid[0]
    

    disconnect_db(cnx)

    return tableID



    
    
    
    
