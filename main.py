import os
import os.path as pt
from os.path import isdir, join
import IndiceInvertido as ii
pathbus,pathin,path,bandera="",os.getcwd(),"",True
cre="""
Jimmy Joseph Jiménez Alvarado (Estudiante de ingeniería electrónica)
Julián Andrés Córdoba (Estudiante de ingeniería de sistemas)
Nicolás López Nieto (Estudiante de ingeniería de sistemas)

Este proyecto fue inspirado por el ingenierio Edwin Andrés Niño Velásquez.
"""
os.system("cls")
print('''
_________
|    __   \            
|   |  |   | __                                  __    _
|   |__|   ||__|                                |__|  | |
|    __    | __  ___  _ _____     __ ___  _ ___  __   | |_____
|   |  |   ||  |/ _ ]| '_  \ \   / // _ ]| '_  \|  |__| |  _  |
|   |__|   ||  |  __/| | | |\ \_/ /|  __/| | | ||  | __ | |_| |
|_________/ |__|\___||_| |_| \___/  \___||_| |_||__|____|_____|
''')
print("Este programa le permite filtrar archivos .pdf y .txt según algunas palabras, seleccione las opciones que desea ingresando los valores dados. Se recomienda correr el programa en la consola de su ordenador\n")
while(bandera):
    
    print("\nMENÚ")
    print("1. Selección del directorio de búsqueda")
    print("2. Hacer una búsqueda")
    print("3. Créditos")
    print("4. Salir")
    op = input('\n'+"Ingrese el número de la opción que desee: ")
    os.system("cls")
    while op != "1" and op != "2" and op!="3" and op!="4":
            print("Opción incorrecta\n")
            print("MENÚ")
            print("1. Selección del directorio de búsqueda")
            print("2. Hacer una búsqueda")
            print("3. Créditos")
            print("4. Salir")
            op = input("\nIngrese el número de la opción que desee: ")
            os.system("cls")
    if op == "1" :
            print('1. Ingresar una ruta')
            print('2. Utilizar la ruta por defecto:','"'+pathin+'"')
            a = input()
            os.system("cls")
            while a != "1" and a != "2":
                print("Opcion incorrecta\n")
                print('1.Ingresar una ruta')
                print('2.Utilizar la ruta por defecto:',pathin)
                a = input()
                os.system("cls")
            if a == "1":
                print('Ingrese la ruta del directorio en el que desea hacer la búsqueda:')
                path = input()
                os.system("cls")
                if not isdir(path):
                    print("La ruta ingresada no es valida")
                    path = ""
            else:
            	path=pathin
            	os.system("cls")
    elif op == "2":
    	if path == "" and pathbus == "":
    		print("Se debe seleccionar un directorio antes de hacer una busqueda")
    	else:
            pathbus = path
            print("El directorio en el que se realizará la búsqueda es:", pathbus)
            print("¿Desea realizar la búsqueda en este directorio?"+'\n'+"1. Sí"+'\n'+"2. No, ingresar ruta")
            b = input()
            os.system("cls")
            while b != "1" and b !="2":
                    print("Opcion incorrecta\n")
                    print("\nEl directorio en el que se realizará la búsqueda es:", pathbus)
                    print("¿Desea utilizar este directorio?"+'\n'+"1. Sí"+'\n'+"2. No, seleccionar directorio")
                    b = input()
                    os.system("cls")
            if b=="2":
                print('Ingrese la ruta del directorio en el que desea hacer la busqueda:')
                pathbus = input()
                if not isdir(pathbus):
                    print("La ruta ingresada no es valida")
                    pathbus = ""
                else:
                	path = pathbus
            if pathbus!= "":
	            os.system("cls")
	            print("Ingrese las palabras que desea buscar. Si no desea agregar más palabras haga doble salto de línea")
	            pbuscar = []
	            while True:
	                a = input()
	                if a == "":
	                    break
	                else:
	                    pbuscar +=a.split(" ")
	            os.system("cls")
	            if len(pbuscar) == 0:
	            	print("No se ingreso ninguna palabra")
	            else:
		            print("Palabras guardadas:")
		            for i in range (len(pbuscar)):
		                if i==0:print(pbuscar[i],end="")
		                else:print(", "+pbuscar[i],end="")
		            print("\n")
		            ii.comprobar(pathbus,pbuscar)
    elif op == "3":
            print('Bienvenido a los créditos.'+'\n')
            print("Este Software fue diseñado como un proyecto de la Universidad Nacional de Colombia por los estudiantes:", cre)
    else:
            os.system("cls")
            print("Gracias por usar el programa, vuelva pronto.")
            bandera = False
