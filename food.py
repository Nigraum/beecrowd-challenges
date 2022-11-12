x = input().split()
a, b = x

if int(a) == 1:
    print(f'Total: R$ {4.00 * int(b):.2f}')

if int(a) == 2:
    print(f'Total: R$ {4.50 * int(b):.2f}')

if int(a) == 3:
    print(f'Total: R$ {5.00 * int(b):.2f}')

if int(a) == 4:
    print(f'Total: R$ {2.00 * int(b):.2f}')

if int(a) == 5:
    print(f'Total: R$ {1.50 * int(b):.2f}')
