import os.path
import leer
import glob
from os.path import isdir,join
import pickle
from os import startfile
def buscarIndice(path,pbuscar):
	di = os.listdir(path)
	if "index.pickle" in di:
		print("El indice ya existe")
		buscar(path,pbuscar)
	else:
		print("El indice sera creado")
		crear(path)
		buscar(path,pbuscar)

def buscar(path,pbuscar):
	fpath = join(path,"index.pickle")
	fichero = open(fpath,'rb')
	iInvertido = pickle.load(fichero)
	fichero.close()
	
	archivos_encontrados = set()
	for p in pbuscar:
		if p in iInvertido.keys():
			archivos_encontrados.update(iInvertido[p])
		else:
			print("No se encontro ninguna referencia a la palabra '{palabra}'".format(palabra=p))
	archivos_encontrados = list(archivos_encontrados)
	parchivo = join(path,archivos_encontrados[1])
	os.startfile(parchivo)

def crear(path):
	di = os.listdir(path)
	archivostxt = glob.glob(join(path,"*.txt"))
	archivospdf = glob.glob(join(path,"*.pdf"))
	llaves = set()
	iInvertido = {}
	for atxt in archivostxt:
		llaves.update(leer.preparar(atxt,"txt"))
		archivo = str(os.path.split(atxt)[1])
		print(archivo)
		for l in llaves:
			if l not in iInvertido.keys():
				iInvertido[l] = {archivo}
			else:
				iInvertido[l].add(archivo)
	fpath = join(path,"index.pickle")
	fichero = open(fpath,"wb")
	pickle.dump(iInvertido,fichero)
	fichero.close()
def comprobar(path,pbuscar):
	if isdir(path):
		print("El directorio si existe")
		buscarIndice(path,pbuscar)
	else:
		print("El directorio no existe")
		return 1