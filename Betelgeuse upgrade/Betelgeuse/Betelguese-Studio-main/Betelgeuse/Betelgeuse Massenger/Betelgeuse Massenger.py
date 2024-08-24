import tkinter as tk
import tkinter
import json
from tkinter import messagebox



# Load user data
def load_users():
    try:
        with open('credentials.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save user data
def save_users(users):
    with open('credentials.json', 'w') as file:
        json.dump(users, file)

# Signup function
def signup():
    username = entry_username.get()
    password = entry_password.get()
    if username and password:
        users = load_users()
        if username in users:
            messagebox.showerror("Error", "Username already exists!")
        else:
            users[username] = password
            save_users(users)
            messagebox.showinfo("Success", "Signup successful! Please login.")
            login_screen()
    else:
        messagebox.showerror("Error", "Please fill in all fields!")

# Login function
def login():
    global logged_in_user
    username = entry_username.get()
    password = entry_password.get()
    users = load_users()
    if username in users and users[username] == password:
        logged_in_user = username  # Store the logged-in username in the variable
        messagebox.showinfo("Success", "Login successful!")
        messenger_screen()
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# Show login screen
def login_screen():
    clear_window()
    global entry_username, entry_password
    tk.Label(window, text="Login", font=("Arial", 16), bg="gray", fg="white").pack(pady=20)
    tk.Label(window, text="Username:", bg="gray", fg="white").pack()
    entry_username = tk.Entry(window)
    entry_username.pack(pady=5)
    tk.Label(window, text="Password:", bg="gray", fg="white").pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack(pady=5)
    tk.Button(window, text="Login", command=login, bg="white", fg="black").pack(pady=10)
    tk.Button(window, text="Signup", command=signup_screen, bg="white", fg="black").pack(pady=5)

# Show signup screen
def signup_screen():
    clear_window()
    global entry_username, entry_password
    tk.Label(window, text="Signup", font=("Arial", 16), bg="gray", fg="white").pack(pady=20)
    tk.Label(window, text="Username:", bg="gray", fg="white").pack()
    entry_username = tk.Entry(window)
    entry_username.pack(pady=5)
    tk.Label(window, text="Password:", bg="gray", fg="white").pack()
    entry_password = tk.Entry(window, show="*")
    entry_password.pack(pady=5)
    tk.Button(window, text="Signup", command=signup, bg="white", fg="black").pack(pady=10)
    tk.Button(window, text="Back to Login", command=login_screen, bg="white", fg="black").pack(pady=5)

# Show messenger screen
def messenger_screen():
    clear_window()

    # Create a frame for the messages
    message_frame = tk.Frame(window, bg="white")
    message_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(message_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Create a text widget for displaying messages
    message_display = tk.Text(message_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, bg="white", fg="black")
    message_display.pack(fill=tk.BOTH, expand=True)
    scrollbar.config(command=message_display.yview)
    message_display.config(state=tk.DISABLED)

    # Create an entry widget for typing messages
    message_entry = tk.Entry(window, bg="white", fg="black", font=("Arial", 14))
    message_entry.pack(fill=tk.X, padx=10, pady=5)

    # Function to send a message
    def send_message():
        message = message_entry.get()
        if message:
            message_display.config(state=tk.NORMAL)
            message_display.insert(tk.END, f"{logged_in_user}: " + message + "\n")
            message_display.config(state=tk.DISABLED)
            message_entry.delete(0, tk.END)
            # Simulate receiving a response
            window.after(1000, receive_message, "howd can yo help y'all? amigo!")

    # Function to receive a message
    def receive_message(msg):
        message_display.config(state=tk.NORMAL)
        message_display.insert(tk.END,  ">> " + msg + "\n")
        message_display.config(state=tk.DISABLED)

    # Create a send button
    send_button = tk.Button(window, text="Send", command=send_message, bg="white", fg="black", font=("Arial", 12))
    send_button.pack(pady=10)

# Clear the window for new screens
def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

# Create the main window
window = tk.Tk()
window.title("Bonjour Messenger")
window.geometry("368x600")
window.config(bg="gray")
icon_path = r'C:\Users\Vivek bhimrao shinde\Downloads\mango_icon.ico'
window.iconbitmap(icon_path)

# Start with the login screen
logged_in_user = None  # Initialize the variable to store the username
login_screen()

# Run the application
window.mainloop()
