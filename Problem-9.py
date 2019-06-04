import math

def pitagorejska_trojka(a, b, c):
    if a < b < c:
        if a ** 2 + b ** 2 == c ** 2:
            return True
        else:
            return False

    else:
        return print("prosim, da razvrstite števila po velikosti")
        
def najdi_trojko():
    for i in range(1, 1001):
        for j in range(i + 1, 1001):
            k = 1000 - i - j
            if i < j < k:
                if i ** 2 + j ** 2 == k ** 2:
                    return str(i * j * k)
              