import os
import os.path as pt
from os.path import isdir, join
import IndiceInvertido as ii

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
bandera = True
while(bandera):
	print("MENU")
	print("1.Seleccion del directorio de busqueda")
	print("2.Creditos")
	print("3.Salir")
	op = input("Ingrese la opcion que desee ")
	os.system("cls")
	while op != "1" and op != "2" and op!="3":
		print("Opcion incorrecta\n")
		print("MENU")
		print("1.Hacer una busqueda")
		print("2.Creditos")
		print("3.Salir")
		op = input("Ingrese la opcion que desee ")
		os.system("cls")

	if op == "1" :
		print('1.Ingresar una ruta')
		print('2.Utilizar la ruta por defecto')
		a = input()
		while a != "1" and a != "2":
			print("Opcion incorrecta\n")
			print('1.Ingresar una ruta')
			print('2.Utilizar la ruta por defecto')
			a = input()
		if a == "1":
			print('Ingrese la ruta del directorio en el que desea hacer la busqueda')
			path = input()
		else:
			path = os.getcwd()
			d = True
			print(path,"este es el directorio en el que se encuentra, desea hacer la busqueda en este directorio?")
			print("1.Si")
			print("2.No")
			p = input()
			os.system("cls")
			while p != "1" and p !="2":
				print("Opcion incorrecta\n")
				print(path,"este es el directorio en el que se encuentra, desea hacer la busqueda en este directorio?")
				print("1.Si")
				print("2.No")
				p = input()
			os.system("cls")
			while d and p == "2":
				solo_dir = [di for di in os.listdir(path) if isdir(join(path,di))]
				if len(solo_dir) == 0:
					print("No existen mas directorios, se hara la busqueda en",path)
					break
				print("Estos son los directorios a los que se puede ingresar, escoja uno")
				for i in range(len(solo_dir)):
					print(i,solo_dir[i])
				i = int(input())
				path = join(path,solo_dir[i])
				os.system("cls")
				print(path,"este es el directorio en el que se encuentra, desea hacer la busqueda en este directorio?")
				print("1.Si")
				print("2.No")
				p = input()
				while p != "1" and p !="2":
					print("Opcion incorrecta\n")
					print(path,"este es el directorio en el que se encuentra, desea hacer la busqueda en este directorio?")
					print("1.Si")
					print("2.No")
					p = input()
				os.system("cls")
		d = True
		print("Ingrese las palabras que desea buscar, si no desea agregar mas palabras haga doble salto de linea")
		pbuscar = set()
		while d:
			a = input()
			if a == "\n" or a == "":
				d = False
			else:
				pbuscar.add(a)
		os.system("cls")
		print("Palabras guardadas")
		pbuscar = list(pbuscar)
		print(pbuscar)
		ii.comprobar(path,pbuscar)
	elif op == "2":
		print('Bienvenido a la opcion 2')
		print()
	else:
		os.system("cls")
		print("Gracias por usar el programa, vuelva pronto")
		bandera = False

	
	