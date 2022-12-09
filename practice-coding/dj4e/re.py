import re

fhandler = open('romeo.txt')
numlist = []
for line in fhandler:
    line = line.strip()
    stuff = re.findall('s\S+', line)
    #if len(stuff) !=1: continue
    print(stuff)

x = 'My favorite numbers are 29 and 13'
a = 'We just received $10.00 for cookies.'
y = re.findall('[0-9]+', x)
z = re.findall('f.+?e', x)
w = re.findall('f.+', x)
v = re.findall('\$[0-9.]+', a)
print(y)
print(z)
print(w)
print(v)