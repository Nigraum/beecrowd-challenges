pos = 0
a = 0

for i in range(100):
    n = int(input())
    if(n > a):
        a = n
        pos = i
print(a)
print(pos + 1)
