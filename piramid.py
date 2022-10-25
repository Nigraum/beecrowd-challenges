n = int(input())

ascii_value = 65

for i in range(n):
    for j in range(i + 1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")

    ascii_value =+ 1
    print("\n")
