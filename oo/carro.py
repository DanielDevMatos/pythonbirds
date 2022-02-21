class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade <= 2 :
            self.velocidade = 0
        elif self.velocidade > 2:
            self.velocidade -= 2



class Direcao:
    def __init__(self):
        self.direcao = 'norte'

    def virar_esquerda(self):
        if self.direcao == 'norte':
            return self.direcao == 'oeste'
        elif self.direcao == 'oeste':
            return self.direcao == 'sul'
        elif self.direcao == 'sul':
            return self.direcao == 'leste'
        else:
            return self.direcao == 'norte'

    def virar_direita(self):
        if self.direcao == 'norte':
            return self.direcao == 'leste'
        elif self.direcao == 'leste':
            return self.direcao == 'sul'
        elif self.direcao == 'sul':
            return self.direcao == 'oeste'
        else:
            return self.direcao == 'norte'


class Carro:
    def __init_(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        print(self.motor.velocidade)

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calular_direcao(self):
        return self.direcao.direcao

    def girar_esquerda(self):
        print(self.direcao.virar_esquerda())

    def girar_direita(self, lado: str):
        print(self.direcao.virar_direita())



