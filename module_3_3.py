"""1. Функция с параметрами по умолчанию"""

def print_params(a, b, c):
    print(a, b, c)

a = '1'
b = 'строка'
c = 'True'

print_params(a, b, c)

#print_params() - вызов не возможен, кол-во параметров должно соответст. кол-ву по умолчанию
#print_params(a, b) - аналогично вышесказанному
#print_params(a, 25, c)
#print_params(a, b, [1,2,3])

"""2.Распаковка параметров"""

def print_params(**kwargs):
    print(kwargs)

values_list = [True, 25.4, 'list']
values_dict = [a, b, c]
dict_ = dict(zip((values_dict), values_list))

print_params(**dict_)

# def print_params(*args):
#     print(*args)
# a = 1
# b = 'строка'
# c = True
#
# print_params(a, b, c)
# print_params(a)
# print_params()
# print_params(a,b)
# print_params(c)


"""3.Распаковка + отдельные параметры"""
values_list_2 = [54.32, 'Строка']


def print_params(*args):
    print(*args)

print_params(*values_list_2, 42)
