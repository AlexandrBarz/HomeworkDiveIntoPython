"""
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег
"""

def tax(summ):
    print("С вас сняли налог на богатство", summ * 0.1)
    summ -= summ * 0.1
    return summ

def add_money(summ, count_add):
    summ_add = int(input("Сумма: "))
    if summ_add % 50 == 0:
        summ += summ_add
        count_add += 1
        if count_add % 3 == 0:
            summ *= 1.03
            return summ
    else:
        print("Введена некорректная сумма (не кратна 50)")
    return summ

def withdraw_money(summ, count_out):
    summ_out = int(input("Сумма: "))
    comission = summ_out * 0.015
    if comission < 30:
        comission = 30
    elif comission > 600:
        comission = 600
    if summ_out + comission > summ:
        print("Недостаточно средств")
        return summ
    else:
        if summ_out % 50 == 0:
            summ -= summ_out + comission
            count_out += 1
            if count_out % 3 == 0:
                summ *= 1.03
            return summ
        else:
            print("Введена некорректная сумма")
            return summ

summ = 0
count_add = 0
count_out = 0
while True:
    if summ > 5_000_000:
        summ = tax(summ)
    action = input("Действие: ")
    if action == "q":
        print("Выходим из банкомата")
        print("Сумма: ", summ)
        break
    elif action == "a":
        summ = add_money(summ, count_add)
    elif action == "o":
        summ = withdraw_money(summ, count_out)
    elif action == "b":
        print(f"Ваш баланс: {summ}")
    print(f"Сумма: {summ}")