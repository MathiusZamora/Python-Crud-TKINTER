class Lab:
    def __init__(self, name, address, phone, email, status, id):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.status = status
        self.id = id

    def __str__(self):
        return self.name
    
class Supplier:
    def __init__(self, name, address, phone, email, status, id):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email
        self.status = status
        self.id = id

    def __str__(self):
        return self.name
    
class Item:
    def __init__(self, name, labs_id, suppliers_id, price, category, expiration_date, description, status, id):
        self.name = name
        self.labs_id = labs_id
        self.suppliers_id = suppliers_id
        self.price = price
        self.category = category
        self.expiration_date = expiration_date
        self.description = description
        self.status = status
        self.id = id
    
    def get_name(self):
        return self.name
    
    def get_lab(self):
        return self.lab.name
    
    def get_supplier(self):
        return self.supplier.name
    
    def get_price(self):
        return self.price
    
    def get_status(self):
        return self.status
    
    def set_status(self, status):
        self.status = status

    
