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
        cur.execute('''
            INSERT INTO 
            paises(
                Flag,
                Area,
                Population,
                Iso,
                Country,
                Capital,
                Continent,
                Tld,
                Currency_code,
                Currency_name,
                Phone,
                Postal_code_format,
                Postal_Code_regex,
                Languages,
                Neighbours) VALUES (%s,%s,%s,%s,%s, %s,%s,%s,%s,%s, %s,%s,%s,%s,%s)''',(
                    data['Flag'],
                    data['Area'],
                    data['Population'],
                    data['Iso'],
                    data['Country (District)'],
                    data['Capital'],
                    data['Continent'],
                    data['Tld'],
                    data['Currency Code'],
                    data['Currency Name'],
                    data['Phone'],
                    data['Postal Code Format'],
                    data['Postal Code Regex'],
                    data['Languages'],
                    data['Neighbours']))

    def update():
        pass

    
