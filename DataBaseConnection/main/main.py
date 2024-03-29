import os
import sys
sys.path.append(r"C:\Users\Jader Mendoza\Desktop\ExamenFinalLenguajeProgramacion\DataBaseConnection")
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
    id = int(input("ID de la ciudad a editar: "))
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



def Menu():
    print("1. Igresar Laboratorio")
    print("2. Editar Laboratorio")
    print("3. Mostrar Laboratorio")
    print("4. Eliminar Laboratorio")
    print("5. Buscar Laboratorio")
    print("6. Salir")

def main():
    opcion = 0

    while(opcion != 6): 
        Menu()
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

main()

