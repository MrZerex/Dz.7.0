mat_1 = [[14, 13, 12], [15, 17, 88], [32, 17, 45]]
mat_2 = [[51, 60, 9], [88, 1, 22], [45, 43, 10]]
mat_0 = [[], [], []]
class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        strok = '\n'.join(map(str, self.matr))
        return strok

    def __add__(self, other):
        for el in range(len(self.matr)):
            for el_1 in range(len(self.matr[0])):
                mat_0[el].append(self.matr[el][el_1] + other.matr[el][el_1])
        resultat = '\n'.join(map(str, mat_0))
        return resultat

matrx_1 = Matrix(mat_1)
matrx_2 = Matrix(mat_2)
print(f'Первая матрица:\n{matrx_1}')
print(f'Вторая матрица:\n{matrx_2}')
print(f'Сложение матриц:\n{matrx_1 + matrx_2}')