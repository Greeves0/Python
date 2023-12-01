"""
def factorielle(n):
    print("fact",n)
    if n==0:
        return 1
    else:
        return n*factorielle(n-1)
print(factorielle(5))
"""
"""
def genereDecrementation_it(n):
    if n==0:
        return []
    for n in range(n,-1,-1):
        lst.append(n)
        return lst

print(genereDecrementation_it(10))

def genereDecrementation_rec(n):
    if n==0:
        return []
    else:
        return [n]+genereDecrementation_rec(n-1)

print(genereDecrementation_rec(10))

def genereIncrementation_rec(n):
    if n==0:
        return []
    else:
        return genereDecrementation_rec(n-1)+[n]

print(genereIncrementation_rec(10))

def inverse_it(chaine):
    new=""
    for i in range(len(chaine),0,-1):
        new+=chaine[i]
    return new
"""
"""
def inverse_rec(chaine):
    if len(chaine)==0:
        return ""
    else:
        return inverse_rec(chaine[1:])+chaine[0]

chaine="hello"
print(chaine[1:])
print(chaine[0])
print(inverse_rec("hello"))
"""

def pgcd(a,b):
    if b==0:
        return a
    else:
        return pgcd(b,a%b)

print(pgcd(21,15))


def simplifie(a,b):
    k=pgcd(a,b)
    print(a,b,",le pgcd=",k)
    return a//k, b//k

print(simplifie(21,15))

def finobacci(n):
    if n<2:
        return n
    else:
        return finobacci(n-1)+finobacci(n-2)

print(finobacci(10))
