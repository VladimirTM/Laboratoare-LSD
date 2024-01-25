from functools import reduce


def p1(multime):
    print("{", end=" ")
    reduce(lambda acc, element: print(element, end=" "), multime, 0)
    print("}")


# p1({1, 2, 3})


def p2(lista):
    return reduce(lambda multime, element: multime | {element[0]}, lista, set())


# print(p2([(1, 2), (3, 4)]))

def filter(functie, multime):
    return reduce(lambda multime, element: multime | {element} if functie(element) else multime, multime, set())


# print(filter(lambda x: x % 2 == 0, {1, 2, 3, 4}))

def partition(functie, multime):
    multimeAcceptata = reduce(lambda multime, element: multime | {element} if functie(element) else multime, multime,
                              set())
    multimeRespinsa = reduce(lambda multime, element: multime | {element} if not functie(element) else multime, multime,
                             set())
    return multimeAcceptata, multimeRespinsa


# print(partition(lambda x: x % 2 == 0, {1, 2, 3, 4}))

def p5(lista):
    reuniune = reduce(lambda multime, element: multime | element, lista, set())
    intersectie = reduce(lambda multime, element: multime & element, lista, {0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
    return reuniune, intersectie

# print(p5([{1, 2, 3}, {1, 2, 3, 4}, {3, 5, 6, 7}]))

def conversie(numar, multime = set()):
    if numar != 0:
        cifra = numar % 10
        multime = multime | {cifra}
        return conversie(numar // 10, multime)
    else:
        return multime

def p6(multime):
    reuniune =  reduce(lambda multime, element: multime | conversie(element), multime, set())
    intersectie = reduce(lambda  multime, element: multime & conversie(element), multime, {0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
    return reuniune,intersectie

print(p6({1234, 123, 127}))