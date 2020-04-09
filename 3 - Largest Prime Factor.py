# Problem 3 - Largest Prime Factors
# https://projecteuler.net/problem=3
# Prime Factorization Algorithms find Prime Factors
# For Example: Sieve of Eratothenes, Polland's Rho Algorithm
from math import sqrt, ceil

def max_prime_factor(n):
    maxPrime = -1

    # We keep dividing n by 2 to get rid of all the even composite factors.
    while n % 2 == 0:
        maxPrime = 2
        n >>= 1                 # equivalent to n //= 2

    # We loop over the possible odd factors to remove the rest of the composites
    # and updating maxPrime to the largest factor.
    for i in range(3, ceil(sqrt(n)) + 1, 2):
        while n % i == 0:
            maxPrime = i
            n //= i

    # If at this stage n is is still bigger than 2
    # then n must be prime so we return it, otherwise we return maxPrime
    if n > 2:
        return n
    else:
        return maxPrime


if __name__ == '__main__':
    print(max_prime_factor(600_851_475_143))
