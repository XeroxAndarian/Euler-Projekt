import math


def delitelji(n):
    '''Za število n vrne množico vseh njegovih deliteljev'''
    delitelji = {1, n}
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            delitelji.update((i, n // i))
    return delitelji
    
def praštevilo(n):
    '''Vrne "True" če je število n praštevilo in "False", če ni za število n, ki je večje od 1'''

    # Če je število n večje od 1 ... 
    if n > 1:  

       # ... preverimo deljivost števila, z vsemi njegovimi predhodniki njegove polovične vrednosti, saj... 
       for i in range(2, n // 2): 

           # ... če je n deljivo s katerimkoli številom i med n in n / 2, potem n ni praštevilo.
           if (n % i) == 0: 
               return False

        # Če pa pa tako število i ne obstaja, potem je število gotovo praštevilo. 
       else: 
           return True 

    # Če število ni pozitivno, potem funkcija avtomatično vrne "False"
    else: 
       return False

def praštevila(n):
    '''Za število n izpiše, katera praštevila, ga delijo'''

    #Zapišemo množico vseh deliteljev
    množica_deliteljev = delitelji(n)

    #Definiramo prazen setnam, kamor bomo dajali praštevila
    seznam_prastevil = []

    #Za vsak element množicedeliteljev preverimo, če je praštevilo
    for i in množica_deliteljev:
        if praštevilo(i) == True:
            seznam_prastevil.append(i)
    return seznam_prastevil

def maksimum(seznam):
    return max(seznam)

def najvecje_prastevilo_ki_deli(n):
    return max(praštevila(n))


# Rešitev 3. naloge:
print(najvecje_prastevilo_ki_deli(600851475143))
