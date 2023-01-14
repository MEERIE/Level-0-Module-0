from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    window = Tk()
    
    window.withdraw()
    
    # 1. Ask the user if they know how to write code.
    code = simpledialog.askstring(title=None, prompt="Do you know how to code? Or are you Dumb")
    # 2. If they say "yes", tell them they will rule the world in a message box pop-up.
    if code=="yes":
        messagebox.showinfo(title=None, message="You shall rule the world")
    if code=="no":
        messagebox.showinfo(title=None, message="You are dumb, sign up for classes at the league")
    # 3. Otherwise, tell them to sign up for classes at The League in an error box pop-up.
    
    # Run the window's .mainloop() method
    window.mainloop()
