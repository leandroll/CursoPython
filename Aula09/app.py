i = 1

while i < 10:
    print(i)
    i += 1

print(f"Terminou o while...terminou com {i}")

print("-----------------------------------------------\n")

pessoas = ["Leandro", "Renata", "Anna Claudia"]

for itens in pessoas:
    print(itens)

print("-----------------------------------------------\n")
nome = "Leandro"
for itens in nome:
    print(itens)

print("-----------------------------------------------\n")
for index in range(20):
    print(index)

print("-----------------------------------------------\n")
for index in range(5, 20):
    print(index)

print("-----------------------------------------------\n")
for index in range(1, 10, 2):
    print(index)

print("-----------------------------------------------\n")
for index in range(len(pessoas)):
    print(index)

print("-----------------------------------------------\n")
for index in range(len(pessoas)):
    print(pessoas[index], index)

print("-----------------------------------------------\n")
for index in range(5):
    if index == 0:
        print(f"primeira linha - {index}")
    else:
        print(f"Outrs linhas - {index}")

print("-----------------------------------------------\n")
matrix_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
for linhas  in matrix_numeros:
        print(f"------------")
        for colunas in linhas:
            print(colunas)


print("tabuada multiplicação -----------------------------------------------\n")
numerador = int(input("Qual o número que quer que se faça a tabuada: "))
print("\n")
for i in range(1,11):
    r = i*numerador
    print("{} x {} = {}".format(numerador,i,r))
    i = i+1
