import eulerlib


# kombinatorika 
def binom(n, r):
	return str(eulerlib.numtheory.nCr(n, r))

print(binom(40, 20))