while True:
    try:
        list1 = input().split()
        list2 = input().split()
        x, y = list1
        a, b = list2
        print(int(x) ^ int(y))
        print(int(a) ^ int(b))

    except EOFError:
        break

