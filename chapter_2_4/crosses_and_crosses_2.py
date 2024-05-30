# 1. Встроенные модули
import random
from copy import deepcopy
from functools import partial
from tkinter import ACTIVE, Button, DISABLED, Tk, messagebox

#  INFO: CTRL + SHIFT + стрелка

# 2. Внешние модули


# 3. Модули проекта


# TODO: 1. Убрать ненужные комментарии

# sign variable to decide the turn of which player
sign = 0

board = [[" " for x in range(3)] for y in range(3)]


# Check l(O/X) won the match or not
# according to the rules of the game


# TODO: 2. Дать понятные имена параметрам b и l
# INFO: Удерживать ALT + клик или SHIFT + F6
def winner(b, l):
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l)
            or (b[1][0] == l and b[1][1] == l and b[1][2] == l)
            or (b[2][0] == l and b[2][1] == l and b[2][2] == l)
            or (b[0][0] == l and b[1][0] == l and b[2][0] == l)
            or (b[0][1] == l and b[1][1] == l and b[2][1] == l)
            or (b[0][2] == l and b[1][2] == l and b[2][2] == l)
            or (b[0][0] == l and b[1][1] == l and b[2][2] == l)
            or (b[0][2] == l and b[1][1] == l and b[2][0] == l))


# TODO: 3. Дать понятные имена параметрам gb, l1 и l2
# Configure text on button while playing with another player
def get_text(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    if winner(board, "X"):
        gb.destroy()
        messagebox.showinfo("Побеждает", "1 игрок")
    elif winner(board, "O"):
        gb.destroy()
        messagebox.showinfo("Побеждает", "1 игрок")
    elif (isfull()):
        gb.destroy()
        messagebox.showinfo("Игра вничью", "Игра вничью")


# Check if the player can push the button or not

# TODO: 4. Функция нигде в коде не используется
def isfree(i, j):
    return board[i][j] == " "


# Check the board is full or not

# TODO: 5. Использовать стиль snake_case (замечание общее)
def isfull():
    flag = True
    for i in board:
        if (i.count(' ') > 0):
            flag = False
    return flag


# Create the GUI of game board for play along with another player


def game_board_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


# Decide the next move of system


def pc():
    possible_move = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possible_move.append([i, j])
    # if possible_move == []:
    if not possible_move:
        return

    for let in ['O', 'X']:
        for i in possible_move:
            boardcopy = deepcopy(board)
            boardcopy[i[0]][i[1]] = let
            if winner(boardcopy, let):
                return i
    corner = []
    for i in possible_move:
        if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
            corner.append(i)
    if len(corner) > 0:
        move = random.randint(0, len(corner) - 1)
        return corner[move]
    edge = []
    for i in possible_move:
        if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
            edge.append(i)
    if len(edge) > 0:
        move = random.randint(0, len(edge) - 1)
        return edge[move]


# Configure text on button while playing with system


def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        messagebox.showinfo("Побеждает", "игрок")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        messagebox.showinfo("Побеждает", "компютер")
    elif (isfull()):
        gb.destroy()
        x = False
        messagebox.showinfo("Игра вничью", "Игра вничью")
    if (x):
        if sign % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)


# Create the GUI of game board for play along with system


def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()


# Initialize the game board to play with system


def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Крестики нолики приветствуют вас!")
    l1 = Button(game_board, text="Player : X", width=10)
    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Computer : O",
                width=10, state=DISABLED)

    l2.grid(row=2, column=1)
    gameboard_pc(game_board, l1, l2)


# Initialize the game board to play with another player


def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Крестики нолики приветствуют вас!")
    l1 = Button(game_board, text="Player 1 : X", width=10)

    l1.grid(row=1, column=1)
    l2 = Button(game_board, text="Player 2 : O",
                width=10, state=DISABLED)

    l2.grid(row=2, column=1)
    game_board_pl(game_board, l1, l2)


# main function


def play():
    menu = Tk()
    menu.geometry("300x300")
    menu.title("Крестики нолики приветствуют вас!")
    wpc = partial(withpc, menu)
    wpl = partial(withplayer, menu)

    head = Button(menu, text="Крестики нолики приветствуют вас!",
                  activeforeground='red',
                  activebackground="black", bg="red",
                  fg="black", width=500, font='summer', bd=5)

    B1 = Button(menu, text="Одиночный матч", command=wpc,
                activeforeground='red',
                activebackground="black", bg="red",
                fg="black", width=500, font='summer', bd=5)

    B2 = Button(menu, text="Игра с другом", command=wpl, activeforeground='red',
                activebackground="black", bg="red", fg="black",
                width=500, font='summer', bd=5)

    B3 = Button(menu, text="Выход", command=menu.quit, activeforeground='red',
                activebackground="yellow", bg="red", fg="black",
                width=500, font='summer', bd=5)
    head.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    B3.pack(side='top')
    menu.mainloop()


# Call main function
if __name__ == '__main__':
    play()
