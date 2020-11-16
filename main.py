import PyPDF2
documento = open("EnfrentandolaEspadadeDobleFilo.pdf")
#leer = PyPDF2.PdfFileReader(documento)
print(dir(documento))
print(help(documento.readline))
print(type(documento.read(5)))
