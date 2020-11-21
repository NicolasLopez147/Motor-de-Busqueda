# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:36:30 2020

@author: sable
"""
import pypdf2

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
    return(contenido)

def leer_TXT(arg):
    archivo = open(arg, "r")
    contenido = ""
    for linea in archivo.readlines():
        contenido = contenido + linea
    archivo.close() 
    contenido.split()
    contenido = set(contenido)
    return(contenido)