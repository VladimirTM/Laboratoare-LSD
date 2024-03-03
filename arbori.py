arbore_binar = {"value": 2, "left":
    {
        "value": 7, "left": None, "right":
        {
            "value": 6, "left":
            {
                "value": 5, "left": None, "right": None
            }, "right":
            {
                "value": 11, "left": None, "right": None
            },
        },
    }, "right":
                    {
                        "value": 4, "left": None, "right": None
                    }
                }
arbore_binar_cautare = {"value": 4, "left":
    {"value": 2, "left": {"value": 1, "left": None, "right": None}, "right": {"value": 3, "left": None, "right": None},
     }, "right":
                            {"value": 7, "left": None, "right": None}
                        }

value = "value"
left = "left"
right = "right"


def p1(arbore):
    if arbore == None:
        return []
    elif arbore[left] == None and arbore[right] == None:
        return [arbore[value]]
    else:
        return p1(arbore[left]) + p1(arbore[right])


# print(p1(arbore_binar))

def rsd(arbore):
    if arbore != None:
        return [arbore[value]] + rsd(arbore[left]) + rsd(arbore[right])
    else:
        return []


def srd(arbore):
    if arbore != None:
        return srd(arbore[left]) + [arbore[value]] + srd(arbore[right])
    else:
        return []


def sdr(arbore):
    if arbore != None:
        return sdr(arbore[left]) + sdr(arbore[right]) + [arbore[value]]
    else:
        return []


# print(rsd(arbore_binar))
# print(srd(arbore_binar))
# print(sdr(arbore_binar))

def p3(arbore, functie):
    if arbore != None:
        if arbore[left] == None and arbore[right] == None:
            arbore[value] = functie(arbore[value])
            print(arbore[value], end=" ")
        else:
            arbore[value] = functie(arbore[value])
            print(arbore[value], end=" ")
            p3(arbore[left], functie)
            # Se multa aici pentru parcurgere in inordine
            # arbore[value] = functie(arbore[value])
            # print(arbore[value], end=" ")
            p3(arbore[right], functie)
            # Se multa aici pentru parcurgere in postordine
            # arbore[value] = functie(arbore[value])
            # print(arbore[value], end=" ")


# p3(arbore_binar, lambda x: x * 2)

def p4(arbore):
    if arbore != None:
        aux = arbore[left]
        arbore[left] = arbore[right]
        arbore[right] = aux
        p4(arbore[left])
        p4(arbore[right])
    return arbore


# print(p4(arbore_binar))

def p5(arbore, functie):
    if arbore != None:
        if arbore[left] == None and arbore[right] == None:
            return functie(arbore[value])
        else:
            return functie(arbore[value]) or p5(arbore[left], functie) or p5(arbore[right], functie)
    else:
        return False


# print(p5(arbore_binar, lambda x: x % 2 == 0))


def p6(arbore, functie):
    if arbore != None:
        if arbore[left] == None and arbore[right] == None:
            return functie(arbore[value])
        else:
            return functie(arbore[value]) and p6(arbore[left], functie) and p6(arbore[right], functie)
    else:
        return True


# print(p6(arbore_binar, lambda x: x % 2 == 0))

def max(a, b):
    return a if a > b else b


def p8(arbore):
    if arbore != None:
        if arbore[left] == None and arbore[right] == None:
            return 0
        else:
            return 1 + max(p8(arbore[left]), p8(arbore[right]))
    else:
        return 0


# print(p8(arbore_binar))

def p9(arbore):
    if arbore != None:
        if arbore[left] == None and arbore[right] == None:
            return arbore[value]
        else:
            return bool((arbore[value] > arbore[left][value]) and (arbore[value] < arbore[right][value]) and p9(
                arbore[left]) and p9(arbore[right]))


# print(p9(arbore_binar))

def p10(arbore, x):
    if arbore != None:
        valoare = arbore[value]
        if valoare == x:
            return True
        elif valoare < x:
            return p10(arbore[right], x)
        else:
            return p10(arbore[left], x)
    return False


# print(p10(arbore_binar_cautare, 3))

def p11(arbore, x):
    if p10(arbore, x) == False:
        if arbore == None:
            arbore = {value: x, left: None, right: None}
        else:
            valoare = arbore[value]
            if valoare < x:
                arbore[left] = p11(arbore[right], x)
            else:
                arbore[right] = p11(arbore[left], x)
    return arbore


# print(p11(arbore_binar_cautare, 5))

def p12(arbore, n):
    return srd(arbore)[n - 1]

# print(p12(arbore_binar_cautare, 5))
