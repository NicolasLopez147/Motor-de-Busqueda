import os.path
import leer
import glob
from os.path import isdir,join
import pickle
from os import startfile
from os import remove

def buscarIndice(path,pbuscar):
    di = os.listdir(path)
    if "index.pickle" in di:
        print("El índice ya existe, ¿Desea actualizarlo?"+'\n'+"1. Sí"+'\n'+"2. No")
        a=input()
        while a!="1" and a !="2":
            os.system("cls")
            print("Opcion incorrecta")
            print("El índice ya existe, ¿Desea actualizarlo?"+'\n'+"1. Sí"+'\n'+"2. No")
            a=input()
        if a =="1":                    
            print("El índice será actualizado, espere un momento.\n")
            remove(path+"/index.pickle")
            crear(path)
            buscar(path,pbuscar)
        else: buscar(path,pbuscar)

    else:
        print("El índice será creado, espere un momento.\n")
        crear(path)
        buscar(path,pbuscar)

def buscar(path,pbuscar):
    fpath = join(path,"index.pickle")
    fichero = open(fpath,'rb')
    iInvertido = pickle.load(fichero)
    fichero.close()
    pbuscar = leer.comprobar(pbuscar)
    archivos_encontrados = set()
    for p in pbuscar:
            if p in iInvertido.keys():
                    if archivos_encontrados == set():
                            archivos_encontrados = iInvertido[p]
                    else:
                            archivos_encontrados  = archivos_encontrados & iInvertido[p]
            else:
                    #print("No se encontro ninguna referencia a la palabra '{palabra}'".format(palabra=p))
                    archivos_encontrados = set()
                    break
    archivos_encontrados = list(archivos_encontrados)
    if len(archivos_encontrados) == 0:
            print("No se encontraron documentos que referencien todas las palabras ingresadas")
            return 0
    while True:
            print("Estos son los archivos encontrados, seleccione alguno para abrirlo o vuelva al menú principal:")
            print("1. Volver al menú principal")
            for i in range(len(archivos_encontrados)):
                    print(str(i+2)+".",archivos_encontrados[i])
            try:
                    op = int(input())
                    os.system("cls")
                    if op == 1:
                            os.system("cls")
                            return 0
                    if op-2 < 0 :
                        os.system("cls")
                        print("Opcion incorrecta\n")
                    else:
                        parchivo = join(path,archivos_encontrados[op-2])
                        os.startfile(parchivo)
            except:
                    os.system("cls")
                    print("Opcion incorrecta\n")


def crear(path):
    archivostxt = glob.glob(join(path,"*.txt"))
    archivospdf = glob.glob(join(path,"*.pdf"))
    iInvertido = {}
    for atxt in archivostxt:
            llaves = set()
            llaves = leer.preparar(atxt,"txt")
            if "" in llaves:
                    llaves.remove("")
            archivo = str(os.path.split(atxt)[1])
            for l in llaves:
                    if l not in iInvertido.keys():
                            iInvertido[l] = {archivo}
                    else:
                            iInvertido[l].add(archivo)
    for apdf in archivospdf:
            llaves = set()
            llaves = leer.preparar(apdf,"pdf")
            if "" in llaves:
                    llaves.remove("")
            archivo = str(os.path.split(apdf)[1])
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
            buscarIndice(path,pbuscar)
    else:
            print("El directorio no existe")
