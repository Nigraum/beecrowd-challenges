while True:
    try:
        list1 = input().split()
        x, y = list1
        print(int(x) ^ int(y))

    except EOFError:
        break

