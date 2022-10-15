# TALLER 4 PYTHON
# AUTOR(A): JUAN CAMILO PEREZ
#FECHA: 14 OCTUBRE 2022
from datetime import date
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
if animal=="PERRO":
    print("Este animal es el mejor amigo del hombre:",animal)
elif animal=="GATO":
    print("Este animal persigue a los ratones",animal)
elif animal=="OSO":
    print("Este animal vive en el polo norte:",animal)
else:
    print("No es Perro, No es Gato , No es Oso , es",animal)
print()
print('FIN')