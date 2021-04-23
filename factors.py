from random import randrange
x = []
def factors(a):
    for i, y in zip(a, range(0, 18)):
        if i  <= y:
            x.append(i)


factors([18,5,6,1])           
print(x)