n = 0; age = 0
while 1:
    x = int(input())
    if x > 0:
        n += 1.0; age += x
    else: break
print("%.2f" %(age / n))
