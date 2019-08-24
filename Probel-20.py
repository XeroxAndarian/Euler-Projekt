import math
import eulerlib



def fakulteta_vsote(n):
	a = math.factorial(n)
	vsota = eulerlib.numtheory.digital_sum(a)
	return str(vsota)


print(fakulteta_vsote(100))