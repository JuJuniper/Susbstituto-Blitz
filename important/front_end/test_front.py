from abc import ABC, abstractmethod
from unittest import removeResult


class Front(ABC):

    @abstractmethod
    def getUser(self, id):
        pass

    @abstractmethod
    def printUser(self):
        pass

    @abstractmethod
    def getElo(self):
        pass


class frontTeste(Front):

    def getUser(self, id):
        return super().getUser(id)

    def printUser(self):
        print("usuario qqr")

    def getElo(self):
        return super().getElo()

class TesteFront_end():

    def printELO():
        return

    def printSummoner():
        return
