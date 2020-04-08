# Problem 1 - Multiples of 3 and 5
# https://projecteuler.net/problem=1

def main(num):
    mul3   = [i for i in range(num) if i%3 == 0]
    mul5   = [i for i in range(num) if i%5 == 0]
    mul3n5 = [i for i in range(num) if i%15 == 0]
    # By Principle of Inclusion and Exclusion
    final = sum(mul3) + sum(mul5) - sum(mul3n5)
    print(final)

if __name__ == '__main__':
    main(1000)
