nome = input("Seu nome: ")

print(f"Olá {nome}")

idade = int(input("Qual sua idade ? : "))

print(f"Ola {nome}! parabéns pelos {idade} anos !")

from datetime import date

ano_atual = int(date.today().year)

print(f"Ano atual {ano_atual}")

nascimento = ano_atual - idade

print(f"Legal {nome}, você nasceu em {nascimento}")