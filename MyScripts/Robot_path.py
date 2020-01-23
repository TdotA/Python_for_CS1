3
x =int(input("Enter first coordinate: "))
y =int(input("Enter second coordinate: "))
Direction = input("Enter direction: ")
Instructions = input("Enter instructions: ")
 
if Direction == "w" :
    d = 4 
if Direction == "N" :
    d = 1 
if Direction == "E" :
    d = 2 
if Direction == "S" :
    d = 3 


for i in Instructions:
    if i == "L" :
        d = d -1
        continue 
    if i == "R" :
        d = d + 1
        continue
    if i == "A" and (d % 4 == 0 or d == 0) and x - 1 >= 0:
        x = x - 1
    if i == "A" and d % 4 == 3 and y - 1 >= 0:
        x = x - 1
    if i == "A" and d % 4 == 1:
        y = y + 1
    if i == "A" and d % 4 == 2 and x - 1 >= 0:
        x = x + 1
 
if abs(d) % 4 == 0 or d == 0:
    Direction = "W"
if abs(d) % 4 == 1 :
    Direction = "N"
if abs(d) % 4 == 2:
    Direction = "E"
if abs(d) % 4 == 3:
    Direction = "S"

print("Coordinates: (" + str(x) +"," + str(y) + ")" )
print(Direction)

      
