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
root.configure(bg="#0D1117")
root.iconbitmap("icon.ico")
root.resizable(False, False)


# Create a label with the welcome message and set the font size
welcome = tk.Label(root, text=f"Freshy", fg="white", bg="#0D1117", font=("Arial", font_size))

# Calculate the center position of the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Place the label at the center of the window
welcome.place(relx=0.5, rely=0.5, anchor="center")
slogan = tk.Label(root, text=f"Setup a fresh windows OS with easy", fg="white", bg="#0D1117", font=("Arial", 25))
slogan.place(relx=0.5, rely=0.70, anchor="center")


# Schedule the disappearance of the label after 5 seconds
def hide_welcome():
    welcome.destroy()
    slogan.destroy()
    
root.after(5000, hide_welcome)

# Define the URLs for each image
discord_url = "https://discord.gg/8WyFZF3kqn"
github_url = "https://github.com/unofficialdxnny/Freshy"
instagram_url = "https://www.instagram.com/unofficialdxnny"

# Load the images
discord_img = tk.PhotoImage(file="discord.png")
github_img = tk.PhotoImage(file="github.png")
instagram_img = tk.PhotoImage(file="instagram.png")

# Define the labels for each image
discord_label = tk.Label(root, image=discord_img, bd=0, cursor="hand2")
github_label = tk.Label(root, image=github_img, bd=0, cursor="hand2")
instagram_label = tk.Label(root, image=instagram_img, bd=0, cursor="hand2")

# Define the click events for each label
def open_discord(event):
    
    import webbrowser
    webbrowser.open_new(discord_url)

def open_github(event):
    
    import webbrowser
    webbrowser.open_new(github_url)

def open_instagram(event):
    
    import webbrowser
    webbrowser.open_new(instagram_url)

discord_label.bind("<Button-1>", open_discord)
github_label.bind("<Button-1>", open_github)
instagram_label.bind("<Button-1>", open_instagram)

# Place the labels on the canvas
discord_label.place(relx=0.8, rely=0.9, anchor="center")
github_label.place(relx=0.95, rely=0.9, anchor="center")
instagram_label.place(relx=0.2, rely=0.9, anchor="center")

root.mainloop()