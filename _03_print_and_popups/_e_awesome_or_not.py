from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    num = random.randint(0,3)
    print(num)

    user_input = simpledialog.askstring(title=None, prompt="Enter something you think is awesome")

    if num == 0:
        messagebox.showerror(tile=None, message=user_input + " is awesome!")
    elif num == 1:
        print(f"{user_input} is ok.")
    elif num == 2:
        print(f"{user_input} is boring.")
    elif num == 3:
        print(f"{user_input} is unique and interesting.")

    window.mainloop()
