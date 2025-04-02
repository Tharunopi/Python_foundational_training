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

    def Order_product(self, oid, cid, pid, qty):
        product_price = two_way_command(self.conn, f"SELECT price FROM product WHERE pid = {pid}")
        price = product_price[0][0]
        new_order = order(oid, cid, pid, qty, price)
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

    def display_order_id(self):
        query = "SELECT TOP 1 oid FROM orders ORDER BY oid DESC"
        result = two_way_command(self.conn, query)
        print(f"Last order ID - {result[0][0]}")

    def display_customer_records(self):
        query = """SELECT c.cid, c.cname, sum(total_amount) AS sum_total FROM orders o
                INNER JOIN customer c
                ON c.cid = o.cid
                GROUP BY c.cid, c.cname"""
        result = two_way_command(self.conn, query)
        print("------------------------------")
        for i in result:
            print(f"{i.cid}  {i.cname}  {i.sum_total}")
        print("------------------------------")

m1 = Menu()
status = "Online"
operations = ["1. Add customer", "2. Add product", "3. Add order", "4. Display all order", "5. Display order ID", "6. Display customer details", "7. Exit"]
for i in operations:
    print(i)

while status == "Online":
    response = int(input("Enter operations to perform: "))

    if response == 1:
        m1.Add_customer(cid=int(input("Enter CID: ")), cname=input("Enter Name: "), address=input("Enter Location: "), mob=input("Enter number: "))
    elif response == 2:
        m1.Add_product(pid=int(input("Enter PID: ")), pname=input("Enter Product name: "), desc=input("Enter Description: "), price=int(input("Enter price: ")))
    elif response == 3:
        m1.Order_product(oid=int(input("Enter OrderID: ")), cid=int(input("Enter CustomerID: ")), pid=int(input("Enter ProductID: ")), qty=int(input("Enter Quantity: ")))
    elif response == 4:
        m1.display_all_order()
    elif response == 5:
        m1.display_order_id()
    elif response == 6:
        m1.display_customer_records()
    elif response == 7:
        status = "Offline"
        print("Logged Out!!")
    else:
        print("Invalid response!!")
        break