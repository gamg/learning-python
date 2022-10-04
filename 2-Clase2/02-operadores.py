### Operadores aritmeticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 2)
print(2 ** 3 + 3 - 7 / 1 // 4)

# divsion con resultado aproximado
# 10/3 = 3.333333 
print(10 // 3) # 10 // 3 = 3

# exponente
print(2 ** 3)

print("Hola " + "Python")
print("Hola" + str(5))
print("Hola " * 4)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))


### Operadores de comparacion ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

# aqui ordena alfabeticamente si se compara strings
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")
print("aaaa" >= "abaa")

# aqui cuenta los caracteres
print(len("Hola") >= len("aaa"))


### Operadores logicos ###

print(3 > 4 and "Hola" > "Python") # false and false
print(3 > 4 or "Hola" > "Python")  # false or false
print(3 < 4 and "Hola" < "Python") # true and true
print(3 < 4 or "Hola" < "Python") # true or true

print(3 < 4 or ("Hola" > "Python" and 4 == 4)) # true or (false and true)
print(not(3 > 4))




