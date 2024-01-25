from functools import reduce


def p1(lista, dictionar=dict()):
    if len(lista) != 0:
        key, value = lista[0]
        tail = lista[1:]
        if key in dictionar:
            dictionar[key] = dictionar[key] + value
        else:
            dictionar[key] = value
        return p1(tail, dictionar)
    else:
        return dictionar


# print(p1([('a', 7), ('b', 5), ('c', 2), ('a', 3), ('b', 3)]))

def conversieSD(string, dictionar):
    if len(string) != 0:
        caracter = string[0]
        rest = string[1:]
        if caracter in dictionar:
            dictionar[caracter] = dictionar[caracter] + 1
        else:
            dictionar[caracter] = 1
        return conversie(rest, dictionar)
    else:
        return dictionar


def p2(lista):
    return reduce(lambda dictionar, element: conversieSD(element, dictionar), lista, dict())


# print(p2(["aaa", "bbb", "aabbb"]))

def conversieD(element, dictionar, functie):
    key, value = element
    if functie(value):
        dictionar[key] = value
    return dictionar


def filter(dictionar, functie):
    items = list(dictionar.items())
    return reduce(lambda dictionar, element: conversieD(element, dictionar, functie), items, dict())


# print(filter({'a': 5, 'b': 7, 'c': 1}, lambda x: x >= 5))

def exists(dictionar, functie):
    values = list(dictionar.values())
    return reduce(lambda valoareAdevar, element: valoareAdevar or functie(element), values, False)


# print(exists({'a': 5, 'b': 7, 'c': 1}, lambda x: x >= 5))


def for_all(dictionar, functie):
    values = list(dictionar.values())
    return reduce(lambda valoareAdevar, element: valoareAdevar and functie(element), values, True)


# print(for_all({'a': 5, 'b': 7, 'c': 1}, lambda x: x >= 5))

def aplicareF(element, dictionar, functie):
    key, value = element
    dictionar[key] = functie(value)
    return dictionar


def map(dictionar, functie):
    items = list(dictionar.items())
    return reduce(lambda dictionar, element: aplicareF(element, dictionar, functie), items, dict())


# print(map({'a': 5, 'b': 7, 'c': 6}, lambda x: x + 1))

def p6(dictionar, lista):
    items = list(dictionar.items())
    return reduce(lambda multime, element: multime | {element[1]} if element[0] in lista else multime, items, set())


# print(p6({'aa': 5, 'bb': 7, 'ca': 6}, ['aa', 'bb', 'c']))

def max(a, b):
    return a if a > b else b


def p7(dictionar, functie):
    items = list(dictionar.items())
    return reduce(lambda maxim, element: functie(element) if functie(element) > maxim else maxim, items,
                  functie(items[0]))

# print(p7({1: 2, 4: 3, 5: 6, 1: 15, 3: 4}, lambda pereche: pereche[0] + pereche[1]))
