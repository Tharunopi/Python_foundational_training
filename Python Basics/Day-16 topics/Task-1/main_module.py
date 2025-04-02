from entity.customer import customer
from entity.product import product
from entity.order import order 
import pyodbc

def one_way_command(conn, query, values):
    try:
        cur = conn.cursor()
        cur.execute(query, values)
        cur.commit()
        cur.close()
        print("Query Excuted")

    except pyodbc.Error as e:
        print(e)

def two_way_command(conn, query):
    try:
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        return result

    except pyodbc.Error as e:
        print(e)

class Menu:
    def __init__(self):
        try:
            self.conn = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};"
                "SERVER=THARUN\SQLEXPRESS;"
                "DATABASE=ecom;"
                "Trusted_Connection=yes;"
            )
        
        except pyodbc.Error as e:
            print(e)

    def Add_customer(self, cid, cname, address, mob):
        new_customer = customer(cid, cname, address, mob)
        values = new_customer.get_customer()
        query = "INSERT INTO customer VALUES (?, ?, ?, ?)"
        one_way_command(self.conn, query, values)
    
    def Add_product(self, pid, pname, desc, price):
        new_product = product(pid, pname, desc, price)
        values = new_product.get_product()
        query = "INSERT INTO product VALUES (?, ?, ?, ?)"
        one_way_command(self.conn, query, values)

    def Order_product(self, oid, date, cid, pid, qty):
        product_price = two_way_command(self.conn, f"SELECT price FROM product WHERE pid = {pid}")
        price = product_price[0][0]
        new_order = order(oid, date, cid, pid, qty, price)
        values = new_order.make_order()
        query = "INSERT INTO orders VALUES (?, ?, ?, ?, ?, ?, ?)"
        one_way_command(self.conn, query, values)

    def display_all_order(self):
        query = "SELECT * FROM orders"
        result = two_way_command(self.conn, query)
        print("------------------------------------------")
        for i in result:
            print(f"{i.oid}  {i.date}  {i.cid} {i.pid}  {i.qty}  {i.price}  {i.total_amount}")
        print("------------------------------------------")

m1 = Menu()
# m1.Add_customer(1, "Tharun", "KGM", "9360496526")
# m1.Add_product(1, "mobile", "working fine", 9666)
# m1.Order_product(1, "2025", 1, 1, 2)
m1.display_all_order()
