import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database 
    Return a pointer to the open connection"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn
    


if __name__ == '__main__':
    #open the SQLite database
    connection = create_connection("BDFournisseurs.db") 
    
    #execute a query
    cur = connection.cursor()
    cur.execute("SELECT * FROM ARTICLE")
    #print results
    results = cur.fetchall()
    for row in results:
        print(row)
