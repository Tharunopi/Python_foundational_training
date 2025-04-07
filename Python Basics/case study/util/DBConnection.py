from util.PropertyUtil import PropertyUtil
import pyodbc

class DBConnection:
    @staticmethod
    def getConnection():
        connectionString = PropertyUtil.getPropertyString()
        return pyodbc.connect(connectionString)
    
    