#coding: utf-8

print "PARES E IMPARES"

x=int(input("Escriba un numero entero: "))
y=int(input("Escriba un numero entero mayor que "+str(x)+": "))

while x>y:
	print "¡Le he pedido un numero entero mayor que "+str(x)+"!"
	y=int(input("Intentelo de nuevo: "))

for i in range (x,y+1):
	if i % 2 == 0:
		print "El numero "+str(i)+" es un numero par"
	if i % 2 != 0:
		print "El numero "+str(i)+" es un numero impar"
