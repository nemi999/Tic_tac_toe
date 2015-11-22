from tkinter import *
from Tic_Tac_Toe import result
retry = True
game = Tk()
game.title(result)

options = Canvas(game, height = 200, width = 350, background='white')
options.pack()

option = options.create_text(200, 50, anchor=CENTER, text=result, font=("Purisa", 28))

option1 = options.create_rectangle(100, 100, 250, 150, fill="#66CD00")
option1Text = options.create_text(175, 125, anchor=CENTER, text="Close", font=("Purisa", 30), width=100)


def check_location(x:int, y:int):
    if (100 <= x <= 300 and 100 <= y <= 300):
        options.itemconfigure(option1, fill='red')
    else:
        options.itemconfigure(option1, fill='#66CD00')

def check_click(x:int, y:int):
    if (100 <= x <= 300 and 100 <= y <= 300):
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

#Retry function, not yet working!
'''
options = Canvas(game, height = 350, width = 450, background='white')
options.pack()

option = options.create_text(225, 50, anchor=CENTER, text=result + " , Retry?", font=("Purisa", 28))

option1 = options.create_rectangle(50, 100, 200, 200, fill="#66CD00")
opetion1Text = options.create_text(125, 150, anchor=CENTER, text="Retry?", font=("Purisa", 30), width=100)

option2 = options.create_rectangle(250, 100, 400, 200, fill="#66CD00")
option2Text = options.create_text(325, 150, anchor=CENTER, text="Quit", font=("Purisa", 30), width=100)


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
        import Start_Tic_Tac_Toe_Game
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
'''
