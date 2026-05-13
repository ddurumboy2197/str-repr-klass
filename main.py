from abc import ABC, abstractmethod

class Geometriya(ABC):
    @abstractmethod
    def yuza(self):
        pass

class Doira(Geometriya):
    def __init__(self, radius):
        self.radius = radius

    def yuza(self):
        return 3.14 * self.radius ** 2

class Kvadrat(Geometriya):
    def __init__(self, tomon):
        self.tomon = tomon

    def yuza(self):
        return self.tomon ** 2

# Test
doira = Doira(5)
print(doira.yuza())

kvadrat = Kvadrat(4)
print(kvadrat.yuza())
