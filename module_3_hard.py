data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])]

k = []

#функция, которая раскрывает все классы, кроме словаря
def new_(*args):
    for j in args:
        if j is None:
            continue
        if isinstance(j, int):
            k.append(j)
        elif isinstance(j, str):
            k.append(len(j))
        elif isinstance(j, (tuple, list)):
            new_(*j)
        elif isinstance(j, dict):
            new_1(**j)
        elif isinstance(j, set):
            new_(*j)
    return args

#функция, которая раскрывает класс словаря
def new_1(**kwargs):
    for key,value in kwargs.items():
        k.append(key)
        k.append(value)

    return k


def calculate_structure_sum(*args):
    for i in args:
        if isinstance(i, dict):
            new_1(**i)
        elif isinstance(i, (tuple, list)):
            new_(*i)
        elif isinstance(i, str):
            k.append(len(i))
        elif isinstance(i, int):
            k.append(i)
        elif isinstance(i, set):
            new_(*i)
    for i in k:
        if isinstance(i, str):
            k.append(len(i))
            k.remove(i)

    return sum(k)


result = calculate_structure_sum(data_structure)
print(result)






