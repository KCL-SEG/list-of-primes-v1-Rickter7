"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = [2]
    x = 3
    while len(list) < number_of_primes:
        prime = True
        for i in range(2, x):
            if x % i == 0:
                prime = False
                break
            i += 1
        if prime == True:
            list.append(x)
        x += 1
    return list
