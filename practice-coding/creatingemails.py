import sys
import random

users = ["camilo", "paula", "ricardo", "edilma", "manuel", "carlos", "miguel", "jorge", "juan", "dario", "ciz", "chloe"]
domains=["gmail","hotmail","yahoo","live","empresarial"]

fname = str(input('Enter a file name: '))
try:
    fhandler = open(fname, 'w')
    count = 0
    while count < 50:
        user = random.choice(users)
        domain = random.choice(domains)
        fhandler.writelines(f"From: {user}@{domain}.com\n")
        count = count + 1

except:
    print(f'The file {fname} cannot be opened')
    sys.exit()


