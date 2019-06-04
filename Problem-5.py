import math


def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)


def deljiv_z_vsemi_do(n):
    x = 1
    for i in range(1, n):
        if lcm(x, i) > x:
            x = lcm(x, i)
    return int(x)

print(deljiv_z_vsemi_do(20))
