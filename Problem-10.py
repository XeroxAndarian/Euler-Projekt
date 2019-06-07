import eulerlib



def vsota_prastevil(n):
	vsota = sum(eulerlib.prime_numbers.primes(n))
	return vsota

print(vsota_prastevil(1999999))

