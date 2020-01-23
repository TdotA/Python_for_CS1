import turtle as t 

def koch_curve(d,lvl):  
    if lvl == 0:
        t.fd(d)
        t.pu()
        t.bk(d)
        t.pd()
        return
    koch_curve(d/3, lvl-1)
    t.pu()
    t.fd(d/3)
    t.lt(60)
    t.pd()
    koch_curve(d/3, lvl-1)
    t.pu()
    t.fd(d/3)
    t.rt(120)
    t.pd()
    koch_curve(d/3, lvl-1)
    t.pu()
    t.fd(d/3)
    t.lt(60)
    t.pd()
    koch_curve(d/3, lvl -1)
    t.pu()
    t.bk(2*d/3)
    t.pd()

#koch_curve(2000, 5)

def kochflake(d, lvl):
    i = 0
    while i <= 3:
        koch_curve(d,lvl)
        t.pu()
        t.fd(d)
        t.rt(120)
        t.pd()
        i= i+1
    


#kochflake(500,4)

def kochflake_area(d, lvl):
    if lvl == 0:
        return (3**0.5)/4
    kochflake_area(d*3, lvl-1) + 3*(4**(lvl-2)) * (3**0.5) *(1/9**lvl)   

#kochflake_area(100, 2)

def tree(d, k, alpha, lvl):
    t.fd(d)
    if lvl > 0:
        t.lt(alpha)
        tree(d*k, k, alpha, lvl-1)
        t.rt(2 * alpha)
        tree(d*k, k, alpha, lvl-1)
        t.lt(alpha)
    t.pu()
    t.bk(d)
    t.pd()
tree(100,0.7,75,6)
