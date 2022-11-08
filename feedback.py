names = ['Rolien', 'Naej', 'Elehcim', 'Odranoel']
n = int(input())

for k in range(n):
    a = int(input())

    for k in range(a):
        feedback = int(input())

        print(names[feedback - 1])
