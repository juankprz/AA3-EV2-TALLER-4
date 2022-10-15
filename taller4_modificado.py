# TALLER 4 PYTHON
# AUTOR(A): JUAN CAMILO PEREZ
#FECHA: 14 OCTUBRE 2022
from datetime import date
nombre=input('Digite su nombre:')
print("Bienvenido",nombre.title())	
hoy=date.today()	#fecha actual
print("Hoy es el dia: ", hoy)
print()
print("EJERCICIO DE LAS CLASES DE TRIANGULOS") 
a=int(input("digite el valor de A: "))
b=int(input("digite el valor de B: "))
c=int(input("digite el valor de C: "))
if a==b and a==c and b==c:
  print('EL TRIANGULO ES EQUILATERO')
else:
   if a==b or b==c or a==c:
      print("EL TRIANGULO ES ISOCELES")
   else:
       print('EL TRIANGULO ES ESCALENO')
print()
animal=input("Digite un animal: ")
animal=animal.upper()
if animal=="PEZ":
    print("Pueden ser de agua Salada o agua dulce",animal)
elif animal=="LEON":
    print("Es el rey de la selva",animal)
elif animal=="TORTUGA":
    print("Es un animal al que catalogamos lento",animal)
else:
    print("Animal no registrado",animal)
print("TALLER 4 modificado")
print('FIN')