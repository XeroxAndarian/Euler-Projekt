import math
import eulerlib


def vsota_stevk(n):
    return eulerlib.numtheory.digital_sum(n)


print(vsota_stevk(2 ** 1000))