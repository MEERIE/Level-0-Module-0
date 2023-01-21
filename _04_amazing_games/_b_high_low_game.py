from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print(num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(10):
        # 4. Ask the user for a guess using a pop-up window, and save their response
        hi = simpledialog.askinteger(title=None, prompt="Guess a number between 1 and 100")
        # 5. If the guess is correct
        if hi == num:
            # 6. Win. Use 'sys.exit(0)' to end the program
            sys.exit(0)
        # 7. if the guess is high
        if hi > num:
            simpledialog.askstring(title=None, prompt="try again: lower")
            # 8. Tell them it's too high
        # 9. Else if the guess is low
            # 10. Tell them it's too low
        if hi < num:
            simpledialog.askstring(title=None, prompt="try again: higher")
    window.mainloop()
    messagebox.showinfo("YOU LOSE")
