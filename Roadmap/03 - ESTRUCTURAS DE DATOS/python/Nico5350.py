"""
Estructuras
"""
#listas: (tienen un orden y se pueden cambiar)

my_list=['Nicolas','Agustin','Contreras']
my_list.append('Lucas') #inserccion
my_list.remove('Agustin')   #borrado
my_list[2]  #acceso
my_list[2]='Sofia'  #actualizacion


print(my_list)
my_list.sort()  #ordenacion
print(my_list)

#Tuplas: (son inalterables)

my_tuple = ("Nicolas","Agustin","Contreas")
print(my_tuple)
print(my_tuple[0])  #acceso
print(my_tuple[1])  #acceso
print(my_tuple[2])  #acceso

my_tuple = tuple(sorted(my_tuple))
print(type(my_tuple))
print(my_tuple)

#Sets :(no estan ordenados y no puede duplicar datos)
my_set = {"Nicolas","Agustin","Contreas"}
print(my_set)

my_set.add("Sofia") #inserción
my_set.add("Sofia") #Evita duplicados
my_set.remove("Nicolas") #eliminacion

print(my_set)

my_set = set(sorted(my_set)) #No se puede ordenar de ninguna forma
print(type(my_set))

print(my_set)

#Diccionario:

my_dict : dict = {"Nombre":"Nicolas","2doNombre":"Agustin","Apellido":"Contreas","Edad":"21"}

print(my_dict["Nombre"])#acceso

my_dict["Email"] = "nicocontreras5350@gmail.com" #inserccion

my_dict["Edad"]="22" #actualizacion

del my_dict["2doNombre"]

print(my_dict)

my_dict=dict(sorted(my_dict.items()))   #ordenacion

print(my_dict)
print(type(my_dict))

"""
Extra
"""
def my_agenda():

    def insert_contact():
        numero = input("Introduce el teléfono del contacto: ")
        if numero.isdigit() and len(numero) > 0 and len(numero) <= 11:
            agenda[nombre] = numero
        else:
            print(
                "Debes introducir un número de teléfono un máximo de 11 dígitos.")

    agenda:dict= {}
    while True :

        print("")
        print("2. Inserción de contacto")
        print("3. Actualización de contacto")
        print("4. Eliminacion de contacto")
        print("5. Salir")

        operacion=input("\nIngrese codigo: ")

        match operacion:
            case "1":
                nombre=input("Inserte el nombre de contacto: ")
                if nombre in agenda:
                    print (f"El contacto {nombre} esta en la agenda {agenda[nombre]}.")
                else:
                    print(f"El contacto {nombre} no esta en la agenda")
                
            case "2":
                nombre=input("Inserte el nuevo nombre de contacto: ")
                insert_contact()
            case "3":
                nombre=input("Inserte el nuevo nombre de contacto: ")
                if nombre not in agenda:
                    insert_contact()
                else:
                    print(f"El contacto {nombre} no existe")

            case "4":
                nombre=input("Inserte el contacto que desea eliminar: ")
                if nombre in agenda:
                    del agenda[nombre]
                    print("el contacto {nombre} fue eliminado")
                else:
                    print(f"El contacto {nombre} no esta en la agenda")
                    
                print(agenda)
            case "5":
                print("Saliendo de agenda.")
                break
            case _: 
                print("Elige una opcion valida.")   

my_agenda()







