"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте модуль fractions.
"""
import fractions
import math

num_1 = input("Введите первое число в формате дроби ***/***: ").split("/")
num_2 = input("Введите второе число в формате дроби ***/***: ").split("/")

lcm_fraction = math.lcm(int(num_1[1]), int(num_2[1]))
numerator_fraction1 = int(lcm_fraction / int(num_1[1]) * int(num_1[0]))
numerator_fraction2 = int(lcm_fraction / int(num_2[1]) * int(num_2[0]))
total_numerator_sum = numerator_fraction1 + numerator_fraction2
gcd_fraction_sum = math.gcd(total_numerator_sum, lcm_fraction)
print(f"Сумма дробей --> {num_1[0]}/{num_1[1]} + {num_2[0]}/{num_2[1]} = \
{str(int(total_numerator_sum / gcd_fraction_sum))}/{str(int(lcm_fraction / gcd_fraction_sum))}")

total_numerator_mult = int(num_1[0]) * int(num_2[0])
total_denominator_mult = int(num_1[1]) * int(num_2[1])
gcd_fraction_mult = math.gcd(total_numerator_mult, total_denominator_mult)
print(f"Произведение дробей -->  {num_1[0]}/{num_1[1]} * {num_2[0]}/{num_2[1]} = \
{str(int(total_numerator_mult / gcd_fraction_mult))}/{str(int(total_denominator_mult / gcd_fraction_mult))}")

print("=======================================================")
print("Проверка с помощью функции Fraction")
f1 = fractions.Fraction(int(num_1[0]), int(num_1[1]))
f2 = fractions.Fraction(int(num_2[0]), int(num_2[1]))
print(f"Сумма дробей --> {f1 + f2}")
print(f"Произведение дробей --> {f1 * f2}")