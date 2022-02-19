class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome = None, idade = 35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa (nome = 'Renzo')
    daniel = Pessoa(renzo, nome ='Daniel')
    print(Pessoa.comprimentar(daniel))
    print(daniel.comprimentar())
    print(daniel.nome)
    print(daniel.idade)
    for filho in daniel.filhos:
        print(filho.nome)

    daniel.sobrenome = 'Matos'
    print(daniel.sobrenome)
    del daniel.filhos
    renzo.olhos = 1
    print(daniel.__dict__)
    print(renzo.__dict__)
    print(daniel.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(daniel.olhos), id(renzo.olhos))

