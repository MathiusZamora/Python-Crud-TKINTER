import mysql.connector


class Lab:
    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="", database="pharmacydatabase")

    def __str__(self):
        datos=self.consulta_laboratorios()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_laboratorios(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM labs")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_laboratorio(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM labs WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_laboratorio(self,name, address, phone, email, status):
        cur = self.cnn.cursor()
        sql='''INSERT INTO labs (name, address, phone, email, status) 
        VALUES('{}', '{}', '{}', '{}', '{}')'''.format(name, address, phone, email, status)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_laboratorio(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM labs WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_laboratorio(self, Id, name, address, phone, email, status):
        cur = self.cnn.cursor()
        sql='''UPDATE labs SET name='{}', address='{}', phone='{}',
        email='{}', status='{}' WHERE Id={}'''.format(name, address, phone, email, status, Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n


class Supp:
    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="", database="pharmacydatabase")

    def __str__(self):
        datos=self.consulta_proveedores()        
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux
        
    def consulta_proveedores(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM suppliers")
        datos = cur.fetchall()
        cur.close()    
        return datos

    def buscar_proveedores(self, Id):
        cur = self.cnn.cursor()
        sql= "SELECT * FROM suppliers WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()    
        return datos
    
    def inserta_proveedores(self,name, address, phone, email, status):
        cur = self.cnn.cursor()
        sql='''INSERT INTO suppliers (name, address, phone, email, status) 
        VALUES('{}', '{}', '{}', '{}', '{}')'''.format(name, address, phone, email, status)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def elimina_proveedores(self,Id):
        cur = self.cnn.cursor()
        sql='''DELETE FROM suppliers WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modifica_proveedores(self, Id, name, address, phone, email, status):
        cur = self.cnn.cursor()
        sql='''UPDATE suppliers SET name='{}', address='{}', phone='{}',
        email='{}', status='{}' WHERE Id={}'''.format(name, address, phone, email, status, Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n


class Item:
    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="", database="pharmacydatabase")

    def __str__(self):
        datos = self.consulta_items()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_items(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM items")
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_item(self, Id):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM items WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos

    def inserta_item(self, name, labs_id, suppliers_id, price, category, expiration_date, description, status):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO items (name, labs_id, suppliers_id, price, category, expiration_date, description, status) 
                 VALUES('{}', {}, {}, {}, '{}', '{}', '{}', '{}')'''.format(
                 name, labs_id, suppliers_id, price, category, expiration_date, description, status)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def elimina_item(self, Id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM items WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def modifica_item(self, Id, name, labs_id, suppliers_id, price, category, expiration_date, description, status):
        cur = self.cnn.cursor()
        sql = '''UPDATE items SET name='{}', labs_id={}, suppliers_id={}, price={}, category='{}', 
                 expiration_date='{}', description='{}', status='{}' WHERE Id={}'''.format(
                 name, labs_id, suppliers_id, price, category, expiration_date, description, status, Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n