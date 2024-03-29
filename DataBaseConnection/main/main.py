import os
import sys
sys.path.append(r"C:/Users/MathiusZ/Desktop/ExamenFinal/DataBaseConnection")
from dao import daoConnection
from models import clases as c


os.system('cls')
conex = daoConnection.Connection("localhost", "root", "", "pharmacydatabase")
conex.connect()


def addLab():
    name = input("Nombre del Laboratorio: ")
    address = input("Direccion del Laboratorio: ")
    phone = input("Telefono del Laboratorio: ")
    email = input("Email del Laboratorio: ")

    laboratorio = c.Lab(name, address, phone, email, 1, None)
    daoLab = daoConnection.DaoLab(conex)
    daoLab.insert(laboratorio)
    

def editLab():
    id = int(input("ID del laboratorio a editar: "))
    newName = input("Nuevo nombre del Laboratorio: ")
    newAddress = input("Nueva direccion del Laboratorio: ")
    newPhone = input("Nuevo telefono del Laboratorio: ")
    newEmail = input("Nuevo email del Laboratorio: ")


    daoLab = daoConnection.DaoLab(conex)
    laboratorio = c.Lab(newName, newAddress, newPhone, newEmail, 1, id)
    daoLab.update(laboratorio)


def showLab():
    daoLab = daoConnection.DaoLab(conex)
    labs = daoLab.get_all()
    for lab in labs:
        print(lab)


def deleteLab():
    id = int(input("ID del Laboratorio a eliminar: "))
    daoLab = daoConnection.DaoLab(conex)
    daoLab.delete(id)


def searchLab():
    id = int(input("ID del laboratorio buscar: "))
    daoLab = daoConnection.DaoLab(conex)
    labs = daoLab.get_by_id(id)
    print(labs)



def MenuLab():
    print("1. Ingresar Laboratorio")
    print("2. Editar Laboratorio")
    print("3. Mostrar Laboratorio")
    print("4. Eliminar Laboratorio")
    print("5. Buscar Laboratorio")
    print("6. Salir")

def mainLab():
    opcion = 0

    while(opcion != 6): 
        MenuLab()
        opcion = int(input("Ingresa una opcion: "))

        if (opcion == 1):
            addLab()
            os.system("pause")

        elif(opcion == 2):
            editLab()
            os.system("pause")

        elif(opcion == 3):
            showLab()
            os.system("pause")
        
        elif(opcion == 4):
            deleteLab()
            os.system("pause")

        elif(opcion == 5):
            searchLab()
            os.system("pause")







def addSupplier():
    name = input("Nombre del Proveedor: ")
    address = input("Direccion del Proveedor: ")
    phone = input("Telefono del Proveedor: ")
    email = input("Email del Proveedor: ")

    supplier = c.Supplier(name, address, phone, email, 1, None)
    daoSupplier = daoConnection.DaoSupplier(conex)
    daoSupplier.insert(supplier)
    

def editSupplier():
    id = int(input("ID del proveedor a editar: "))
    newName = input("Nuevo nombre del Proveedor: ")
    newAddress = input("Nueva direccion del Proveedor: ")
    newPhone = input("Nuevo telefono del Proveedor: ")
    newEmail = input("Nuevo email del Proveedor: ")


    daoSupplier = daoConnection.DaoSupplier(conex)
    supplier = c.Supplier(newName, newAddress, newPhone, newEmail, 1, id)
    daoSupplier.update(supplier)


def showSupplier():
    daoSupplier = daoConnection.DaoSupplier(conex)
    suppliers = daoSupplier.get_all()
    for supplier in suppliers:
        print(supplier)


def deleteSupplier():
    id = int(input("ID del Proveedor a eliminar: "))
    daoSupplier = daoConnection.DaoSupplier(conex)
    daoSupplier.delete(id)


def searchSupplier():
    id = int(input("ID del Proveedor a buscar: "))
    daoSupplier = daoConnection.DaoSupplier(conex)
    suppliers = daoSupplier.get_by_id(id)
    print(suppliers)



def MenuSupplier():
    print("1. Ingresar Proveedor")
    print("2. Editar Proveedor")
    print("3. Mostrar Proveedor")
    print("4. Eliminar Proveedor")
    print("5. Buscar Proveedor")
    print("6. Salir")

def mainSupplier():
    opcion = 0

    while(opcion != 6): 
        MenuSupplier()
        opcion = int(input("Ingresa una opcion: "))

        if (opcion == 1):
            addSupplier()
            os.system("pause")

        elif(opcion == 2):
            editSupplier()
            os.system("pause")

        elif(opcion == 3):
            showSupplier()
            os.system("pause")
        
        elif(opcion == 4):
            deleteSupplier()
            os.system("pause")

        elif(opcion == 5):
            searchSupplier()
            os.system("pause")




def MenuPrincipal():
    os.system('cls')
    print("----------------------------")
    print("1. Registros de Laboratorios")
    print("2. Registros de Proveedores")
    print("3. Registros empleados")
    print("4. Salir")
    print("----------------------------")


def main():
    opcion= 0
    while(opcion != 4):
        MenuPrincipal()
        opcion = int(input("dime tu opcion:"))
        if (opcion == 1):
            mainLab()
            os.system("pause")
        elif (opcion == 2):
            mainSupplier()
            os.system("pause")    


main()

