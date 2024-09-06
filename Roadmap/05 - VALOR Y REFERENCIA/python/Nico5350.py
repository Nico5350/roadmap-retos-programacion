"""
Valor y referencia
"""

#Tipos de datos por valor:

my_int_a=10
my_int_b = my_int_a
my_int_b=20
#my_int_a=30
print(my_int_a)
print(my_int_b)

#Tipos de datos por referencia:

my_list_a=[10,20]
my_list_b=my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)

#Funciones con datos por valor

my_int_c=10
def my_int_func(my_int:int):
    my_int=20
    print(my_int)

my_int_func(my_int_c)
print(my_int_c)

#funciones con datos por referencia:

my_list_c=[10,20]
def my_list_func(my_list: list):
    my_list.append(30)

    my_list_d=my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)

my_list_c=[10,20]
my_list_func(my_list_c)
print(my_list_c)

"""
Extra
"""
#por valor:



def value(valor_a:int,valor_b:int):
    aux=valor_a
    valor_a=valor_b
    valor_b=aux
    return valor_a,valor_b


my_int_d=10
my_int_e=20

my_int_f,my_int_g=value(my_int_d,my_int_e)

print(f"{my_int_d},{my_int_e}")
print(f"{my_int_f},{my_int_g}")

#por referencia:

def value(valor_a:list,valor_b:list):
    aux=valor_a
    valor_a=valor_b
    valor_b=aux 
    return valor_a,valor_b


my_list_d=[10,20]
my_list_e=[30,40]

my_list_f,my_list_g=value(my_list_d,my_list_e)

print(f"{my_list_d},{my_list_e}")
print(f"{my_list_f},{my_list_g}")