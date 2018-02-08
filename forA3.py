#coding: utf-8

print "DIVISORES"

x=int(input("Escriba un numero mayor que cero: "))

while x<=0:
	print "¡Le he pedido un numero entero mayor que cero!"
	x=int(input("Intentelo de nuevo: "))

print "Los divisores de "+str(x)+" son: "

for i in range (1, x + 1):
        if x % i == 0:
            print(i)
