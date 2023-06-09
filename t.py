import tkinter as tk
import subprocess


root = tk.Tk()

# Get the width and height of the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the appropriate window size and font size
window_width = 1500
window_height = 600
font_size = int(screen_height * 0.1)

root.geometry(f"{window_width}x{window_height}")
root.title("Freshy")
root.configure(bg="#694966")
root.iconbitmap("icon.ico")
root.resizable(False, False)


# Create a label with the welcome message and set the font size
welcome = tk.Label(root, text=f"Freshy", fg="white", bg="#694966", font=("Arial", font_size))

# Calculate the center position of the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Place the label at the center of the window
welcome.place(relx=0.5, rely=0.5, anchor="center")
slogan = tk.Label(root, text=f"Setup a fresh windows OS with easy", fg="white", bg="#694966", font=("Arial", 25))
slogan.place(relx=0.5, rely=0.70, anchor="center")


def main_screen():
    # Create a new label with the text and font size
    label = tk.Label(root, text="The #1 Windows Setup Automator", fg="white", bg="#694966", font=("Arial", 10))
    # Place the label at the top-middle of the screen
    label.place(relx=0.05, rely=0, anchor="n")
    
   

# Schedule the disappearance of the label after 5 seconds
def hide_welcome():
    welcome.destroy()
    slogan.destroy()
    main_screen()



    
root.after(5000, hide_welcome)


root.mainloop()
