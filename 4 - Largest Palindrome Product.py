# Problem 4 - Largest Palindrome Product
# https://projecteuler.net/problem=4


def brute(n):
    min = 10**(n-1)
    max = 10**n-1
    largest =-1
    for i in range(min, max+1):
        for j in range(min ,max+1):
            temp = i*j
            if str(temp) == str(temp)[::-1] and temp>largest:
                largest = temp
    print(largest)

if __name__ == '__main__':
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        brute(n)
