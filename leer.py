# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:36:30 2020

@author: sable
"""
import PyPDF2
import os
from os.path import join,isfile
caracteres = [",",".","'","\n",":","\xad"]
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
    archivo = open(arg, "r")
    contenido = set()
    for linea in archivo.readlines():
        linea = linea.split(" ")
        for palabra in linea:
            contenido.add(palabra)
    archivo.close() 
    contenido = list(contenido)
    contenido = comprobar(contenido)
    return contenido

def comprobar(pbuscar):
	for palabra in pbuscar:
		for letra in palabra:
			if letra in caracteres:
				aux = list(palabra)
				if palabra in pbuscar:
					pbuscar.remove(palabra)
				aux.remove(letra)
				pbuscar.append("".join(aux))

	pbuscar = [palabra.lower() for palabra in pbuscar]
	return pbuscar

def preparar (path):
	llaves = leer_TXT(path)
	return set(llaves)