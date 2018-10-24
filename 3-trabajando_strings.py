"|Asi se declaran los caracteres/cadenas|"
nombres = "Cristian"

"|Los saltos de linea se dan usando '\n'|"
print(nombres + "\n" + "Tomat")


"""|Para imprimir cualquier tipo de caracter especial
utilizamos \ y seguido el caracter|"""
print("\"Ni que fuera chiquito\"")


"|Funcion para imprimir todas las letreas minusculas|"
"Estructura: nombre_de_la_variable.lower()"
print(nombres.lower())


"|Funcion para imprimir todas las letreas MAYUSCULAS|"
"Estructura: nombre_de_la_variable.upper()"
print(nombres.upper())


"""|Funcion para comprobar si la palabra esta en
minusculas (retorna un valor boolean)|
"""
"Estructura: nombre_de_la_variable.islower()"
print(nombres.islower())


"""|Funcion para comprobar si la palabra esta en
MAYSCULAS (retorna un valor boolean)|
"""
"Estructura: nombre_de_la_variable.isupper()"
print(nombres.isupper())


"""|Funcion para contar el numero de caracteres
de una cadena|
"""
"Estructura: len(nombre_de_variable)"
print(len(nombres))


"|Acceder a caracteres especificos de una cadena|"
"Estructura: nombre_de_variable[numero_caracter]"
print(nombres[0])


"""|Funcion para buscar la posicion inicial
de un caracter o palabra especifica dentro de un
string o cadena|
"""
"Estructura: nombre_de_la_variable.index(Busqueda)"
print(nombres.index("r"))

"""|Funcion para remplazar una parte del string
con un nuevo caracter o cadena especificado|
"""
"""Estructura:
nombre_de_la_variable.replace("antiguo","nuevo")"""
print(nombres.replace("tian","topher"))
