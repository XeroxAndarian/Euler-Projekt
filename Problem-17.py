


def beseda(n):
	beseda = sum(len(prevedi(i)) for i in range(1, n + 1))
	return str(beseda)


def prevedi(n):
	if 0 <= n < 20:
		return enice[n]
	elif 20 <= n < 100:
		return desetice[n // 10] + (enice[n % 10] if (n % 10 != 0) else "")
	elif 100 <= n < 1000:
		return enice[n // 100] + "hundred" + (("and" + prevedi(n % 100)) if (n % 100 != 0) else "")
	elif 1000 <= n < 1000000:
		return prevedi(n // 1000) + "thousand" + (prevedi(n % 1000) if (n % 1000 != 0) else "")
	else:
		return None


enice = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
desetice = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]


print(beseda(1000))