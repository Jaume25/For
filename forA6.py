#coding: utf-8

print "CONTADOR DE PARES E IMPARES"

num=int(input("Cuantos valores va a introducir? "))
aux=0
aux2=0

while num<=0:
	print "Imposible"
	num=int(input("Intentalo de nuevo: "))
	
for i in range (1,num+1):
	num2=int(input("Escriba el numero "+str(i)+": "))
	if num2 % 2 == 0:
		aux+=1
	if num2 % 2 !=0:
		aux2+=1	
print "Ha escrito "+str(aux)+" numeros pares y "+str(aux2)+" numeros impares"
print "Gracias por su colaboracion"

