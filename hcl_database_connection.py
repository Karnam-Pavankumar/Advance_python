import sys,os
import mysql.connector

class mysqlDatabaseConnection:
 try:
    def connect(self,host,username,passwd,database):
        self.host=host
        self.username=username
        self.passwd=passwd
        self.database=database
        self.connection=mysql.connector.connect(host=self.host,user=self.username,
                                                password=self.passwd,database=self.database)
        self.cursor=self.connection.cursor()
 except Exception as e:
     print(e)
