import math

def vsota_do_n(n):
    vsota = 0
    for i in range(0, n + 1, 1):
        vsota += i
    return vsota



def delitelji(n):
    '''Za število n vrne množico vseh njegovih deliteljev'''
    delitelji = {1, n}
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            delitelji.update((i, n // i))
    return delitelji

def prva_z_n_deliteli(k):
    m = 100
    while len(delitelji(vsota_do_n(m))) < k:
        m += 1
    return m

print(prva_z_n_deliteli(500))