class Game:
    def __init__(self):
        f = open("MAZE.TXT")
        self.board=[]
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            line = list(line)
            if "P" in line:
                line[line.index("P")] = "."
            self.board.append(line)
        max_row = len(self.board)-1
        max_col = len(self.board[0])-1
        self.cur_pos = max_row//2,max_col//2
        self.board[max_row//2][max_col//2]="O"

    def place_prize(self):
        import random
        max_row = len(self.board)-1
        max_col = len(self.board[0])-1

        while True:
            random_row, random_col = random.randint(0,max_row),random.randint(0,max_col)
            if self.board[random_row][random_col] not in ("X", "O"):
                self.board[random_row][random_col] = "P"
                break
    def show_board(self):
        for row in self.board:
            print(f"{''.join(row)}")
        print()
 
    def move(self, step):
        def check_valid(r, c):
            if r >= len(self.board) or c >= len(self.board[0]) or self.board[r][c] == "X":
                return False
            return True

        def over(r, c):
            return self.board[r][c] == "P"

        if step.upper() == "R":
            new_pos = self.cur_pos[0],self.cur_pos[1]+1
        if step.upper() == "L":
            new_pos = self.cur_pos[0],self.cur_pos[1]-1
        if step.upper() == "U":
            new_pos = self.cur_pos[0]-1,self.cur_pos[1]
        if step.upper() == "D":
            new_pos = self.cur_pos[0]+1,self.cur_pos[1]
            
        if check_valid(*new_pos):
            if over(*new_pos): # spread (x,y)->x,y
                return True
            self.board[self.cur_pos[0]][self.cur_pos[1]] = "."
            self.board[new_pos[0]][new_pos[1]] = "O"  
            self.cur_pos = new_pos
        return False

game = Game()
game.place_prize()
game.show_board()

while True:
    step = input("Move>")
    if game.move(step):
        print("Player has reached prize")
        break
    else:
        game.show_board()