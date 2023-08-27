"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение дробей.
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