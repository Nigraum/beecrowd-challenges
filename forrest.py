list = []
seconds = int(input())

while seconds >= 0:
    list.append(seconds)
    seconds = int(input())

avg = sum(list) / len(list)
print(f'MEDIA: {avg:.2f}')
for x in list:
    if x < avg:
        print(x)
