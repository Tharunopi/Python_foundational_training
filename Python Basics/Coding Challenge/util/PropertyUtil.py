import sys
sys.path.append(r"C:\Stack overflow\Python_foundational_training\Python Basics\Coding Challenge")

driver = 'ODBC Driver 17 for SQL Server'
server = 'THARUN\SQLEXPRESS'
database = 'OrderManagementSystem'
trusted_connection = 'yes'

class PropertyUtil:
    @staticmethod
    def getPropertyString():
        connectionString = (
            f'DRIVER={driver};'
            f'SERVER={server};'
            f'DATABASE={database};'
            f'Trusted_Connection={trusted_connection};'
        )
        return connectionString