#coding: utf-8

print "NUMEROS NEGATIVOS"

num=int(input("Cuantos valores va a introducir? "))
aux=0

while num<=0:
	print "Imposible"
	num=int(input("Intentalo de nuevo: "))
	
for i in range (1,num+1):
	num2=int(input("Escriba el numero "+str(i)+": "))
	if num2<0:
		aux+=1
print "Ha escrito "+str(aux)+" numeros negativos"
