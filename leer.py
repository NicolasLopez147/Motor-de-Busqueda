# -*- coding: utf-8 -*-

import os
from os.path import join,isfile
caracteres = {",",".","'","\n",":","\xad","!","?","¡","¿","/","@","«","»",";","",'"',"(",")","|","-","_","[","]"}
#palabras_no_deseadas = ["de","la","con","un","una","unos","unas","el","","ellos"]

def leer_PDF(arg):
    from PyPDF2 import PdfFileReader
    pdf_document = arg  
    contenido = ""
    with open(pdf_document, "rb") as filehandle:  
        pdf = PdfFileReader(filehandle)
        pages = pdf.getNumPages()

        for i in range(pages):
            page1 = pdf.getPage(i)
            page_content = page1.extractText()
            contenido = contenido + page_content
        contenido = contenido.split(" ")
        contenido = set(contenido)
        contenido = list(contenido)
        contenido=comprobar(contenido)
        return(contenido)

def leer_TXT(arg):
    archivo = open(arg, "r",encoding="utf-8")
    contenido = set()
    for linea in archivo.readlines():
        linea = linea.split(" ")
        for palabra in linea:
            contenido.add(palabra)
    archivo.close()
    contenido = list(contenido)
    contenido = comprobar(contenido)
    return contenido

def comprobar(contenido):
	for i in range(len(contenido)):
		for letra in contenido[i]:
			if letra in caracteres:
				contenido[i] = contenido[i].replace(letra,"")

	contenido = [palabra.lower() for palabra in contenido]
	contenido = list(set(contenido))
	return contenido

def preparar (path,tipo):
	if tipo == "txt":
		llaves = leer_TXT(path)
	if tipo == "pdf":
		llaves = leer_PDF(path)
	return set(llaves)

