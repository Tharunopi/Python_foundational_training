from dao.IOrderManagementRepository import IOrderManagementRepository

from util.DBConnection import DBConnection

class OrderProcesor(IOrderManagementRepository):
    def __init__(self):
        self.conn = DBConnection.getConnection()

    def createOrder(self, user, listofProducts):
        try:
            cur = self.conn.cursor()
            userId = user.userId

            query = """INSERT INTO Orders(userId, listOfProducts, amount)
                    VALUES (?, ?, ?)"""
            
            values = (userId, listofProducts, None)

            cur.execute(query, values)
            self.conn.commit()
            cur.close()
            return True

        except Exception as e:
            print(f"Error: {e}")

    def cancelOrder(self, userId, orderId):
        try:
            cur = self.conn.cursor()
            query_1 = "SELECT userId FROM Users"
            cur.execute(query_1)
            users = cur.fetchall()
            if not any(userId in i for i in users):
                return False

            query_3 = "SELECT orderId FROM Orders"
            cur.execute(query_3)
            orders = cur.fetchall()
            if not any(orderId in i for i in orders):
                return False
           
            query_2 = f"DELETE FROM Orders WHERE orderId = {orderId}"
            cur.execute(query_2)
            self.conn.commit()
            cur.close
            return True

        except Exception as e:
            print(f"Error : {e}")

    def createProduct(self, user, product):
        try:
            cur = self.conn.cursor()
            userId = user.userId
            query_1 = "SELECT userId, role FROM Users"
            cur.execute(query_1)
            usersList = cur.fetchall()
            if not any(i.userId == userId and i.role == 'Admin' for i in usersList):
                return False
            
            query_2 = """INSERT INTO Products
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            if product.__class__.__name__ == 'Electronics':
                values = (product.productName, product.description, product.price, product.quantityInStock, product.type, product.brand, product.warrantyPeriod, None, None)
            else:
                values = (product.productName, product.description, product.price, product.quantityInStock, product.type, None, None, product.size, product.color)
            cur.execute(query_2, values)
            self.conn.commit()
            cur.close()
            return True
        
        except Exception as e:
            print(f"Error: {e}")

    def createUser(self, user):
        try:
            cur = self.conn.cursor()
            query = """INSERT INTO Users(username, password, role) 
                    VALUES (?, ?, ?)"""
            values = (user.username, user.password, user.role)

            cur.execute(query, values)
            self.conn.commit()
            cur.close()
            return True
        
        except Exception as e:
            print(f"Error: {e}")

    def getAllProducts(self):
        try:
            cur = self.conn.cursor() 
            query = "SELECT * FROM Products"
            cur.execute(query)
            productList = cur.fetchall()
            cur.close()
            return productList
        
        except Exception as e:
            print(f"Error: {e}")

    def getOrderByUser(self, user):
        try:
            cur = self.conn.cursor()
            userId = user.userId
            query = f"SELECT listOfProducts FROM Orders WHERE userId = {userId}"
            cur.execute(query)
            listOfProducts = cur.fetchall()
            return listOfProducts
        
        except Exception as e:
            print(f"Error: {e}")