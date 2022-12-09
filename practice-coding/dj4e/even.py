import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n in range(2,6):
        mod = n % 2
        if mod == 0:
            print("Not Weird")
        else:
            print("Weird")
    elif n in range(6,20):
        print("Weird")
    elif (n >= 20 and n <= 100):
        modular = n % 2
        if modular == 0:
            print("Not Weird")
        else:
            print("Weird")
    else:
        sys.exit()