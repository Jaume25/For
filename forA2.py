#coding: utf-8

print "DIVISORES"

x=int(input("Escriba un numero mayor que cero: "))

while x>0:
	y=int(input("¡Le he pedido un numero entero mayor que cero"))

for i in range (x,y):
	if i % 2 == 0:
		print "El numero "+str(i)+" es un numero par"
	if i % 2 != 0:
		print "El numero "+str(i)+" es un numero impar"
