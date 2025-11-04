from abc import ABC, abstractmethod

# Classe base abstrata
class Espadachim(ABC):
    @abstractmethod
    def atacar(self):
        pass

# Classes concretas
class Tanjiro(Espadachim):
    def atacar(self):
        print("Tanjiro usa o Golpe da Água!")

class Zenitsu(Espadachim):
    def atacar(self):
        print("Zenitsu usa o Trovão Veloz!")

class Inosuke(Espadachim):
    def atacar(self):
        print("Inosuke usa as Garras da Fera!")

# Lista genérica de espadachins
equipe = [Tanjiro(), Zenitsu(), Inosuke()]

for personagem in equipe:
    personagem.atacar()

# =========================================================================== #
# Agora:
# Todas as classes herdam da mesma base (Espadachim)

# O método atacar() é obrigatório

# Podemos tratar todos os objetos de forma genérica (loop for)

# Se alguém esquecer de implementar atacar(), o Python gera erro automaticamente


# 💬 Em resumo:
# Situação	                Antes	                            Depois
# Repetição de código	    Alta (cada classe isolada)	        Mínima (herança + abstração)
# Manutenção	            Difícil	                            Fácil e centralizada
# Validação	                Manual	                            Automática (erro se faltar método abstrato)

# Analogia pra lousa:

# É como criar um “contrato” para os personagens:
# quem quiser ser um Espadachim, precisa obrigatoriamente saber atacar.