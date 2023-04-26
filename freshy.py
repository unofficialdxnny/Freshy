import tkinter as tk

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
root.configure(bg="#0D1117")
root.iconbitmap("icon.ico")

# Create a label with the welcome message and set the font size
welcome = tk.Label(root, text=f"Welcome To Freshy", fg="white", bg="#0D1117", font=("Arial", font_size))

# Calculate the center position of the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Place the label at the center of the window
welcome.place(relx=0.5, rely=0.5, anchor="center")

# Schedule the disappearance of the label after 5 seconds
def hide_welcome():
    welcome.destroy()

root.after(5000, hide_welcome)

root.mainloop()