
def naslednji_clen(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def dolzina_zaporedja(n):
    if n == 1:
        return 1
    else:
        return 1 + dolzina_zaporedja(naslednji_clen(n))



def najdaljse_zaporedje(m, n):
    if m == n:
        return dolzina_zaporedja(m)
    else:
        return max(dolzina_zaporedja(m), najdaljse_zaporedje(m + 1, n))

print(najdaljse_zaporedje(900000, 1000000))