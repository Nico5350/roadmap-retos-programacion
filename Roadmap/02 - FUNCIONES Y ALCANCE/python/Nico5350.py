"""
Funciones definidas por el usuario
"""

#simple
 
def greet():
    print("Hola, Python")
greet()

#con retorno 

def return_greet():
    return "Hola, Python"

print(return_greet())

#con un argumento

def args_greet(greet,name):
    print(f"{greet} {name}")
args_greet("hello","Nicolás")
args_greet(name="Nicolás",greet="hello")

def default_arg_greet(name="Python"):
    print(f"Hola ,{name}!")

default_arg_greet()
default_arg_greet("Nicolás")

#con argumento y return:

def return_args_greet(greet,name):
    return f"{greet},{name}!"

print(return_args_greet("nicolas","hola"))

#con return de varios valores:

def mulitiple_return_greet():
    return "Hola","Nicolás"

greet,name= mulitiple_return_greet()
print(greet)
print(name)

#con un numero variable de argumentos :

def variable_arg_greet(*names):# "*" siginifica mas de un nombre
    for name in names:
        print(f"Hola, {name} !")

variable_arg_greet("Nicolas","Agustin","Contreras")

#con un numero variable pero con palabra clave:

def variable_key_arg_greet(**names):
    for key,value in names.items():
        print(f"Hola, {value} ({key}) !")

variable_key_arg_greet(lenguaje="Python",name="Nicolas",age="21")


"""
Funciones dentro de funciones
"""

def funcion_externa():
    def funcion_interna():
        print("Funcion interna: Hola ,Python!")
    funcion_interna()

funcion_externa()

"""
Funciones del lenguaje (built -in)
"""
print(len("Nicolas contreras"))#funcion que cuenta
print(type("Nicolas contreras"))#tipo de clase
print("Nicolas contreras".upper())

"""
variables local y global 
"""
global_variable=" Python"
print(global_variable)

def hola_python():
    local_variable= "Hello"
    print(f"{local_variable} {global_variable}!")

hola_python()

"""
extra
"""
def funcion_numero(texto_1,texto_2)-> int:
    cont = 0
    for numero in range(1,101):
        if numero % 3 == 0 and numero % 5 == 0:
            print(texto_1 + texto_2)
        elif numero % 3 == 0:
            print(texto_1)
        elif numero % 5 == 0:
            print(texto_2)
        else:
            print(numero)
            cont+=1
    return cont

print(funcion_numero("Texto 1","Texto 2"))