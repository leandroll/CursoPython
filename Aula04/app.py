minha_string = "qualquer texto"

print(type(minha_string))
print(f"esse é {minha_string} concatenado.")
print(minha_string.upper())

minha_string_maiuscula =  "QUALQUER TEXTO"

print(minha_string_maiuscula.lower())
print(minha_string.capitalize())
print(minha_string.isupper())
print(minha_string.islower())

minha_string_espacos = " qualquer texto "

print(minha_string_espacos.strip())
print(minha_string.replace("qualquer","meu"))
print(minha_string.replace("u","U"))
print(minha_string.replace("u","U",1))
print(len(minha_string))
print(minha_string[2])
print(minha_string[-4:-1])
print(minha_string[0:-8])
print(minha_string.index("texto"))

x = "texto" in minha_string

print(x)

minha_string_multexto = """
1 - \"texto\"
2 - \"texto\"
3 - \"texto\"
"""

print(minha_string_multexto)

minha_string_multexto2 = "1 - texto, \n2 - texto, \n3 - texto."

print(minha_string_multexto2)

