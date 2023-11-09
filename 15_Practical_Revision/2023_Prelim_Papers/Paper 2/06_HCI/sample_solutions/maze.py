# %%
import random
## config consists of ( grid, (row, col) of robot, (row, col) of exit )
def init_config(filename):
    ## beware of empty lines in file
    grid = list(
        map(lambda line: list(line.strip()),open(filename))
    )[:-1]
    exit_column = random.randint(1,4)
    grid[-1][exit_column] = "."
    return grid, (0,4), (5,exit_column)

def draw(config):
    for row in config[0]:
        print(f"{ ''.join(row)}")
    print()



def make_move(config, prev_move=None):
    global count
    valid_letters = ('U','D','L','R','')
    while True:
        move = input(
            f"Enter direction ({','.join(map(lambda x: f'`{x}`', valid_letters))}):"
            )
        count+=1
        if move in valid_letters:
            if move == "":
                if prev_move:
                    move = prev_move
                else:
                    print("No previous move")
                    continue
            ## find new position of robot
            grid, (row, col), exit_pos = config
            if move == "U":
                new_row = row - 1
                if new_row > 0 and  grid[new_row][col] == ".":
                    return update_config(config, (new_row, col) ), move
            elif move == "D":
                new_row = row + 1
                if new_row < len(grid) and ( grid[new_row][col] == "." or grid[new_row][col] =="a" ):
                    return update_config(config, (new_row, col) ), move
            elif move == "L":
                new_col = col - 1
                if new_col > 0 and grid[row][new_col] == ".":
                    return update_config(config, (row, new_col) ), move
            elif move == "R":
                new_col = col + 1
                if new_col < len(grid[row]) and grid[row][new_col] == ".":
                    return update_config(config, (row, new_col) ), move    
        print("Invalid Move!")


def update_config(config, new_pos):
    grid, (row, col), exit_pos = config
    if exit_pos == new_pos: ## reach the end
        return None
    new_row, new_col = new_pos
    grid[row][col] = "X"
    grid[new_row][new_col] = "T"

    return grid, (new_row, new_col), exit_pos

# %%
config = init_config("MAZE.txt")
prev_move = None
count = 0
while config:
    draw(config)
    config, prev_move = make_move(config, prev_move)
print(f"You completed in {count} moves")





# %%
