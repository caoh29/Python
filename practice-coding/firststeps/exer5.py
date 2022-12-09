a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
z = []

n=1
while n in b:
    if  n in a:
        if n not in z:
            z.append(n)
            z.sort()
    n=n+1


print(z)