from tkinter import Tk
from ui.play_view import Tic_tac_toe_UI
import os


def main():
    window = Tk()
    window.title('Tic Tac Toe game')
    ui = Tic_tac_toe_UI(window)

    ui.start()
    window.mainloop()


if __name__ == '__main__':
    main()