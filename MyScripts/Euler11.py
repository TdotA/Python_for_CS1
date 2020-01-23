f = open('Euler11.txt', 'r')
l = []
for i in range(20):
    l.append(list(f.readline().strip()))
print (l)  