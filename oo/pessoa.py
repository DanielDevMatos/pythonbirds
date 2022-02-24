class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome = None, idade = 35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def comprimentar(self):
        return f'Ola, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def comprimentar(self):
        comprimentar_classe = super().comprimentar()
        return f'{comprimentar_classe}, Aperto de mão'

class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    renzo = Mutante(nome = 'Renzo')
    daniel = Homem (renzo, nome ='Daniel')
    print(Pessoa.comprimentar(daniel))
    print(daniel.comprimentar())
    print(daniel.nome)
    print(daniel.idade)
    for filho in daniel.filhos:
        print(filho.nome)

    daniel.sobrenome = 'Matos'
    print(daniel.sobrenome)
    del daniel.filhos
    print(daniel.__dict__)
    print(renzo.__dict__)
    print(daniel.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(daniel.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), daniel.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(), daniel.nome_e_atributos_de_classes())
    pessoa = Pessoa('anonima')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(renzo.olhos)
    print(daniel.comprimentar())
    print(renzo.comprimentar())
