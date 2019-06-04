import math

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
    '''Za število n izpiše, vsa praštevila do n-tega'''
    #Definiramo prazen setnam, kamor bomo dajali praštevila
    seznam_prastevil = []
    x = 2
    #Za vsak element množicedeliteljev preverimo, če je praštevilo
    while len(seznam_prastevil) <= n:
        
        if praštevilo(x):
            seznam_prastevil.append(x)
            x += 1
        else:
            x += 1

    return seznam_prastevil

def nto_prastevilo(n):
    return praštevila(n)[n]

print(nto_prastevilo(10001))

#izkaže se da vzame cca 60'

