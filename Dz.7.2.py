from abc import ABC, abstractmethod

class Shmot(ABC):
    def __init__(self, size):
        self.size = size

    @property
    @abstractmethod
    def rezultat(self):
        pass

    def __add__(self, other):
        return f'Всего ткани необходимо: {round(self.rezultat + other.rezultat)}'

class Palto(Shmot):
    @property
    def rezultat(self):
        rez = (self.size/6.5 + 0.5 )
        return rez

class Kostum(Shmot):
    @property
    def rezultat(self):
        rez = (self.size / 6.5 + 0.5)
        return rez

def data():
    while True:
        try:
            size_plt = int(input('Введите размер для пальто: '))
            size_kst = int(input('Введите рост для костюма: '))
            if size_plt < 0 or size_kst < 0:
                print('Необходимо ввести целое положительное число!')
                continue
            break
        except ValueError:
            print('Необходимо ввести целое число!')
            continue
    plt = Palto(size_plt)
    kst = Kostum(size_kst)
    print(plt + kst)

data()