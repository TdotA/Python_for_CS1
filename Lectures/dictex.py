# Dictionary (associative array)

d = {}

d = {'banana': 20, 'apple': 10, (2, 6): False,
     False: "Koper", 100: 34.54}

print(d)
print(d['banana'])

d['plum'] = 5

print(d)

print('apple' in d)
print('kiwi' in d)

print('***********')
for x in d:
	print(x, d[x])

# d = {key_1 : value_1, key_2: value_2, ...}





