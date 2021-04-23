import math
from sys import argv
def quad(a,b, c):
    an1 = -b + math.sqrt((b ** 2) -4 *(a*b))
    an2 = -b - math.sqrt((b ** 2) -4 * (a*b))
    return round(an1, 2), round(an2, 2)

if len(argv) < 4 or len(argv) > 4:
    print('ax^2 + bx + c = 0')
    exit()
else:
    x = quad(int(argv[1]), int(argv[2]), int(argv[3]))
    print(x)