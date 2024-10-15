import random
stouns_1 = []

""" ф-ция выбора случайного камня"""
def first_stoune(stouns):
    stouns_1 = random.choice(stouns)
    return stouns_1

""" номер случайного камня"""
stouns = []
for i in range (3, 21):
    stouns.append(i)

"""возврат 1 случайного камня"""
stoune_1 = first_stoune(stouns)
print('Первый камень: ', stoune_1)

stoune_2_1 = []
stoune_2_2 = []

for i in range(stoune_1):
    i += 1
    for j in range(stoune_1):
        j += 1
        if stoune_1 % (i + j) == 0 and i < j:
           stoune_2_1.append(i)
           stoune_2_1.append(j)
print(stoune_2_1)