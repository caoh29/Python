def is_even(n):
    return (n % 2 == 0)

l = [1, 2, 3, 4, 5]
l2= filter(is_even, l)

print(l2)
print(l)