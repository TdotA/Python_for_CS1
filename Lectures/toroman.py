def to_roman(n):
	# 0 <= n <= 3999
	# 1952 -> 'MCMLII'
	# 0 -> ''
	o = n % 10
	t = (n // 10) % 10
	h = (n // 100) % 10
	m = n // 1000
	# print(o, t, h, m)

	ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
	tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
	hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
	thousands = ['', 'M', 'MM', 'MMM']
	
	return thousands[m] + hundreds[h] + tens[t] + ones[o]

# https://en.wikipedia.org/wiki/Roman_numerals
# print(to_roman(1952))

values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Homework for Dejan: If s is not valid, return None.
def to_arabic_dejan(s):
	ans = 0
	# 'MCMLII' -> 1952
	# '' -> 0
	for i in range(len(s) - 1):
		c = s[i]
		c2 = s[i + 1]
		if values[c2] > values[c]:
			ans = ans - values[c]
		else:
			ans = ans + values[c]
	if len(s) > 0:
		ans = ans + values[s[len(s) - 1]]
	return ans

# print(to_arabic('MCMLII'))

"""
for i in range(4000):
	s = to_roman(i)
	i2 = to_arabic(s)
	if i != i2:
		print(i, s, i2)
"""

all_roman = {}

for i in range(4000):
	s = to_roman(i)
	all_roman[s] = i

# print(all_roman)

def to_arabic(s):
	if s in all_roman:
		return all_roman[s]
	return None

print(to_arabic('MDILXDLXI'))
print(to_arabic_dejan('MDILXDLXI'))


