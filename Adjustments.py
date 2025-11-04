class Tanjiro:
    def atacar(self):
        print("Tanjiro usa o Golpe da Água!")

class Zenitsu:
    def atacar(self):
        print("Zenitsu usa o Trovão Veloz!")

class Inosuke:
    def atacar(self):
        print("Inosuke usa as Garras da Fera!")

# Criando e chamando
tanjiro = Tanjiro()
zenitsu = Zenitsu()
inosuke = Inosuke()

tanjiro.atacar()
zenitsu.atacar()
inosuke.atacar()

# =========================================================================== #
# Problema:
# Cada classe repete o mesmo método atacar()

# Se quisermos garantir que todo personagem tenha o método atacar(),
# temos que verificar manualmente em cada classe

# Difícil de manter quando o projeto cresce (ex: 20 personagens diferentes)