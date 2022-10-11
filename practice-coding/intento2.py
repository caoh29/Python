def is_prime(num):
    if num in [2,3,5,7]:
        is_prime = True
        return is_prime
    elif num % 2 != 0:
        if num % 3 != 0:
            if num % 5 != 0:
                if num % 7 != 0:
                    is_prime = True
                    return is_prime
                else:
                    is_prime = False
                    return is_prime
            else:
                is_prime = False
                return is_prime
        else:
            is_prime = False
            return is_prime
    else:
        is_prime = False
        return is_prime

print(is_prime(12))


for i in range(1, 100):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()