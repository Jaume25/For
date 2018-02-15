#coding: utf-8

print "MAYORES QUE EL PRIMERO"

num=int(input("Cuantos valores va a introducir? "))
num2=int(input("Escriba un numero: "))

while num<=0:
	print "Imposible"
	num=int(input("Intentalo de nuevo: "))
	
for i in range (1,num+1):
	num3=int(input("Escriba un numero mas grande que "+str(num2)+": "))
	if num3<num2:
		print str(num3)+" no es mayor que "+str(num2)
print "Gracias por su colaboracion" 
