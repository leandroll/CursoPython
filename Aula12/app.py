'''
arquivos modos:
r  - Leitura
a  - Append / Incrementar
w  - Escrita(limpa o arquivo, escreve os novos dados ou cria um novo arqquivo com dados se digitados)
x  - Criar Arquivo mesmo d0 W
r+ - Leitura e Escrita

'''

try:
    arquivo = open("Aula12/teste.txt","r")

    print(f"{arquivo.readable()}\n")
    print(arquivo.read())
    
    arquivo.close()

    print("\n------------------------------1")
    arquivo = open("Aula12/teste.txt","r")
    
    print(arquivo.readline())
    print(arquivo.readline())
    print(arquivo.readline())
    print(arquivo.readline())

    arquivo.close()
    
    print("\n------------------------------2")
    arquivo = open("Aula12/teste.txt","r")
    
    lista = arquivo.readlines()
    print(lista)
 
    arquivo.close()

    print("\n------------------------------3")
    arquivo = open("Aula12/teste.txt","a")
    arquivo.writelines("\nFotran")
    arquivo.close()

    arquivo = open("Aula12/teste.txt","r")
    print(arquivo.read())
    arquivo.close()

    print("\n------------------------------4")
    arquivo = open("Aula12/teste2.txt","w")
    arquivo.writelines("Fotran\n")
    arquivo.writelines("Cobol\n")
    arquivo.close()

    arquivo = open("Aula12/teste2.txt","r")
    print(arquivo.read())
    arquivo.close()

    print("\n------------------------------4")
    arquivo = open("Aula12/teste3.txt","x")
    arquivo.writelines("Python\n")
    arquivo.close()

    arquivo = open("Aula12/teste3.txt","r")
    print(arquivo.read())
    arquivo.close()

    print("\n------------------------------5")
    import os
    if(os.path.exists("Aula12/teste3.txt")):
        os.remove("Aula12/teste3.txt")

    print("\n------------------------------5")
    import os.path
    if(not os.path.exists("Aula12/teste")):
        os.makedirs("Aula12/teste")
    if(os.path.exists("Aula12/teste")):
        os.removedirs("Aula12/teste")

finally:
    print("fechar arquivo")
    arquivo.close()