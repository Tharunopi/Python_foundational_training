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

    def one_way_command(self, query, values):
        cur = self.conn.cursor()

        try:
            cur.execute(query, values)
        except pyodbc.Error as e:
            print(e)

        cur.commit()
        cur.close()
        print("Query executed")
    
    def close(self):
        self.conn.close()
        

db = dbConnection()
query = "UPDATE anime set anime_mc = ? WHERE anime_id = ?"
values = ('shidra', 4)
db.one_way_command(query, values)
db.close()