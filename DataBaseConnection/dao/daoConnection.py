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
        query = """
        SELECT
            LPAD('ID', 3, ' ') AS ID,
            LPAD('Nombre del Laboratorio', 20, ' ') AS Nombre_del_Laboratorio,
            LPAD('Dirección', 20, ' ') AS Dirección,
            LPAD('Teléfono', 15, ' ') AS Teléfono,
            LPAD('Correo Electrónico', 25, ' ') AS Correo_Electrónico,
            LPAD('Estado', 6, ' ') AS Estado
        UNION ALL
        SELECT
            LPAD(id, 3, ' ') AS ID,
            LPAD(name, 20, ' ') AS Nombre_del_Laboratorio,
            LPAD(address, 20, ' ') AS Dirección,
            LPAD(phone, 15, ' ') AS Teléfono,
            LPAD(email, 25, ' ') AS Correo_Electrónico,
            LPAD(status, 6, ' ') AS Estado
        FROM labs;
        """
        return self.connection.execute_read_query(query, ())
    
    def get_by_name(self, name):
        query = """
        SELECT
            LPAD('ID', 10, ' ') AS ID,
            LPAD('Nombre del Laboratorio', 25, ' ') AS Nombre_del_Laboratorio,
            LPAD('Dirección', 34, ' ') AS Dirección,
            LPAD('Teléfono', 20, ' ') AS Teléfono,
            LPAD('Correo Electrónico', 30, ' ') AS Correo_Electrónico,
            LPAD('Estado', 10, ' ') AS Estado
        UNION ALL
        SELECT
            LPAD(id, 10, ' ') AS ID,
            LPAD(name, 25, ' ') AS Nombre_del_Laboratorio,
            LPAD(address, 34, ' ') AS Dirección,
            LPAD(phone, 20, ' ') AS Teléfono,
            LPAD(email, 30, ' ') AS Correo_Electrónico,
            LPAD(status, 10, ' ') AS Estado
        FROM labs
        WHERE name = %s;
        """
        return self.connection.execute_read_query(query, (name,))
    
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
        query = """
        SELECT
            LPAD('ID', 3, ' ') AS ID,
            LPAD('Nombre del Proveedor', 20, ' ') AS Nombre_del_Proveedor,
            LPAD('Dirección', 20, ' ') AS Dirección,
            LPAD('Teléfono', 15, ' ') AS Teléfono,
            LPAD('Correo Electrónico', 25, ' ') AS Correo_Electrónico,
            LPAD('Estado', 6, ' ') AS Estado
        UNION ALL
        SELECT
            LPAD(id, 3, ' ') AS ID,
            LPAD(name, 20, ' ') AS Nombre_del_Proveedor,
            LPAD(address, 20, ' ') AS Dirección,
            LPAD(phone, 15, ' ') AS Teléfono,
            LPAD(email, 25, ' ') AS Correo_Electrónico,
            LPAD(status, 6, ' ') AS Estado
        FROM suppliers;
        """
        return self.connection.execute_read_query(query, ())
    
    def get_by_name(self, name):
        query = """
        SELECT
            LPAD('ID', 10, ' ') AS ID,
            LPAD('Nombre del Proveedor', 25, ' ') AS Nombre_del_Proveedor,
            LPAD('Dirección', 34, ' ') AS Dirección,
            LPAD('Teléfono', 20, ' ') AS Teléfono,
            LPAD('Correo Electrónico', 30, ' ') AS Correo_Electrónico,
            LPAD('Estado', 10, ' ') AS Estado
        UNION ALL
        SELECT
            LPAD(id, 10, ' ') AS ID,
            LPAD(name, 25, ' ') AS Nombre_del_Proveedor,
            LPAD(address, 34, ' ') AS Dirección,
            LPAD(phone, 20, ' ') AS Teléfono,
            LPAD(email, 30, ' ') AS Correo_Electrónico,
            LPAD(status, 10, ' ') AS Estado
        FROM suppliers
        WHERE name = %s;
        """
        return self.connection.execute_read_query(query, (name,))
    


    def insert(self, supplier):
        query = 'INSERT INTO suppliers (name, address, phone, email, status) VALUES (%s, %s, %s, %s, %s)'
        return self.connection.execute_query(query, (supplier.name, supplier.address, supplier.phone, supplier.email, supplier.status))
    
    def update(self, supplier):
        query = 'UPDATE suppliers SET name = %s, address = %s, phone = %s, email = %s, status = %s WHERE id = %s'
        return self.connection.execute_query(query, (supplier.name, supplier.address, supplier.phone, supplier.email, supplier.status, supplier.id))
    
    def delete(self, id):
        query = 'DELETE FROM suppliers WHERE id = %s'
        return self.connection.execute_query(query, (id,))
    


class DaoItem:
    def __init__(self, connection):
        self.connection = connection
    
    def get_all(self):
        query = """
        SELECT
            LPAD('ID', 3, ' ') AS ID,
            LPAD('Nombre del Item', 20, ' ') AS Nombre_del_Item,
            LPAD('Proveedor', 15, ' ') AS Proveedor,
            LPAD('Laboratorio', 15, ' ') AS Laboratorio,
            LPAD('Precio', 6, ' ') AS Precio,
            LPAD('Categoría', 10, ' ') AS Categoría,
            LPAD('Fecha de Expiración', 19, ' ') AS Fecha_de_Expiración,
            LPAD('Descripción', 15, ' ') AS Descripción,
            LPAD('Estado', 6, ' ') AS Estado
        UNION ALL
        SELECT
            LPAD(items.id, 3, ' ') AS ID,
            LPAD(items.name, 20, ' ') AS Nombre_del_Item,
            LPAD(suppliers.name, 15, ' ') AS Proveedor,
            LPAD(labs.name, 15, ' ') AS Laboratorio,
            LPAD(items.price, 6, ' ') AS Precio,
            LPAD(items.category, 10, ' ') AS Categoría,
            LPAD(items.expiration_date, 19, ' ') AS Fecha_de_Expiración,
            LPAD(items.description, 15, ' ') AS Descripción,
            LPAD(items.status, 6, ' ') AS Estado
        FROM items
        JOIN suppliers ON items.suppliers_id = suppliers.id
        JOIN labs ON items.labs_id = labs.id;
        """

        return self.connection.execute_read_query(query, ())




    def get_by_name(self, name):
        query = """
        SELECT
            LPAD('ID', 5, ' ') AS ID,
            LPAD('Nombre del Item', 20, ' ') AS Nombre_del_Item,
            LPAD('Proveedor', 15, ' ') AS Proveedor,
            LPAD('Laboratorio', 15, ' ') AS Laboratorio,
            LPAD('Precio', 6, ' ') AS Precio,
            LPAD('Categoría', 10, ' ') AS Categoría,
            LPAD('Fecha de Expiración', 19, ' ') AS Fecha_de_Expiración,
            LPAD('Descripción', 20, ' ') AS Descripción,
            LPAD('Estado', 6, ' ') AS Estado
        UNION ALL
        SELECT
            LPAD(items.id, 5, ' ') AS ID,
            LPAD(items.name, 20, ' ') AS Nombre_del_Item,
            LPAD(suppliers.name, 15, ' ') AS Proveedor,
            LPAD(labs.name, 15, ' ') AS Laboratorio,
            LPAD(items.price, 6, ' ') AS Precio,
            LPAD(items.category, 10, ' ') AS Categoría,
            LPAD(items.expiration_date, 19, ' ') AS Fecha_de_Expiración,
            LPAD(items.description, 20, ' ') AS Descripción,
            LPAD(items.status, 6, ' ') AS Estado
        FROM items
        JOIN suppliers ON items.suppliers_id = suppliers.id
        JOIN labs ON items.labs_id = labs.id
        WHERE items.name = %s;
        """
        return self.connection.execute_read_query(query, (name,))
    


    
    def insert(self, item):
        query = 'INSERT INTO items (name, labs_id, suppliers_id, price, category, expiration_date, description, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
        return self.connection.execute_query(query, (item.name, item.labs_id, item.suppliers_id, item.price, item.category, item.expiration_date, item.description, item.status))
    
    def update(self, item):
        query = 'UPDATE items SET name = %s, labs_id = %s, suppliers_id = %s, price = %s, category = %s, expiration_date = %s, description = %s, status = %s WHERE id = %s'
        return self.connection.execute_query(query, (item.name, item.labs_id, item.suppliers_id, item.price, item.category, item.expiration_date, item.description, item.status, item.id))
    
    def delete(self, id):
        query = 'DELETE FROM items WHERE id = %s'
        return self.connection.execute_query(query, (id,))
    

