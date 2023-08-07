"""
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.
"""

data = {"Вася": ("Палатка", "Котелок", "Спички", "Шашлык"),
        "Петя": ("Палатка", "Котелок", "Топор"),
        "Саша": ("Палатка", "Котелок", "Топор", "Спирт"),
        }

lst = []
for k, v in data.items():
    lst.append(set(v))

for i in range(len(lst) - 2):
    res_all = lst[i].intersection(lst[i + 1])
    res_all = res_all.intersection(lst[i + 2])
print(f"Вещи, которые взяли все друзья:\n{res_all}")

for i in range(len(lst) - 2):
    res_unic = lst[i].symmetric_difference(lst[i + 1])
    res_unic_1 = res_unic.symmetric_difference(lst[i + 2]) - res_all
print(f"Вещи, которые есть только у одного из друзей:\n{res_unic_1}")

for friends in data:
    st = set(data[friends])
    set_f = set()
    for f in data:
        if friends != f:
            set_f = set_f.intersection(set(data[f])) if set_f else set(data[f])
    if set_f:
        things = set_f.difference(st)
        if things:
            print(f"Только {friends} не имеет:\n{things}")