try:
    dividendo = int(input("Digite o dividendo: "))
    print(dividendo)
    divisor = int(input("Digite o divisor: "))
    print(divisor)
    print(f"O resultado da divisão é {dividendo / divisor}")
except ZeroDivisionError:
    print("\nnão é possivel um numero ser dividido por 0")
except ValueError:
    print("\nDigite um valor válido.")
except:
    print("Erro inesperado")
finally:
    print("\nFim da operação...")