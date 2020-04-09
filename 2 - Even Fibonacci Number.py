# Problem 2 - Even Fibonacci Number
# https://projecteuler.net/problem=2
# Note: Only "Even-Valued" terms are needed.


def brute(x):
    Fn_2, Fn_1 = 1, 1
    total = 0
    while True:
        Fn = Fn_2 + Fn_1
        if Fn >= x:
            break
        if Fn%2 == 0:
            total += Fn
        Fn_2, Fn_1 = Fn_1, Fn
    print(total)


def optimum(x):
    # Writing the Fibonacci Series in terms of only even terms
    #       { 2             if n=0  }
    # EFn = { 8             if n=1  }
    #       {4EFn_1 + EFn_2 if n>1  }
    EFn_2, EFn_1 = 2, 8
    total = EFn_1 + EFn_2
    while True:
        EFn = 4*EFn_1 + EFn_2;
        if EFn >= x:
            break;
        total += EFn
        EFn_1, EFn_2 = EFn, EFn_1
    print(total)

if __name__ == '__main__':
    brute(4_000_000)
    optimum(4_000_000)
