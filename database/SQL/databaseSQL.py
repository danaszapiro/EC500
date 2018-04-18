# Python code to demonstrate table creation and 
# insertions with SQL
 
# importing module
import sqlite3

def initialize_database(): 
    # connecting to the database 
    connection = sqlite3.connect("twitter.db")
     
    # cursor 
    crsr = connection.cursor()
     
    # SQL command to create the twitterfeed table in the database
    sql_command1 = """CREATE TABLE IF NOT EXISTS twitterFeeds ( 
    handleId integer PRIMARY KEY, 
    twitterHandel text NOT NULL,  
    imageCount integer, 
    joining text NOT NULL);"""
     
    # execute the statement
    crsr.execute(sql_command1)
    
    # SQL command to create the labels table in the database
    sql_command2 = """CREATE TABLE IF NOT EXISTS labels ( 
    handleId integer NOT NULL,
    labelId SERIAL,
    keyword text NOT NULL,
    score integer NOT NULL,
    PRIMARY KEY (handleId , labelId),
    FOREIGN KEY (handleId) REFERENCES twitterFeeds (handleId)
        ON UPDATE CASCADE ON DELETE CASCADE);"""
     
    # execute the statement
    crsr.execute(sql_command2) 
     
    # Save the changes in the files.
    connection.commit()
    # close the connection
    connection.close()

def insertTwitterHandle(handle, imageCount, date):
    # connecting to the database 
    connection = sqlite3.connect("twitter.db")
     
    # cursor 
    crsr = connection.cursor()
        
    # SQL command to insert the data in the table
    crsr.execute("INSERT INTO twitterFeeds (handle, imageCount, date) VALUES (?, ?, ?)", (handle, imageCount, date))
    # Save the changes in the files.
    connection.commit()
    # close the connection
    connection.close()


def insertLabels(handleId, label, score):
    # connecting to the database 
    connection = sqlite3.connect("twitter.db")
    crsr = connection.cursor()
        
    # SQL command to insert the data in the table
    crsr.execute("INSERT INTO twitterFeeds (handleId, label, score) VALUES (?, ?, ?)", (handleId, label, score))
    # Save the changes in the files.
    connection.commit()
    # close the connection
    connection.close()
    
def findId(handle):

    # connecting to the database 
    connection = sqlite3.connect("twitter.db")
    crsr = connection.cursor()
        
    crsr.execute("SELECT handleId, handle FROM twitterFeeds ORDER BY handleId")
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == handle:
            id = row[0]
    cursor.close()
    return id

     