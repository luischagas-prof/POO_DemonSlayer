class Personagem:
    def __init__(self, nome, poder):
        self.nome = nome
        self.poder = poder

tanjiro = Personagem("Tanjiro", 50)
tanjiro.poder = -10  # valor errado!
print(tanjiro.poder)

# Aplicando Encapsulamento
# Solução 1: Usar propriedades (getters e setters) 
class Personagem:
    def __init__(self, nome, poder):
        self.__nome = nome
        self.__poder = poder

    def get_poder(self):
        return self.__poder

    def set_poder(self, novo_poder):
        if novo_poder > 0:
            self.__poder = novo_poder

tanjiro = Personagem("Tanjiro", 50)
tanjiro.set_poder(80)
print(tanjiro.get_poder())


# Aplicando Abstração
from abc import ABC, abstractmethod

class Espadachim(ABC):
    @abstractmethod
    def atacar(self):
        pass

class Tanjiro(Espadachim):
    def atacar(self):
        print("Tanjiro usa o Golpe da Água!")

class Zenitsu(Espadachim):
    def atacar(self):
        print("Zenitsu usa o Trovão Veloz!")

tanjiro = Tanjiro()
zenitsu = Zenitsu()
tanjiro.atacar()
zenitsu.atacar()
print(tanjiro.get_poder())  # Saída: 50
print(zenitsu.get_poder())  # Saída: 70
