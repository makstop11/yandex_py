import tkinter as tk
from random import shuffle
from tkinter.messagebox import showinfo

colors = {
    0: 'white',
    1: 'blue',
    2: 'green',
    3: '#00FFB9',
    4: '#FF0000',
    5: '#FFD500',
    6: '#4200FF',
    7: '#D500FF',
    8: '#FF00AE',
}


class MyButton(tk.Button):

    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font='Calibri 15 bold', *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
        self.count_bomb = 0
        self.is_open = False

    def __repr__(self):
        return f'MyButton{self.x} {self.y} {self.number} {self.is_mine}'


class MineSweeper:
    window = tk.Tk()
    row = 7
    columns = 10
    MINES = 10
    IS_GAME_OVER = False
    IS_FIRST_CLICK = True

    def __init__(self):
        self.buttons = []
        for i in range(MineSweeper.row + 2):
            temp = []
            for j in range(MineSweeper.columns + 2):
                btn = MyButton(MineSweeper.window, x=i, y=j)
                btn.config(command=lambda button=btn: self.clik(button))
                temp.append(btn)
            self.buttons.append(temp)

    def clik(self, cliked_button: MyButton):
        if MineSweeper.IS_GAME_OVER:
            return
        if cliked_button.is_mine:
            cliked_button.config(text='*', background='red', disabledforeground='black')
            cliked_button.is_open = True
            MineSweeper.IS_GAME_OVER = True
            showinfo('Game over', 'ВЫ проиграли')
            for i in range(1, MineSweeper.row + 1):
                for j in range(1, MineSweeper.columns + 1):
                    btn = self.buttons[i][j]
                    if btn.is_mine:
                        btn['text'] = '*'
        else:
            color = colors.get(cliked_button.count_bomb, 'black')
            if cliked_button.count_bomb:
                cliked_button.config(text=cliked_button.count_bomb, disabledforeground=color)
                cliked_button.is_open = True
            else:
                self.breadth_first_search(cliked_button)
        cliked_button.config(state='disabled')
        cliked_button.config(relief=tk.SUNKEN)

    # def breadth_first_search(self, btn: MyButton):
    #     queue = [btn]
    #     while queue:
    #         cur_btn = queue.pop()
    #         color = colors.get(cur_btn.count_bomb, 'black')
    #         if cur_btn.count_bomb:
    #             cur_btn.config(text=cur_btn.count_bomb, disabledforeground=color)
    #         else:
    #             cur_btn.config(text='', disabledforeground=color)
    #         cur_btn.is_open = True
    #         cur_btn.config(state='disabled')
    #         cur_btn.config(relief=tk.SUNKEN)
    #         if cur_btn.count_bomb == 0:
    #             for dx in [-1, 0, 1]:
    #                 for dy in [-1, 0, 1]:
    #                      if not abs(dx - dy) == 1:
    #                          continue
    #                     next_btn = self.buttons[x + dx][y + dy]
    #                     if not next_btn.is_open and 1 <= next_btn.x <= MineSweeper.row and \
    #                             1 <= next_btn.y <= MineSweeper.columns and next_btn not in queue:
    #                         queue.append(next_btn)

    def reload(self):
        [child.destroy() for child in self.window.winfo_children()]
        self.__init__()
        self.create_widgets()
        MineSweeper.IS_FIRST_CLICK = True

    def create_settings_win(self):
        win_settings = tk.Toplevel(self.window)
        win_settings.wm_title('Настройки')
        tk.Label(win_settings, text='Количество строк').grid(row=0, column=0)
        row_entry = tk.Entry(win_settings)
        row_entry.insert(0, MineSweeper.row)
        row_entry.grid(row=0, column=1, padx=20, pady=20)
        tk.Label(win_settings, text='Количество колонок').grid(row=1, column=0)
        columns_entry = tk.Entry(win_settings)
        columns_entry.insert(0, MineSweeper.columns)
        columns_entry.grid(row=1, column=1, padx=20, pady=20)
        tk.Label(win_settings, text='Количество мин').grid(row=2, column=0)
        mines_entry = tk.Entry(win_settings)
        mines_entry.insert(0, MineSweeper.MINES)
        mines_entry.grid(row=2, column=1, padx=20, pady=20)
        tk.Button(win_settings, text='Сохранить изменения',
                  command=lambda: self.change_settings(row_entry, columns_entry, mines_entry))

    def change_settings(self, row: tk.Entry, column: tk.Entry, mines: tk.Entry):
        MineSweeper.row = int(row.get())
        MineSweeper.columns = int(column.get())
        MineSweeper.MINES = int(mines.get())
        self.reload()

    def create_widgets(self):
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)
        settings_menu = tk.Menu(self.window)
        settings_menu = tk.Menu(menubar)
        # settings_menu.add_command(label='Играть', command=self.reload)
        settings_menu.add_command(label='Настройки', command=self.create_settings_win)
        settings_menu.add_command(label='Выход', command=self.window.destroy)
        menubar.add_cascade(label='Файл', menu=settings_menu)
        count = 1
        for i in range(1, MineSweeper.row + 1):
            for j in range(1, MineSweeper.columns + 1):
                btn = self.buttons[i][j]
                btn.number = count
                btn.grid(row=i, column=j, stick='NWES')
                count += 1
        for i in range(1, MineSweeper.row + 1):
            tk.Grid.rowconfigure(self.window, i, weight=1)
        for i in range(1, MineSweeper.columns + 1):
            tk.Grid.columnconfigure(self.window, i, weight=1)

    def open_all_buttons(self):
        for i in range(MineSweeper.row + 2):
            for j in range(MineSweeper.columns + 2):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    btn.config(text='*', background='red', disabledforeground='black')
                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, 'black')
                    btn.config(text=btn.count_bomb, fg=color)

    def start(self):
        self.create_widgets()
        self.insert_mines()
        self.count_mines_in_buttons()
        self.print_buttons()
        # self.open_all_buttons()
        MineSweeper.window.mainloop()

    def print_buttons(self):
        for i in range(1, MineSweeper.row + 1):
            for j in range(1, MineSweeper.columns + 1):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    print('B', end='')
                else:
                    print(btn.count_bomb, end='')
            print()

    def insert_mines(self):
        index_mines = self.get_mines_places()
        print(index_mines)
        count = 1
        for i in range(1, MineSweeper.row + 1):
            for j in range(1, MineSweeper.columns + 1):
                btn = self.buttons[i][j]
                btn.number = count
                if btn.number in index_mines:
                    btn.is_mine = True
                count += 1

    def count_mines_in_buttons(self):
        for i in range(1, MineSweeper.row + 1):
            for j in range(1, MineSweeper.columns + 1):
                btn = self.buttons[i][j]
                count_bomb = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neighbour = self.buttons[i + row_dx][j + col_dx]
                            if neighbour.is_mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb

    @staticmethod
    def get_mines_places():
        indexes = list(range(1, MineSweeper.columns * MineSweeper.row + 1))
        shuffle(indexes)
        return indexes[:MineSweeper.MINES]


game = MineSweeper()
game.start()
