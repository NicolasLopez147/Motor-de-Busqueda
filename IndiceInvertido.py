import os
import leer
from os.path import isdir,join
def buscarIndice(path,pbuscar):
	di = os.listdir(path)
	if "index.pickle" in di:
		print("El indice ya existe")
		buscar(pbuscar)
	else:
		print("El indice sera creado")
		crear(path)
		buscar(pbuscar)

def buscar(pbuscar):
	pass
def crear(path):
	path = join(path,"Prueba.txt")
	print(leer.preparar(path))
def comprobar(path,pbuscar):
	if isdir(path):
		print("El directorio si existe")
		buscarIndice(path,pbuscar)
	else:
		print("El directorio no existe")
		return 1