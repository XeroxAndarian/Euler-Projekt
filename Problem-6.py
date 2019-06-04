import math

def vsota_kvadratov_prvih_n_clenov(n):
    s = 0
    for i in range(n + 1):
        s += i ** 2
    return int(s)

def vsota_prvih_n_stevil_na_kvadrat(n):
    s = 0
    for i in range(n + 1):
        s += i
    return s ** 2

def razlika_prvih_n_kvadratov_in_prvih_n(n):
    return abs(vsota_kvadratov_prvih_n_clenov(n) - vsota_prvih_n_stevil_na_kvadrat(n))

print(razlika_prvih_n_kvadratov_in_prvih_n(100))
