import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

class SQLDataAccess:
    def __init__(self,timeout) -> None:
        self._commandTimeout = 180

    def get_connection(con_name):
        try:
            connect_str = os.getenv("CON_STR")
            conn = pyodbc.connect(connect_str)
            return conn
        except:
            raise 'NO Connecting string'
    
    
    
    
    
    
    

