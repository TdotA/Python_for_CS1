f = open('Euler13.txt','r')
s = f.read().splitlines()
suma = 0

for i in s:
    suma = suma + int(i)
k = str(suma)
print(k[:10])
