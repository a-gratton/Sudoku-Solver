import random


def main():
    # random grid generation driver code
    grid = [[0] * 9 for i in range(9)]
    for index, row in enumerate(grid):
        for i in range(len(row)):
            if not random.randrange(0, 4):
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

# main recursive backtracking function
# traverses depth first, backtracking if no valid solutions are possible on current branch
def solve(grid):
    row, col, flag = getNext(grid)
    if not flag:
        return True # grid is solved
    else:
        for i in range(1, len(grid) + 1):
            if isValid(grid, row, col, i):
                grid[row][col] = i
                if solve(grid):
                    return True
                else:
                    grid[row][col] = 0
    return False # no solutions exist

# finds next empty space in the grid
def getNext(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == 0:
                return i, j, 1
    return 0, 0, 0


# calls functions to determine if a given number placement is valid
def isValid(grid, row, col, num):
    if grid[row][col]:
        return False
    else:
        return checkRow(grid, row, num) and checkCol(grid, col, num) and checkSquare(grid, row, col, num)

#checks for valid placement incurrent row
def checkRow(grid, row, num):
    for i in grid[row]:
        if num == i: return False
    return True

# checks for valid placement in current column
def checkCol(grid, col, num):
    for i in range(len(grid)):
        if num == grid[i][col]: return False
    return True

# checks for valid placement in current square area
def checkSquare(grid, row, col, num):
    rowStart = int((row // (len(grid) ** 0.5)) * (len(grid) ** 0.5))
    colStart = int((col // (len(grid) ** 0.5)) * (len(grid) ** 0.5))
    for i in range(rowStart, rowStart + int((len(grid) ** 0.5))):
        for j in range(colStart, colStart + int((len(grid) ** 0.5))):
            if num == grid[i][j]: return False
    return True

if __name__ == '__main__':
    main()