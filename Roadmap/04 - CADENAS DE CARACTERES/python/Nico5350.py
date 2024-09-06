"""
Operaciones
"""
s1= "Hola"
s2= "Python"

#concatenacion
print(s1,s2)
print(s1 + "bienvenido a " + s2 )
print(f"{s1} bienvenidos a {s2}")

#repeticion
print(s1 * 3)

#indexacion
print(s1[0] + s1[1] + s1[2] + s1[3])

#longitud
print(len(s1 + s2))

#Slicing (porcion)
print(s2[0:3])
print(s2[2:])
print(s2[:2])

#Busqueda
print("y" in s2)
print("y" in s1)

#Reemplazo
print(s1.replace("a","o"))

#División
print(s2.split("t"))

#Conversion a mayusculas y minusculas
print(s2.upper())
print(s2.lower())
print("hola python".title())
print("hola python".capitalize())

#eliminacion de espacios al principio y al dinal
print(" hola python ".strip())

#busqueda al principio y al final
print(s1.startswith("ho"))
print(s1.startswith("la"))
print(s1.endswith("ho"))
print(s1.endswith("la"))

s3="Nicolas Agustin Contreras"

#busqueda de posicion
print(s3.find("contreras"))
print(s3.find("a"))

#Busqueda de ocurrencias
print(s3.lower().count("a"))

#Formateo
print("Saludo: {}, lenguaje {}!".format(s1,s2))

#interpolacion
print(f"Saludo: {s1}, lenguaje {s2}!")

#Transformacion en lista de caracteres
print(list(s3))

#Transformacion de lista en cadenas
l1= [s1,",",s2,"!"]
print("-".join(l1))

#Transformaciones numericas
s4="123456789"
s4=float(s4)#o int
print(s4)

#Comprobaciones varias
print(s1.isalnum())
print(s1.isalpha())
print(s1.isnumeric())

"""
Extra
"""

def check(palabra1:str ,palabra2:str):
    #palindromos

    print(f"¿{palabra1} es un palindromo?: {palabra1 == palabra1[::-1]}")  
    print(f"¿{palabra2} es un palindromo?: {palabra2 == palabra2[::-1]}")  
    #anagramas

    print(f"¿{palabra1} es un anagrama de {palabra2}?: {sorted(palabra1) == sorted(palabra2)}")
    #Isogramas

    def isogram(word: str) -> bool:
        word_dict = dict()
        for palabra in palabra1:
            word_dict[palabra] = word_dict.get(palabra,0)+1
        
        isograma=True
        values=list(word_dict.keys())
        isogram_len=values[0]

        for word_count in values:
            if word_count != isogram_len:
                isograma=False
                break

    print(f"¿{palabra1} es un isogram?: {isogram(palabra1)}")
    print(f"¿{palabra2} es un isogram?: {isogram(palabra2)}")
    return isogram

    

check("amor","roma")