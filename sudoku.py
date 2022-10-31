from functools import reduce

def checkLine(sudoku, x):
    numbers = set(sudoku[x])
    return len(numbers) == 9

def checkColumn(sudoku, x):
    numbers = set([sudoku[i][x] for i in range(9)])
    return len(numbers) == 9

def checkSquare(sudoku, x):
    line, column = 3 * (x // 3), 3 * (x % 3)
    numbers = set(list(reduce(list.__add__, [l[column: (column + 3)] for l in sudoku[line:(line + 3)]])))
    return len(numbers) == 9

n = int(input())
for k in range(1, n + 1):
    sudoku = []

    for i in range(9):
        sudoku.append([int(x) for x in input().strip().split(' ')])

        print(f'Instancia {k}')

        answer = 'SIM'
        for i in range(9):
            if(not checkLine(sudoku, i) or not checkColumn(sudoku, i) or not checkSquare(sudoku, i)):
                answer = 'NAO'

print(answer)
print()
