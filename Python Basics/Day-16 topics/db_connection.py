import pyodbc

class dbConnection:
    def __init__(self):
        try:
            self.conn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "SERVER=THARUN\SQLEXPRESS;"
                "DATABASE=demo_assignment;"
                "Trusted_Connection=yes;"
            )
        except pyodbc.Error as e:
            print("Error in connection: ", e)

    def one_way_command(self, query):
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            cur.commit()
            cur.close()
            print("Query executed")

        except pyodbc.Error as e:
            print(e)

    def two_way_command(self, query):
        try:
            cur = self.conn.cursor()
            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            self.show(result)
            return result
        
        except pyodbc.Error as e:
            print(e)

    def show(self, result):
        if len(result) > 1:
            for i in result:
                print(i)

    def close(self):
        self.conn.close()
        

db = dbConnection()
query = input("Enter query: ")
lis = db.two_way_command(query)
db.close()