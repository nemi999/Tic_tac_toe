from tkinter import *
game = Tk()
game.title("Choose turn!")

go_first = ''

options2 = Canvas(game, height = 250, width = 450, background='white')
options2.pack()

option = options2.create_text(225, 50, anchor=CENTER, text="Do you want to go first?", font=("Purisa", 28))

option1 = options2.create_rectangle(50, 100, 200, 200, fill="#66CD00")
option1Text = options2.create_text(125, 150, anchor=CENTER, text="Yes", font=("Purisa", 24))

option2 = options2.create_rectangle(250, 100, 400, 200, fill="#66CD00")
option2Text = options2.create_text(325, 150, anchor=CENTER, text="No", font=("Purisa", 24))

def check_location2(x:int, y:int):
    if (50 <= x <= 200 and 100 <= y <= 200):
        options2.itemconfigure(option1, fill='red')
    elif(250 <= x <= 400 and 100 <= y <= 200):
        options2.itemconfigure(option2, fill='red')
    else:
        options2.itemconfigure(option1, fill='#66CD00')
        options2.itemconfigure(option2, fill='#66CD00')

def check_click1(x:int, y:int):
    global go_first
    if (50 <= x <= 200 and 100 <= y <= 200):
        go_first = 'y'
        game.destroy()
        import Tic_Tac_Toe
    elif(250 <= x <= 400 and 100 <= y <= 200):
        go_first = 'n'
        game.destroy()
        import Tic_Tac_Toe

def track_mouse(event):
    check_location2(event.x, event.y)

def track_click(event):
    check_click1(event.x, event.y)

options2.bind("<Button-1>", track_click)
options2.bind("<Motion>", track_mouse)

def on_closing():
    game.destroy()

game.protocol("WM_DELETE_WINDOW", on_closing)
