#coding: utf-8

print "SUMA ENTRE VALORES"

num=int(input("Escriba un numero entero: "))
num2=int(input("Escriba un numero entero mayor que "+str(num)+": "))
aux=0

while num2<=num:
	print "Le he pedido un numero entero mayor que "+str(num)
	num2=int(input("Escriba un numero entero mayor que "+str(num)+": "))
	
for i in range (num,num2+1):
	aux+=i
print "La suma desde",num,"hasta",num2,"es",aux
