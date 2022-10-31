from functools import reduce

def checkLine(sudoku, x):
    numbers = set(sudoku[x])
    return len(numbers) == 9
