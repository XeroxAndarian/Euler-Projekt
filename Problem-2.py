import math

def vsota(n):
    '''Vrne vsoto sodih Fibonaccijevih stevil, ki so manjsi od $n$.'''
    vsota = 0
    F1 = 1
    F2 = 2
    while F1 <= n:
        if F1 % 2 == 0:
            vsota += F1   
        F1, F2 = F2, F1 + F2           
    return vsota

print(vsota(4000000))
