"""
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или
из документации к языку.
"""

import re
from collections import Counter

text = \
    'Есть такая легенда - о птице, что поёт лишь один раз за всю жизнь, но зато прекраснее всех на свете.\
    Однажды она покидает свое гнездо и летит искать куст терновника и не успокоится, пока не найдёт.\
    Среди колючих ветвей запевает она песню и бросается грудью на самый длинный, самый острый шип.\
    И, возвышаясь над несказанной мукой, так поет, умирая, что этой ликующей песне позавидовали бы и жаворонок, и соловей.\
    Единственная, несравненная песнь, и достаётся она ценою жизни.\
    Но весь мир замирает, прислушиваясь, и сам Бог улыбается в небесах.\
    Ибо все лучшее покупается лишь ценою великого страдания.\
    По крайней мере, так говорит легенда.'

word_list = re.findall(r'\b\w+\b', text.lower())
print("Количество слов в строке:", len(word_list))
dict = {}
for word_1 in word_list:
    count = 0
    for word_2 in word_list:
        if word_1 == word_2:
            count += 1
    dict[word_1] = count
    if count == 1:
        del dict[word_1]
print(f"Кол-во повторяющих слов: {len(dict)}")
print(f"Список 10 самых частых повторений:\n{Counter(dict).most_common(10)}")