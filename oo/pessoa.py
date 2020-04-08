class Pessoa:
    def __init__(self, *filhos, nome=None, idade=43):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    fernando = Pessoa(nome='Fernando')
    cesar = Pessoa(fernando, nome='Cesar')
    print(Pessoa.cumprimentar(cesar))
    print(id(cesar))
    print(cesar.cumprimentar())
    print(cesar.nome)
    print(cesar.idade)
    for filho in cesar.filhos:
        print(filho.nome)




