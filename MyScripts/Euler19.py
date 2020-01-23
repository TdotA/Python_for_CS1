months = [31,28, 31,30,31,30,31,31,30,31,30,31]
months1 = [31,28, 31,30,31,30,31,31,30,31,30,31]
def counting():
    day = 1 
    count = 0
    for y in range(1901,2001):
        if y % 4 == 0:
            for m in months:
                day+= months[m]
                if day % 7 == 0 :
                    count+= 1

        else:
            for m in months1:
                day+= months1[m]
                if day % 7 == 0 :
                    count+= 1
    print(count)