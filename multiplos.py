n = input().split()
a, b = n

a = int(a)
b = int(b)

if a < b:
if b % a == 0:
    print("Sao multiplos")
else:
    print("Nao sao multiplos")

if a > b:
if a % b == 0:
    print("Sao multiplos")
else:
    print("Nao sao multiplos")


