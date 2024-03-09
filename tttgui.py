from tkinter import *
root = Tk()
root.title("test")
root.config(bg="skyblue")



gamepieces = []
wincolor = "#00A36C"
message_label = Label(root, text="TicTacToe", font=("Consolas", 47), justify=CENTER)
message_label.grid()
restart_btn = Button(root, text="RESTART", command=lambda: restart())
restart_btn.grid()
frame = Frame(root, width=700, height=700)
frame.grid(padx = 20, pady = 20)
turn_label = Label(root, text="X turn...", font=("Consolas", 21))
turn_label.grid()
colcount = 0
piececount = 0
for k in range(3):
    for i in range(3):
        gamepieces.append(Button(frame, text="*", font=("Consolas", 20), width=10, height=5, command=lambda c=piececount: game_click(c)))
        gamepieces[piececount].grid(row=k, column=i)
        piececount += 1

buttoncolor = gamepieces[0].cget("background")
activecolor = gamepieces[0].cget("activebackground")



class TicTacToe:
    def __init__(self):
        self.gameover = False
        self.gameboard = [["","",""],["","",""],["","",""]]
        self.xturn = True
        self.p1 = "X"
        self.p2 = "O"
        self.msg = ""
        self.winning_line = ["","",""]

    def reset_game(self):
        self.gameover = False
        self.xturn = True
        self.gameboard = [["","",""],["","",""],["","",""]]
        self.winning_line = ["","",""]

    def update_board(self, gamebuttons):
        count = 0
        idx = 0
        for i in range(9):
            if count > 2:
                count = 0
                idx += 1
            self.gameboard[idx][count] = gamebuttons[i].cget("text")
            count += 1
    
    def print_game(self):
        print(self.gameboard)

    def free_space(self, spot):
        count = 0
        for pieces in self.gameboard:
            for piece in pieces:
                count += 1
                if piece == "*" and count == spot:
                    return True
        return False
    
    def board_full(self):
        star_count = 0
        for pieces in self.gameboard:
            for piece in pieces:
                if piece == "*":
                    star_count += 1
        return star_count == 0

    def check_win(self, symbol):
        #check rows
        for idx, x in enumerate(self.gameboard):
            if x.count(symbol) == 3:
                print("MATCH ON ROW " + str(idx+1))
                match idx+1:
                    case 1:
                        self.winning_line = ["0", "1", "2"]
                    case 2:
                        self.winning_line = ["3", "4", "5"]
                    case 3:
                        self.winning_line = ["6", "7", "8"]
                return True
        #setup to check collums and diagonals
        cols = [ [], [], []]
        leftDiag = [ ]
        rightDiag = [ ] 
        for i, pieces in enumerate(self.gameboard):
            for j, piece in enumerate(pieces):
                if i == j:
                    leftDiag.append(piece)
                if j == len(pieces)-1 - i:
                    rightDiag.append(piece)
                cols[j].append(piece)
        #check columns
        for i, x in enumerate(cols):
            if x.count(symbol) == 3:
                print("MATCH ON COLUMN " + str(i+1))
                match i+1:
                    case 1:
                        self.winning_line = ["0", "3", "6"]
                    case 2:
                        self.winning_line = ["1", "4", "7"]
                    case 3:
                        self.winning_line = ["2", "5", "8"]
                return True
        #check diagnols
        if leftDiag.count(symbol) == 3:
            print("MATCH LEFTWAY DIAGONL")
            self.winning_line = ["0", "4", "8"]
            return True
        if rightDiag.count(symbol) == 3:
            print("MATCH RIGHTWAY DIAGONAL")
            self.winning_line = ["2", "4", "6"]
            return True
        return False



game = TicTacToe()
# print(gamepieces)

game.update_board(gamepieces)

game.print_game()

def restart():
    for piece in gamepieces:
        piece.config(text="*" ,bg = buttoncolor, activebackground = activecolor)
    turn_label.config(text="X turn...")
    game.reset_game()
    game.update_board(gamepieces)


def game_click(index):
    print(index,end="")
    print(" : text is " + gamepieces[index].cget("text"))
    if game.xturn:
        sym = game.p1
    else:
        sym = game.p2
    if not game.gameover:
        if game.free_space(index+1):
            gamepieces[index].config(text=sym)
            game.xturn = not game.xturn 
            game.update_board(gamepieces)
            if game.xturn:
                turn_label.config(text=game.p1 + " turn...")
            else:
                turn_label.config(text=game.p2 + " turn...")
        else:
            print("space occupied")
            text = "SPACE OCCUPIED"
            if game.xturn:
                text += " (X turn)"
            else:
                text += " (O turn)"
            turn_label.config(text=text)
        game.print_game()
        
        if game.check_win(game.p1):
            print(game.p1 + " WINS!")
            turn_label.config(text=game.p1 + " WINS!")
            print(game.winning_line)
            for i in range(len(game.winning_line)):
                gamepieces[int(game.winning_line[i])].config(bg=wincolor, activebackground=wincolor)
            game.gameover = True
        if game.check_win(game.p2):
            print(game.p2 + " WINS!")
            turn_label.config(text=game.p2 + " WINS!")
            print(game.winning_line)
            for i in range(len(game.winning_line)):
                gamepieces[int(game.winning_line[i])].config(bg=wincolor, activebackground=wincolor)
            game.gameover = True
        if game.board_full() and not game.gameover:
            print("ITS A DRAW")
            turn_label.config(text="ITS A DRAW!")
            game.gameover = True



    



root.mainloop()