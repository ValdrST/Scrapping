import os
import mysql.connector
#from dotenv import load_dotenv


class BaseController(object):
    def __init__(self):
        #load_dotenv()
        self.conn = mysql.connector.connect(
            host=os.getenv('HOST_DB'),
            user=os.getenv('USER_DB'),
            password=os.getenv('PASS_DB'),
            database=os.getenv('DATABASE_DB')
        )
    
    def insertData(self, data):
        cur = self.conn.cursor(prepared=True)



    
    def update():
        pass

    def delete():
        pass

    def select():
        pass
    
