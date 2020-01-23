f = open('krpan.txt', 'r')
text = f.read().upper()
f.close()

freq = {}

ex = {'Á': 'A', 'É': 'E', 'Ê': 'E', 'À': 'A'}

# print(text)

for c in text:
	if not c.isalpha():
		continue
	if c in ex:
		c = ex[c]
	if not (c in freq):
		freq[c] = 0
	freq[c] = freq[c] + 1

#print(freq)

# for c in freq:
#	print(c, freq[c])

# l = list(freq.items()) # List of pairs.
l = []

for k, v in freq.items():
	l.append((v, k))

#for k, v in freq.items():
#	l.append((-v, k))

l.sort()
l.reverse()

for k, v in l:
	print(v, k)

