driver = 'ODBC Driver 17 for SQL Server'
server = 'THARUN\SQLEXPRESS'
database = 'demo_assignment'
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