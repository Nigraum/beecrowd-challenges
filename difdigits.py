x = [0 for r in range(5001)]

def repeat(n):
    digits = str(n)
    difDigits = set(digits)

    return len(digits) != len(difDigits)

def calc():
    for i in range(1, 5001):
        x[i] = x[i - 1]
        if(not repeat(i)):
            x[i] += 1

def difDigitsF(a, b):
    return x[b] - x[a - 1]

calc()

while True:
    try:
        N, M = [int(x) for x in input().strip().split(' ')]

        print(difDigitsF(N, M))
    except EOFError:
        break


