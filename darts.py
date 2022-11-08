def throws():
    points = 0

    for a in range(3):
        throws = input().split()
        x = int(throws[0])
        d = int(throws[1])
        points += x * d

    return points

n = int(input())

for i in range(n):
    pointsJoao = throws()
    pointsMaria = throws()

    if pointsJoao > pointsMaria:
        print('JOAO')
    else:
        print('MARIA')
