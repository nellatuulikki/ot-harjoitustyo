from tkinter import Tk
from ui.ui import Ui


def main():

    window = Tk()
    window.title('Tic-Tac-Toe')
    ui = Ui(window)
    ui.start()
    window.mainloop()


if __name__ == '__main__':
    main()
