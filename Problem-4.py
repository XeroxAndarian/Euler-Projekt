import math

def prezrcali(niz):
    '''Zrcali niz'''
    # print(niz[-1])
    # print(niz[1])
    # print(niz[:-1])
    # print(niz[1:])
    # print(niz[1:-1])
    # print(niz[:])
    # print(niz[::])
    return niz[::-1]

def je_palindrom(n):
    '''Prever, ali število n je palindrom ali ne'''
    return (str(n) == prezrcali(str(n)))

def palindrom_trimestnih():
    palindromi = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if je_palindrom((i * j)):
                palindromi.append(i * j)
    return palindromi

def maksimalna_kombinacija_palindroma():
    return max(palindrom_trimestnih())
    
