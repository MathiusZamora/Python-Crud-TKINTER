import mysql.connector

class Connection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.cnx = None
        self.connect()
        
    def connect(self):
        self.cnx = mysql.connector.connect(user=self.user, password=self.password, host=self.host, database=self.database)

    def close(self):
        self.cnx.close()

    def execute_query(self, query, params):
        cursor = self.cnx.cursor()
        cursor.execute(query, params)
        self.cnx.commit()
        cursor.close()
        return cursor

    def execute_read_query(self, query, params):
        cursor = self.cnx.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        cursor.close()
        return result
    
class DaoLab:
    def __init__(self, connection):
        self.connection = connection
    
    def get_all(self):
        query = 'SELECT * FROM labs'
        return self.connection.execute_read_query(query, ())
    
    def get_by_id(self, id):
        query = 'SELECT * FROM labs WHERE id = %s'
        return self.connection.execute_read_query(query, (id,))
    
    def insert(self, lab):
        query = 'INSERT INTO labs (name, address, phone, email, status) VALUES (%s, %s, %s, %s, %s)'
        return self.connection.execute_query(query, (lab.name, lab.address, lab.phone, lab.email, lab.status))
    
    def update(self, lab):
        query = 'UPDATE labs SET name = %s, address = %s, phone = %s, email = %s, status = %s WHERE id = %s'
        return self.connection.execute_query(query, (lab.name, lab.address, lab.phone, lab.email, lab.status, lab.id))
    
    def delete(self, id):
        query = 'DELETE FROM labs WHERE id = %s'
        return self.connection.execute_query(query, (id,))
    

class DaoSupplier:
    def __init__(self, connection):
        self.connection = connection
    
    def get_all(self):
        query = 'SELECT * FROM suppliers'
        return self.connection.execute_read_query(query, ())
    
    def get_by_id(self, id):
        query = 'SELECT * FROM suppliers WHERE id = %s'
        return self.connection.execute_read_query(query, (id,))
    
    def insert(self, supplier):
        query = 'INSERT INTO suppliers (name, address, phone, email, status) VALUES (%s, %s, %s, %s, %s)'
        return self.connection.execute_query(query, (supplier.name, supplier.address, supplier.phone, supplier.email, supplier.status))
    
    def update(self, supplier):
        query = 'UPDATE suppliers SET name = %s, address = %s, phone = %s, email = %s, status = %s WHERE id = %s'
        return self.connection.execute_query(query, (supplier.name, supplier.address, supplier.phone, supplier.email, supplier.status, supplier.id))
    
    def delete(self, id):
        query = 'DELETE FROM suppliers WHERE id = %s'
        return self.connection.execute_query(query, (id,))
    


class DaoItems:
    def __init__(self, connection):
        self.connection = connection
    
    def get_all(self):
        query = 'SELECT * FROM items'
        return self.connection.execute_read_query(query, ())
    
    def get_by_id(self, id):
        query = 'SELECT * FROM items WHERE id = %s'
        return self.connection.execute_read_query(query, (id,))
    
    def insert(self, item):
        query = 'INSERT INTO items (name, labs_id, suppliers_id, price, category, expiration_date, description, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        return self.connection.execute_query(query, (item.name, item.labs_id, item.suppliers_id, item.price, item.category, item.expiration_date, item.description, item.satus))
    
    def update(self, item):
        query = 'UPDATE items SET name = %s, labs_id = %s, suppliers_id = %s, price = %s, category = %s, expiration_date = %s, description = %s, status = %s WHERE id = %s'
        return self.connection.execute_query(query, (item.name, item.labs_id, item.suppliers_id, item.price, item.category, item.expiration_date, item.description, item.satus, item.id))
    
    def delete(self, id):
        query = 'DELETE FROM items WHERE id = %s'
        return self.connection.execute_query(query, (id,))
    

