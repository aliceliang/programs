"""
 2D Spiral Array
Find the pattern and complete the function:
int[][] spiral(int n);
where n is the size of the 2D array.
"""

def spiral(n):
    if n == 1:
        return [[1]]
    result = [[None]*n for i in range(n)]
    row = 0
    col = 0
    spiral = 0
    for i in range(n*n):
        result[row][col] = i + 1

        if col == row and row > 0 and row < n - spiral - 1:
            spiral += 1

        # get direction based on where we are in the spiral
        if col >= row and col < n - spiral - 1: # going right
            col += 1
            continue
        if col == n - spiral - 1 and row < n - spiral - 1: # going down
            row += 1
            continue
        if row == n - spiral - 1 and col > spiral: # going left
            col -= 1
            continue
        if col == spiral and row > spiral + 1: # going up
            row -= 1
            continue
        if col == spiral and row == spiral + 1: # go right again
            col += 1
            continue
    return result