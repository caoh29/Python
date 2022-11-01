def is_prime(num):
    digits = [2,3,5,7]
    
    if (num in digits) or ((num % digits[0] != 0) and (num % digits[1] != 0) and (num % digits[2] != 0) and (num % digits[3] != 0)):
        is_prime = True
        return is_prime
    
    else:
        is_prime = False
        return is_prime
        

print(is_prime(5))