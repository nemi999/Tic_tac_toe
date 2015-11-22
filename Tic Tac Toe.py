@@ -0,0 +1,182 @@
from random import randrange
from tkinter import *
from Choose_Character import player, enemy
from Choose_to_go_first_or_not import go_first
game = Tk()
print(go_first)
result = ''

row1 = ['', '', '']
row2 = ['', '', '']
row3 = ['', '', '']
column = [row1, row2, row3]

def print_grid():
    print(" {:1} |  {:1}  | {:1}".format(column[0][0], column[0][1], column[0][2]))
    print("-------------")
    print(" {:1} |  {:1}  | {:1}".format(column[1][0], column[1][1], column[1][2]))
    print("-------------")
    print(" {:1} |  {:1}  | {:1}".format(column[2][0], column[2][1], column[2][2]))
    print('##############')

frame = Canvas(game, width=600, height=600)
game.title("Tic Tac Toe")

def create_board():
    global offset
    offset = 2
    frame.create_rectangle(10 + offset, 10 + offset, 190 + offset, 190 + offset, fill='#66CD00', activefill="red")
    frame.create_rectangle(210 + offset, 10 + offset, 390 + offset, 190 + offset, fill='#66CD00', activefill="red")
    frame.create_rectangle(410 + offset, 10 + offset, 590 + offset, 190 + offset, fill='#66CD00', activefill="red")

    frame.create_rectangle(210 + offset, 210 + offset, 390 + offset, 390 + offset, fill='#66CD00', activefill="red")
    frame.create_rectangle(10 + offset, 210 + offset, 190 + offset, 390 + offset, fill='#66CD00', activefill="red")
    frame.create_rectangle(10 + offset, 410 + offset, 190 + offset, 590 + offset, fill='#66CD00', activefill="red")

    frame.create_rectangle(210 + offset, 410 + offset, 390 + offset, 590 + offset, fill='#66CD00', activefill="red")
    frame.create_rectangle(410 + offset, 210 + offset, 590 + offset, 390 + offset, fill='#66CD00', activefill="red")
    frame.create_rectangle(410 + offset, 410 + offset, 590 + offset, 590 + offset, fill='#66CD00', activefill="red")
    frame.pack()

create_board()

def random_ai_turn(): #not final AI version (?)
    x = (randrange(3))
    y = (randrange(3))
    if column[y][x] == "":
        take_tally((x) * 200, (y) * 200, enemy)
    else:
        random_ai_turn()
        return None


def create_x(x1, y1, x2, y2):
    frame.create_line(x1, y1, x2, y2)
    frame.create_line(x2, y1, x1, y2)

def take_tally(x: int, y: int, symbol: str) -> None:
    global column
    global player_turn
    if x < 200 and y < 200 and column[0][0] == '':
        if symbol == 'o':
            frame.create_oval(25, 25, 175, 175)
        else:
            create_x(25, 25, 175, 175)
        column[0][0] = symbol
    elif x >= 200 and x < 400 and y < 200 and column[0][1] == '':
        if symbol == 'o':
            frame.create_oval(225, 25, 375, 175)
        else:
            create_x(225, 25, 375, 175)
        column[0][1] = symbol
    elif x >= 200 and x < 400 and y < 200 and column[0][1] == '':
        if symbol == 'o':
            frame.create_oval(225, 25, 375, 175)
        else:
            create_x(225, 25, 375, 175)
        column[0][1] = symbol
    elif x >= 400 and y < 200 and column[0][2] == '':
        if symbol == 'o':
            frame.create_oval(425, 25, 575, 175)
        else:
            create_x(425, 25, 575, 175)
        column[0][2] = symbol
    elif x < 200 and y >= 200 and y < 400 and column[1][0] == '':
        if symbol == 'o':
            frame.create_oval(25, 225, 175, 375)
        else:
            create_x(25, 225, 175, 375)
        column[1][0] = symbol
    elif x >= 200 and x < 400 and y >= 200 and y < 400 and column[1][1] == '':
        if symbol == 'o':
            frame.create_oval(225, 225, 375, 375)
        else:
            create_x(225, 225, 375, 375)
        column[1][1] = symbol
    elif x >= 400 and y >= 200 and y < 400 and column[1][2] == '':
        if symbol == 'o':
            frame.create_oval(425, 225, 575, 375)
        else:
            create_x(425, 225, 575, 375)
        column[1][2] = symbol
    elif x < 200 and y >= 400 and column[2][0] == '':
        if symbol == 'o':
            frame.create_oval(25, 425, 175, 575)
        else:
            create_x(25, 425, 175, 575)
        column[2][0] = symbol
    elif x >= 200 and x < 400 and y >= 400 and column[2][1] == '':
        if symbol == 'o':
            frame.create_oval(225, 425, 375, 575)
        else:
            create_x(225, 425, 375, 575)
        column[2][1] = symbol
    elif x >= 400 and y >= 400 and column[2][2] == '':
        if symbol == 'o':
            frame.create_oval(425, 425, 575, 575)
        else:
            create_x(425, 425, 575, 575)
        column[2][2] = symbol

    if check_if_win(column):
        return end_game_winner(player_turn)

    if check_if_full(column):
        return end_game_tie()

    print_grid()
    player_turn = not player_turn
    if not player_turn:
        random_ai_turn()
        # check_if_win()
        # print(player_turn)

def reset_game():
    for x in range(3):
        for y in range(3):
            column[y][x] = ''
    create_board()

def end_game_tie() -> None:
    global result
    print_grid()
    print("Game over, it was a tie")
    reset_game()
    result = "Tie!"
    game.destroy()
    import Retry

def end_game_winner(winner: bool) -> None:
    global result
    print_grid()
    if (player_turn):
        result = ("You won!")
    else:
        result = ("You lost!")
    game.destroy()
    import Retry

def callback(event):
    take_tally(event.x, event.y, player)

frame.bind("<Button-1>", callback)

def check_if_full(list: 'list of list') -> bool:
    return "" not in list[0] and "" not in list[1] and "" not in list[2]


def check_if_win(list: 'list of list') -> bool:
    return ((list[0][0] == list[1][0] and list[1][0] == list[2][0] and "" != list[0][0]) or
            (list[0][1] == list[1][1] and list[1][1] == list[2][1] and "" != list[0][1]) or
            (list[0][2] == list[1][2] and list[1][2] == list[2][2] and "" != list[0][2]) or  # Vertical
            (list[0][0] == list[0][1] and list[0][1] == list[0][2] and "" != list[0][0]) or
            (list[1][0] == list[1][1] and list[1][1] == list[1][2] and "" != list[1][0]) or
            (list[2][0] == list[2][1] and list[2][1] == list[2][2] and "" != list[2][0]) or  # Horizontal
            (list[0][0] == list[1][1] and list[1][1] == list[2][2] and "" != list[0][0]) or
            (list[2][0] == list[1][1] and list[1][1] == list[0][2] and "" != list[2][0]))  # Diagonal

def is_empty(s: str) -> bool:
    return s == ''

if not player:
    random_ai_turn()
    print_grid()

player_turn = True  # when True, its players turn
if go_first == 'y':
    player_turn = True
elif go_first == 'n':
    player_turn = False
    random_ai_turn()

reset_game()

def on_closing():
    game.destroy()

game.protocol("WM_DELETE_WINDOW", on_closing)
