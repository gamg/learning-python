# Variables

from audioop import add


myvariable = "my super variable"
print(myvariable)

my_second_variable = 777
print(my_second_variable)

my_int_to_str_variable = str(my_second_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenar variables en un print
print(myvariable, my_second_variable, my_bool_variable)
print("Este es el valor de:", my_second_variable)

# Funciones del sistema
print(len(myvariable))

# Variables en una sola línea
name, surname, alias, age = "Gustavo", "Meza", "gamg", 34
print('Mi nombre es', name, surname, ", Mi edad es", age, "y mi alias es", alias)

# inputs
"""
name = input('What is your name: ')
age = input('How old are you? ')
print(name)
print(age)
"""

# Cambiado tipo de dato, python es un lenguaje no tipado
name = 77
age = "Pedro"
print(name)
print(age)

# Forzamos el tipo?
address: str = "Mi direccion"
address = 32
print(type(address))
# no igual se puede cambiar facilmente