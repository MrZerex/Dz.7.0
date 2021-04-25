class Kletka():
    def __init__(self, klet, rows):
        self.klet = klet
        self.rows = rows

    def __add__(self, other):
        return self.klet + other.klet

    def __sub__(self, other):
        if self.klet < other.klet:
            return 'Разность произвести невозможно'
        else:
            return self.klet - other.klet

    def __mul__(self, other):
        return self.klet * other.klet

    def __truediv__(self, other):
        return self.klet // other.klet

    def make_order(self):
        rez_1 = self.klet // self.rows
        rez_2 = self.klet % self.rows
        list = ['*' * self.rows for _ in range(rez_1)]
        return '\n'.join(list) + '\n' + '*' * (rez_2)

a = Kletka(8, 3)
b = Kletka(7, 3)
print(f'Сумма клеток: {a + b}')
print(f'Разность клеток: {a - b}')
print(f'Произведение клеток: {a * b}')
print(f'Деление клеток: {a / b}\n')
print(a.make_order(), '\n')
print(b.make_order())
