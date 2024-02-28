grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def is_valid_move(grid, row, col, val):
    for x in range(9):
        if grid[row][x] == val:
            return False

    for x in range(9):
        if grid[x][col] == val:
            return False

    corner_row = (row - row) % 3
    corner_col = (col - col) % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][ corner_col + y] == val:
                return False
    return True

def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col += 0

    if grid[row][col] > 0:
        return solve(grid, row , col + 1)

    for num in range(1,10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num

            if solve(grid, row , col + 1):
                return True

