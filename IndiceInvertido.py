import os
import leer
import glob
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
	di = os.listdir(path)
	archivostxt = glob.glob(join(path,"*.txt"))
	archivospdf = glob.glob(join(path,"*.pdf"))
	llaves = set()
	iInvertido = {}
	for atxt in archivostxt:
		llaves.update(leer.preparar(atxt,"txt"))
		for l in llaves:
			if l not in iInvertido.keys():
				iInvertido[l] = {atxt}
			else:
				iInvertido[l].add(atxt)
	for k,v in iInvertido.items():
		print(k,":")
		print(v)
def comprobar(path,pbuscar):
	if isdir(path):
		print("El directorio si existe")
		buscarIndice(path,pbuscar)
	else:
		print("El directorio no existe")
		return 1