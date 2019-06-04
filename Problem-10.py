import math

def praštevilo(n):
    '''Vrne "True" če je število n praštevilo in "False", če ni za število n, ki je večje od 1'''

    # Če je število n večje od 1 ... 
    if n > 1 and n != 4:  

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
    
def vsota_vseh_pra_do_n(n):
    s = 0
    for i in range(1, n):
        if praštevilo(i):
            s += i
    return s

print(vsota_vseh_pra_do_n(10))


print(vsota_vseh_pra_do_n(100))
print(vsota_vseh_pra_do_n(1000))
print(vsota_vseh_pra_do_n(10000))
print(vsota_vseh_pra_do_n(2000000))



