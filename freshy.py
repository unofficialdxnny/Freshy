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

    # Create a frame to hold the cards
    cards_frame = tk.Frame(root, bg="#f2f2f2", padx=20, pady=20)
    cards_frame.pack()

# Define a function to run the command in the terminal
    def run_command(command):
        subprocess.run(command, shell=True)

    # Define a list of dictionaries containing card information
    cards_data = [
        {
            "image": "path/to/image1.png",
            "text": "Card 1 text",
            "command": "echo 'Card 1 button clicked'"
        },
        {
            "image": "path/to/image2.png",
            "text": "Card 2 text",
            "command": "echo 'Card 2 button clicked'"
        },
        {
            "image": "path/to/image3.png",
            "text": "Card 3 text",
            "command": "echo 'Card 3 button clicked'"
        }
    ]

# Loop through the list of cards data and create a card for each one
    for i, card_data in enumerate(cards_data):
        # Create a frame for the card
        card_frame = tk.Frame(cards_frame, bg="#ffffff", padx=10, pady=10, bd=1, relief="solid")
        card_frame.grid(row=0, column=i, padx=10, pady=10)

        # Create a label for the image
        card_image = tk.PhotoImage(file=card_data["image"])
        image_label = tk.Label(card_frame, image=card_image, bg="#ffffff")
        image_label.pack()

        # Create a label for the text
        text_label = tk.Label(card_frame, text=card_data["text"], font=("Helvetica", 14), bg="#ffffff")
        text_label.pack(pady=(10,0))

        # Create a button to run the command
        command_button = tk.Button(card_frame, text="Install", command=lambda command=card_data["command"]: run_command(command))
        command_button.pack(pady=(10,0))


def hide_welcome():
    welcome.destroy()
    slogan.destroy()
    main_screen()



    
root.after(5000, hide_welcome)


root.mainloop()
