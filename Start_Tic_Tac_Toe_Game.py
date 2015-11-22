from tkinter import *

game = Tk()
game.title("Tic Tac Toe")

player = ''
enemy = ''
options = Canvas(game, height = 250, width = 450, background='white')
options.pack()

option = options.create_text(225, 50, anchor=CENTER, text="Tic Tac Toe", font=("Purisa", 28))

option1 = options.create_rectangle(50, 100, 200, 200, fill="#66CD00")
option1Text = options.create_text(125, 150, anchor=CENTER, text="Play", font=("Purisa", 24))

option2 = options.create_rectangle(250, 100, 400, 200, fill="#66CD00")
option2Text = options.create_text(325, 150, anchor=CENTER, text="Quit", font=("Purisa", 24))

def check_location(x:int, y:int):
    if (50 <= x <= 200 and 100 <= y <= 200):
        options.itemconfigure(option1, fill='red')
    elif(250 <= x <= 400 and 100 <= y <= 200):
        options.itemconfigure(option2, fill='red')
    else:
        options.itemconfigure(option1, fill='#66CD00')
        options.itemconfigure(option2, fill='#66CD00')

def check_click(x:int, y:int):
    if (50 <= x <= 200 and 100 <= y <= 200):
        game.destroy()
        import Choose_Character

    elif(250 <= x <= 400 and 100 <= y <= 200):
        game.destroy()

def track_mouse(event):
    check_location(event.x, event.y)

def track_click(event):
    check_click(event.x, event.y)

options.bind("<Button-1>", track_click)
options.bind("<Motion>", track_mouse)

def on_closing():
    game.destroy()

game.protocol("WM_DELETE_WINDOW", on_closing)
game.mainloop()
