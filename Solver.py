import random


def main():
    grid = [[0]*9 for i in range(9)]
    for index, row in enumerate(grid):
        for i in range(len(row)):
            if not random.randrange(0, 2):
                temp = random.randrange(0, 10)
                if isValid(grid, index, i, temp):
                    row[i] = temp
        print(row)
    print("\n")
    if solve(grid):
        for row in grid:
            print(row)
    else:
        print("No Solution")


def solve(grid):
    row, col, flag = getNext(grid)
    if not flag: return True
    else:
        for i in range(1, len(grid)+1):
            if isValid(grid, row, col, i):
                grid[row][col] = i
                if solve(grid): return True
                else: grid[row][col] = 0
    return False


def getNext(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                return i, j, 1
    return 0, 0, 0


def isValid(grid, row, col, num):
    if grid[row][col]:
        return False
    else:
        return checkRow(grid, row, num) and checkCol(grid, col, num) and checkSquare(grid, row, col, num)


def checkRow(grid, row, num):
    for i in grid[row]:
        if num == i: return False
    return True


def checkCol(grid, col, num):
    for i in range(len(grid)):
        if num == grid[i][col]: return False
    return True


def checkSquare(grid, row, col, num):
    rowStart = int((row // (len(grid) ** 0.5)) * (len(grid) ** 0.5))
    colStart = int((col // (len(grid) ** 0.5)) * (len(grid) ** 0.5))
    for i in range(rowStart, rowStart + int((len(grid) ** 0.5))):
        for j in range(colStart, colStart + int((len(grid) ** 0.5))):
            if num == grid[i][j]: return False
    return True


main()
