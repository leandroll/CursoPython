familia = ["Leandro", "Renata", "Anna Claudia"]
print(familia)

familia[2] = "uiuiui"
print(familia)

print(familia[0])
print(familia[-2])

numeros = ([10,20,30,40,50])
  
print(numeros)   

print(numeros[0] + numeros[4])

print(numeros[1+2])

familia.extend(["Marri", "Grigrilo"])
print(familia)

familia.append("Nenem")
print(familia)

familia.insert(6,"Mingau")
familia.insert(7,"Micuminho")
print(familia)

familia.pop()
familia.pop()
print(familia)

familia.remove("Nenem")
familia[2] = "Anna Claudia"
print(familia)

print(familia.index("Anna Claudia"))
print(familia.count("Leandro"))

familia.sort()
print(familia)

familia.sort()
print(familia)
familia.reverse()
print(familia)

numeros.reverse()
print(numeros)

familia2 = familia
print(familia2)
familia.remove("Leandro")
print(familia2)

familia3 = familia2.copy()
print(familia3)
familia2.remove("Renata")
print(familia2)
print(familia3)

familia3.clear()
print(familia3)

cordenada_tuple = (-10,-20,-34)
print(cordenada_tuple)
print(cordenada_tuple[1])
print(cordenada_tuple.count(-20))