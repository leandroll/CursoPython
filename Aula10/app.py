
#set-------------------------------------------
frutas = {"abacaxi", "laranja", "maca"}
print(frutas)
frutas.add("pera")
print(frutas)
frutas.remove("maca")
print(frutas)
print("------------------------------")
var_set_mista = {True, "Leandro", 78}
print(var_set_mista)

#Dicionário-------------------------------------

dicionario = {
    1:"Leandro",
    2:"Renata",
    3:"Anna Claudia"
}

print(dicionario[3])
print(dicionario.get(3))
print(dicionario.get(5,"valor padrão caso a chave informada não exista"))
print(len(dicionario))