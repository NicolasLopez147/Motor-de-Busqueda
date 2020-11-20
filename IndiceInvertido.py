import os
from os.path import isdir
def buscarIndice(path):
	di = os.listdir(path)
	if "index.pickle" in di:
		buscar(pbuscar)
	else:
		crear(path)
		buscar(pbuscar)

def buscar(pbuscar):
	pass
def crear(path):
	pass
def comprobar(path,pbuscar):
	if isdir(path):
		buscarIndice(path,pbuscar)
	else:
		return 1