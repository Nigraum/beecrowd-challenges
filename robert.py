while True:
    try:
        n = int(input())
        epr = 0
        ehd = 0
        intruder = 0
        for i in range(n):
            l, course = input().split()
            if course == 'EPR':
                epr += 1
            elif course == 'EHD':
                ehd += 1
            else:
                intruder += 1

        print(f'EPR: {epr}')
        print(f'EHD: {ehd}')
        print(f'INTRUSOS: {intruder}')

    except EOFError:
        break


