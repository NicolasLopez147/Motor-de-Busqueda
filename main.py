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
			while d:
				print("")
				solo_dir = [di for di in os.listdir(path) if isdir(join(path,di))]
				for i in range(len(solo_dir)):
					#print(i,solo_dir[i])
					pass
				d = False 
		
		#ii.buscarIndice(path)
	elif op == "2":
		print('Bienvenido a la opcion 2')
		print()
	else:
		os.system("cls")
		print("Gracias por usar el programa, vuelva pronto")
		bandera = False

	
	