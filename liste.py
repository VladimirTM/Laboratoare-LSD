from functools import reduce


def p1(lista):
    if len(lista) != 0:
        head = lista[0]
        tail = lista[1:]
        if head % 2 == 0:
            print(head)
        return p1(lista=tail)


# p1([1, 2, 3, 4])


def p2(lista):
    if len(lista) != 0:
        head = lista[0]
        tail = lista[1:]
        if len(head) < 3:
            print(head)
        return p2(lista=tail)


# p2(["abc", "a", "adadaddadsa", "da"])


def p4(lista):
    lista.sort(key=lambda x: x % 10)
    return lista


# print(p4([12, 34, 19, 32, 76]))


def p5(lista):
    return reduce(lambda produs, element: produs * element, lista, 1)


# print(p5([1, 2, 3, 4]))

def p6(lista):
    lista = list(map(lambda x: x ** 3, lista))
    return lista


# print(p6([1, 2, 3, 4, 5]))

def prim(numar, d=2):
    if numar == 1:
        return 0
    if d > numar // 2:
        return 1
    else:
        if numar % d == 0:
            return 0
        d = d + 1
        return prim(numar, d)


def p7(lista):
    lista = list(filter(prim, lista))
    return lista


# print(p7([1, 2, 3, 4, 5, 43, 44]))

def p8a(numar, lista=[]):
    if numar != 0:
        cifra = numar % 10
        if cifra % 2 == 0:
            lista.append(cifra)
        return p8a(numar // 10, lista)
    else:
        lista.sort(reverse=True)
        return lista


# print(p8a(1285332457))

def p8b(numar, functie, lista=[]):
    if numar != 0:
        cifra = numar % 10
        if functie(cifra):
            lista.append(cifra)
        return p8b(numar // 10, functie, lista)
    else:
        return lista


# print(p8b(23442256, prim))

def p8c(lista, functie):
    listaAcceptata = list(filter(functie, lista))
    return reduce(lambda numar, cifra: numar * 10 + cifra, listaAcceptata, 0)


# print(p8c([1, 2, 3, 4, 5], prim))

def fromto(a, b, lista=[]):
    if a > b:
        return lista
    else:
        lista.append(a)
        return fromto(a + 1, b, lista)


def p9(a, b, d):
    return list(filter(lambda x: x % d == 0, fromto(a, b)))


# print(p9(1, 40, 2))

def nth(lista, n):
    return lista[n - 1]


def firstn(lista, n, i=1, listaNoua=[]):
    if i <= n:
        listaNoua.append(nth(lista, i))
        return firstn(lista, n, i + 1, listaNoua)
    else:
        return listaNoua


# print(firstn([1,2,3,4,5,6,7,8,9,10], 5))

def filter(functie, lista):
    return reduce(lambda lista, element: lista + [element] if functie(element) else lista, lista, list())


# print(filter(prim, [1, 2, 3, 4, 5, 6]))

def exists(lista, functie):
    listaNoua = filter(functie, lista)
    if len(listaNoua) != 0:
        return True
    else:
        return False


# print(exists([1, 4, 9], prim))

def countif(lista, functie):
    return reduce(lambda contor, element: contor + 1 if functie(element) else contor, lista, 0)


# print(countif([1, 4, 9, 2], prim))

def sumif(lista, functie):
    return reduce(lambda suma, element: suma + element if functie(element) else suma, lista, 0)


# print(sumif([1, 4, 9, 2, 4, 5], prim))

def split(lista):
    lista1 = reduce(lambda lista, element: lista + [element[0]], lista, list())
    lista2 = reduce(lambda lista, element: lista + [element[1]], lista, list())
    return lista1, lista2


# print(split([(1, 2), (3, 4), (5, 6)]))

def combine(lista1, lista2, listaNoua=[]):
    if len(lista1) != 0 and len(lista2) != 0:
        a = lista1[0]
        b = lista2[0]
        tail1 = lista1[1:]
        tail2 = lista2[1:]
        listaNoua.append((a, b))
        return combine(tail1, tail2, listaNoua)
    else:
        return listaNoua


# print(combine([1,3,5], [2,4,6]))

def partition(functie, lista):
    listaAcceptata = reduce(lambda lista, element: lista + [element] if functie(element) else lista, lista, list())
    listaRefuzata = reduce(lambda lista, element: lista + [element] if not functie(element) else lista, lista, list())
    return listaAcceptata, listaRefuzata


# print(partition (lambda x : x >= 5, [4,6,7,5,4,8,9]))

def p15(lista):
    return reduce(lambda numar, element: numar * 10 + element, lista, 0)


# print(p15([1,2,3]))

def p16(lista, listaNoua=[], anterior=None):
    if len(lista) != 0:
        head = lista[0]
        tail = lista[1:]
        if head != anterior:
            listaNoua.append(head)
        return p16(tail, listaNoua, head)
    else:
        return listaNoua


# print(p16([1,2,3,4,5, 5, 1, 2, 4, 2, 2]))

def p17(lista1, lista2):
    if len(lista1) > len(lista2):
        return 1
    elif len(lista1) < len(lista2):
        return -1
    else:
        if len(lista1) != 0:
            head1 = lista1[0]
            head2 = lista2[0]
            tail1 = lista1[1:]
            tail2 = lista2[1:]
            if head1 > head2:
                return 1
            elif head1 < head2:
                return -1
            return p17(tail1, tail2)
        else:
            return 0


# print(p17([1, 2, 3, 4, 6], [1, 2, 3, 4, 8]))

def p18(lista1, lista2, listaFinala=[]):
    if len(lista1) != 0 and len(lista2) != 0:
        head1 = lista1[0]
        head2 = lista2[0]
        tail1 = lista1[1:]
        tail2 = lista2[1:]
        if head1 < head2:
            listaFinala.append(head1)
            return p18(tail1, lista2, listaFinala)
        elif head1 > head2:
            listaFinala.append(head2)
            return p18(lista1, tail2, listaFinala)
        else:
            listaFinala.append(head1)
            return p18(tail1, tail2, listaFinala)
    elif len(lista1) != 0:
        head = lista1[0]
        tail = lista1[1:]
        listaFinala.append(head)
        return p18(tail, lista2, listaFinala)
    elif len(lista2) != 0:
        head = lista2[0]
        tail = lista2[1:]
        listaFinala.append(head)
        return p18(lista1, tail, listaFinala)
    else:
        return listaFinala


# print(p18([1, 2, 3, 4, 5, 7], [1, 2, 3, 4, 8, 9]))

def p19(lista, lista1=[], lista2=[], i=0):
    if i != len(lista):
        if i % 2 == 0:
            lista1.append(lista[i])
        else:
            lista2.append(lista[i])
        return p19(lista, lista1, lista2, i + 1)
    else:
        return lista1, lista2


# print(p19([1, 2, 3, 4, 5, 6, 7]))

def p20(lista):
    split = p19(lista, [], [])
    lista1, lista2 = split
    if len(lista1) == 1 or len(lista2) == 1:
        if len(lista1) == 2 and len(lista2) == 1:
            lista1 = p18([lista1[0]], [lista1[1]], [])
        elif len(lista1) == 1 and len(lista2) == 2:
            lista2 = p18([lista2[0]], [lista2[1]], [])
        return p18(lista1, lista2, [])
    return p18(p20(lista1), p20(lista2), [])

# print(p20([2, 1, 3, 4, 6, 5, 7, 8, 9, 3, -4]))
