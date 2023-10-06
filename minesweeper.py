# Minesweeper
def count_adjacent_mines(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    mine_count = 0

    # Define the coordinates of adjacent elements
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        # Check if the adjacent coordinates are within bounds
        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '#':
            mine_count += 1

    return mine_count

def create_minefield(grid):
    rows = len(grid)
    cols = len(grid[0])
    minefield = [['-'] * cols for _ in range(rows)]
# Use for loops as co-ordinates
  
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '#':
                minefield[i][j] = '#'
            else:
                minefield[i][j] = str(count_adjacent_mines(grid, i, j))

    return minefield

# The Grid as 2D list
grid = [
    ['#', '#', '-', '-', '#'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '#', '-'],
    ['-', '-', '#', '-', '-'],
    ['-', '-', '-', '-', '-']
]

minefield = create_minefield(grid)

# Display the minefield
for row in minefield:
    print(' '.join(row))

def print_board(grid):
    for i, row in enumerate(grid):
        print(' '.join(row))
        print('')
      
results = print_board(grid)
print(results)