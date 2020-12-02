# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:36:30 2020

@author: sable
"""
import PyPDF2
import os
from os.path import join,isfile
caracteres = {",",".","'","\n",":","\xad","!","?","¡","¿","/","@","«","»"}
#palabras_no_deseadas = ["de","la","con","un","una","unos","unas","el","","ellos"]
def leer_PDF(arg):
    pdf_file = open(arg)
    read_pdf = pypdf2.PdfFileReader(pdf_file)
    number_of_pages = read_pdf.getNumPages()
    contenido = ""
    for i in range(number_of_pages - 1):
        page = read_pdf.getPage(i)
        page_content = page.extractText()
        contenido = contenido + page_content
    contenido.split()
    contenido = set(contenido)
    return contenido

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
		pass
		#llaves = leer_PDF(path)
	return set(llaves)
