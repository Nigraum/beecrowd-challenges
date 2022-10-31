a = int(input())
b = int(input())
oddSum = 0

for n in range((b + 1), a):
    if (n % 2 != 0):
        oddSum += n
print(oddSum)



