tenho_sede = True
tenho_fome = False
dieta = False

#if tenho_sede:
#    print("beber água")
#else:
#    print("não beber água\n\n")

if tenho_sede and tenho_fome:
    print("fazer sanduiche e coca")
elif tenho_sede and not (tenho_fome):
    if dieta:
        print("beber agua")
    else:
        print("tomar coquinha")
elif not(tenho_sede) and tenho_fome:
    print("fazer sanduiche")
else:
    print("ver netflix")

print("-----------------------------------------\n")
nome01 = "Leandro"
nome02 = "Renata"
nome03 = "Anna Claudia"

if(nome01 == nome02):
    print("Os nomes são iguais")
elif(nome01 != nome02):
    print("Os nome são diferente")

print("-----------------------------------------\n")
if(nome03 == "Anna Claudia"):
    print("Olá uiuiui")
else:
    print("nome desconhecido")



    