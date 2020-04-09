class Pessoa:
    olhos = 2

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
    cesar.sobrenome = 'Santos'
    del cesar.filhos
    cesar.olhos = 1
    del cesar.olhos
    print(fernando.__dict__)
    print(cesar.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(cesar.olhos)
    print(fernando.olhos)
    print(id(Pessoa.olhos), id(cesar.olhos), id(fernando.olhos))




