"""
Operadores
"""

#Operadores:

print(f"Suma: 5+5 = {5+5}")
print(f"Resta: 5-4 = {5-4}")
print(f"División: 10/5 = {10/5}")
print(f"Multiplicación: 5*5 = {5*5}")
print(f"Resto 10%5 = {10%5}")
print(f"Division entera 11/5 ={11//5}")
print(f"multiplo 5**5 = {5**5}")

#Operadores comparacion:

print(f"Operador de igualdad == :{5==5}")
print(f"Operador desigualdad != :{5!=10}")
print(f"Mayor > :{10>5}")
print(f"Menor < : {5<10}")
print(f"Mayor igual >= :{10>=10}")
print(f"Menor igual <= : {9<=10}")

#Operadores logicos:

print(f"AND 10 + 5 == 15 AND 5 + 9 == 14 :{10+5 == 15  and  5+9 == 14}")
print(f"OR 5 + 5 == 10 OR 5 + 5 == 11 : {5 + 5 == 10 or 5 + 5 == 11} ")
print(f"NOT 3 + 3  == 7 : {not 3 + 3== 7 }")

#Operadores asignacion
my_number=10

print(my_number)
my_number += 2
print(my_number)
my_number -= 2
print(my_number)
my_number /= 2
print(my_number)
my_number *=2
print(my_number)
my_number //=2
print(my_number)
my_number **=2

#Operador identidad:
my_new_number=my_number
print(f"my_number is my_new_number :{my_number is my_new_number}")
print(f"my_number is not my_new_number:{my_number is not my_new_number}")

#Operador de pertenencia:

print(f"'i' in 'Nicolas' :{'i' in 'Nicolas'}")
print(f"'e' not in 'Nicolas' :{'i' not in 'Nicolas'}")

"""
Estructuras de control
"""

#condicionales:

my_name="Nicolas"

if my_name == 'Nicolas':
    print("Este es tu nombre")
elif my_name == 'Agustin':
    print("Es tu segundo nombre")
else:
    print("nombre equivocado")

#iterativas:

for i in range(11):
    print (i)

numero=1
while numero >= 10:
    print(numero)
    numero += 1

#manejo de excepciones 

try:
    print(10/0)
except:
    print("se produjo un error")
finally:
    print("finalizo manejo de excepciones")

#programa dificultad extra:


for number in range(10,56):
    excepcion=16
    if number % 2 == 0 and number != 16 and number % 3 == 0:
        print(number)
    

