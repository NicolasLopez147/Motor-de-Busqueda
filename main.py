import PyPDF2
documento = open("EnfrentandolaEspadadeDobleFilo.pdf")
#leer = PyPDF2.PdfFileReader(documento)
print(dir(documento))
print(help(documento.readline))
print(type(documento.read(5)))
def pintar(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if j == len(matriz)-1:
                print(matriz[i][j],end = "")
            else:
                print(matriz[i][j],end = " ")
        print()

n = int(input())
numeros = input().split(" ")
numeros = list(map(int,numeros))
tablero = []
for i in range(n):
    tablero.append([0 for j in range(n)])
for i in range(n):
    for j in range(n):
        m = max(abs(numeros[0]-i),abs(numeros[1]-j))
        if numeros[2] - m > 0:
            tablero[i][j] = numeros[2]-m

pintar(tablero)