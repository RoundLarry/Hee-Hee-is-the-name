print ("Buenos días, bienvenid@ a Dulceria Mary, por favor ingrese los siguientes datos")
nombre=input("Nombre:")
folio=input("Folio:")
print ("Usuario registrado. " + "Su cuenta tiene vigentes 2 cupones" )
print ("Ingrese la cantidad de dulces que desea calcular")
bolsas=int(input("N.- de bolsas de dulces:"))
dulces=int(input("N.- de dulces por bolsa: "))
#r=numero de cupones
r=2

print("----Precio por unidad: $1.00----")
print("N.- de Dulces totales:")
#a=TotalDulces
a=(bolsas*dulces)
print (a)
#i=iva
i=0.15
print("Costo total de los impuestos:")
#b=Iva*Total de Dulces
b= (a*i)
print (b)
print("Costo total:")
#c=Total
c= (a+b)
print(c)
print("------------------------------------------------------------------------")
print ("En estos momentos la tienda cuenta con un descuento del 10% por aniversario por lo cual el total de su compra es de:")
#d=Descuento
d=0.10
e=(c*d)
print("Costo total:")
#f=CostoTotal
f=(c-e)
print (f)
print("------------------------------------------------------------------------")

print ("¿Entre cuantas personas se desea pagar el total?")
p=int(input("Personas:"))
x=(f/p)
print("Cada persona paga: ")
print(x)

print("*****************************")
print ("-----RECIVO-----")
print ("Cliente: " + nombre)
print ("Folio: " , folio)
print ("Total a pagar: " )
print (f)
print("*****************************")

print("ingrese el monto a pagar para saber si puede obtener un cupón")
print ("-----cupones validos solo para compras sin centavos------")
v=int(input("Monto:"))
print (isinstance(v, int))
print("false = no cupón, true = +1 cupón a su cuenta")
print ("cupones totales:")
print(eval("r+1"))
