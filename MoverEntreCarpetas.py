import os
import os.path
from os.path import isdir, join
path = os.getcwd()
#sub = os.listdir(path)
#sub.append("Atras")
#for i in range(len(sub)):
#	pass
	#print(i,sub[i])
#root = "C:\\Users\\Antonio\\Desktop"
#print(os.walk(path))
#tree = os.walk(root)
#print(tree[0])
"""
bandera = True
while bandera:
	sub = os.listdir(root)
	sub.append("Atras")
	for i in range(len(sub)):
		print(i,sub[i])
	a = os.path.isdir('Proyectos')
	print(a)
	bandera = False
"""
#n = input()
#path = path+"\\"+n
#print(os.getcwd())
solo_dir = [di for di in os.listdir(path) if isdir(join(path,di))]
print(solo_dir)