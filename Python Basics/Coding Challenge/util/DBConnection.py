from util.PropertyUtil import PropertyUtil
import pyodbc

import sys
sys.path.append(r"C:\Stack overflow\Python_foundational_training\Python Basics\Coding Challenge")

class DBConnection:
    @staticmethod
    def getConnection():
        connectionString = PropertyUtil.getPropertyString()
        return pyodbc.connect(connectionString)
    
