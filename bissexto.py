y1 = int(input())
y2 = int(input())
leap = 0

for i in range(y1, y2 + 1):
    if (i % 4 == 0 and i % 100 !=0) or i % 400 == 0:
        leap +=1
        print(i)
print(f'bissextos: {leap}')
