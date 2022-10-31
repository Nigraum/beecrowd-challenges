a = int(input())
b = int(input())
prime = 0

for n in range(a + 1, b + 1):
    if all(n % i != 0 for i in range(2, n)):
        prime += 1
        print(n)
print(f'primos: {prime}')
