class Carro:    
    def __init__(self,marca,modelo,cor,combustivel) -> None:
        pass
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel

        self.ligado = False
        self.velocidade = 0

        def ligar(self):
            if self.ligado:
                print("carro já está ligado, nada acontece")
            else:
                print(f"{self.modelo} ligado")
                self.ligado = True

        def desligar(self):
            if self.ligado:
                print(f"{self.modelo} desligado")
                self.ligado = False
            else:
                print("carro já está ligado, nada acontece")

        def acelerar(self):
            if self.ligado:
                self.velocidade += 1
                print(f"{self.velocidade}Km/h.")
            else:
                print("Não é possível acelerar, carro desligar")

        def frear(self):
            if self.ligado:
                self.velocidade -= 1
                print(f"{self.velocidade}Km/h.")
            else:
                print("Não é possível frear, carro desligar")
