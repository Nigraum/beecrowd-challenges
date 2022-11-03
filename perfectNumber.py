def perfectNumber(n):
    l = []
    for i in range(1, n):
        if n % i == 0:
            l.append(i)
    return sum(l)

rep = int(input())

for i in range(rep):
    num = int(input())
    if perfectNumber(num) == num:
        print(f'{num} eh perfeito')
    else:
        print(f'{num} nao eh perfeito')
