# Strings

my_string = "mi super string"
other_string = "otro string"

print(len(my_string))
print(len(other_string))

print(my_string + " " + other_string)

my_new_line_string = "Este es un string con \n salto de linea"
print(my_new_line_string)

my_tab_string = "\t Este es un string con tabulacion"
print(my_tab_string)

my_scape_string = "\\t Este es un string \\n escapado"
print(my_scape_string)

# Formateo

name, surname, age = "Tavo", "Meza", 34

print("Mi nombre es {} {} y tengo {} años.".format(name, surname, age))

print("Mi nombre es %s %s y tengo %d años." %(name, surname, age))

print(f"Mi nombre es {name} {surname} y tengo {age} años.")

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language
print(a)
print(f)

# División

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2]
print(language_slice)

# Reverse ,  el final empieza en -1

reverse_language = language[::-1]
print(reverse_language)

# Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.upper().isupper())
print(language.lower().isupper())
print(language.startswith("py"))
print(language.startswith("Py"))
print("Py" == "py")










