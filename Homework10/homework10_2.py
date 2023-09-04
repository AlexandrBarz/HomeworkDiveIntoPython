"""
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны
предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def check_triangle(self):
        if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b:
            if self.a == self.b == self.c:
                return 'Треугольник равносторонний'
            elif self.a == self.b or self.b == self.c or self.a == self.c:
                return 'Треугольник равнобедренный'
            else:
                return 'Треугольник разносторонний'
        else:
            return 'Треугольник не существует'


a = float(input('введите длину стороны a: '))
b = float(input('введите длину стороны b: '))
c = float(input('введите длину стороны c: '))
t = Triangle(a, b, c)
print(t.check_triangle())