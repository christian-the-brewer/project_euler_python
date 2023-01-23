#Problem 3
#Largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?


def prime_factors(number):
    limit = number
    i = 1
    factors = []
    while i < limit:
        if number % i == 0:
            factor = int(number / i)
            factors.append(i)
            factors.append(factor)
            limit = factor
            # print(f"{i}, {factor}")
        i += 1
    # for num in factors:
    #     print(num)
    #check for prime 
    factors.sort(reverse=True)
    for num in factors:
        if check_prime(num):
            return num

def check_prime(num):
    if num % 2 == 0 or num % 3 == 0:
        return False
    elif num == 2 or num == 3:
        return False
    elif num == 1:
        return False
    for i in range(5, int(num ** 0.5)):
        if num % i == 0:
            return False

    return True

print(prime_factors(600851475143))


