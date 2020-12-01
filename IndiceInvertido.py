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
	if len(archivos_encontrados) == 0:
		print("No se encontraron documentos que referencien las palabras ingresadas")
		return 0
	
	while True:
		print("Estos son los archivos encontrados, escoja uno")
		for i in range(len(archivos_encontrados)):
			print(i,archivos_encontrados[i])
		print(len(archivos_encontrados),"Volver al menu principal")
		try:
			op = int(input())
			os.system("cls")
			if op == len(archivos_encontrados):
				os.system("cls")
				return 0
			parchivo = join(path,archivos_encontrados[op])
			os.startfile(parchivo)
		except:
			os.system("cls")
			print("Opcion incorrecta\n")


def crear(path):
	di = os.listdir(path)
	archivostxt = glob.glob(join(path,"*.txt"))
	archivospdf = glob.glob(join(path,"*.pdf"))
	iInvertido = {}
	for atxt in archivostxt:
		llaves = set()
		llaves = leer.preparar(atxt,"txt")
		archivo = str(os.path.split(atxt)[1])
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