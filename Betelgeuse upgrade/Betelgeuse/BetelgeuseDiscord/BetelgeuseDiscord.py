import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import json
import os

# Initialize the JSON file for users if it doesn't exist
if not os.path.exists("users.json"):
    with open("users.json", "w") as file:
        json.dump([], file)

# Initialize the JSON file for servers if it doesn't exist
if not os.path.exists("servers.json"):
    with open("servers.json", "w") as file:
        json.dump([], file)

# Function to load users from the JSON file
def load_users():
    with open("users.json", "r") as file:
        return json.load(file)

# Function to save a new user to the JSON file
def save_user(username, password):
    users = load_users()
    users.append({"username": username, "password": password})
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

# Function to load servers from the JSON file
def load_servers():
    with open("servers.json", "r") as file:
        return json.load(file)

# Function to save servers to the JSON file
def save_servers(servers):
    with open("servers.json", "w") as file:
        json.dump(servers, file, indent=4)

# Function to create a new server
def create_server():
    server_name = simpledialog.askstring("Create Server", "Enter server name:")
    if not server_name:
        return
    
    servers = load_servers()
    if any(server['name'] == server_name for server in servers):
        messagebox.showwarning("Error", "Server already exists!")
        return

    new_server = {
        "name": server_name,
        "messages": []
    }
    servers.append(new_server)
    save_servers(servers)
    refresh_server_list()

# Function to delete a server
def delete_server():
    server_name = server_listbox.get(tk.ACTIVE)
    if not server_name:
        return

    servers = load_servers()
    servers = [server for server in servers if server['name'] != server_name]
    save_servers(servers)
    refresh_server_list()

# Function to open a selected server
def open_server():
    global current_server
    server_name = server_listbox.get(tk.ACTIVE)
    if not server_name:
        return

    current_server = server_name
    root.destroy()  # Close the server management window
    open_chat_interface()  # Open the chat interface for the selected server

# Function to refresh the list of servers
def refresh_server_list():
    server_listbox.delete(0, tk.END)
    servers = load_servers()
    for server in servers:
        server_listbox.insert(tk.END, server['name'])

# Function to open the chat interface for the selected server
def open_chat_interface():
    def load_messages():
        servers = load_servers()
        for server in servers:
            if server['name'] == current_server:
                return server['messages']

    def save_message(username, message):
        servers = load_servers()
        for server in servers:
            if server['name'] == current_server:
                server['messages'].append({"username": username, "message": message})
        save_servers(servers)

    def refresh_messages():
        chat_window.config(state=tk.NORMAL)
        chat_window.delete(1.0, tk.END)
        messages = load_messages()
        for msg in messages:
            chat_window.insert(tk.END, f"{msg['username']}: {msg['message']}\n")
        chat_window.config(state=tk.DISABLED)

    def send_message():
        username = current_user
        message = message_entry.get()

        if not message:
            messagebox.showwarning("Input Error", "Message cannot be empty!")
            return

        save_message(username, message)
        message_entry.delete(0, tk.END)
        refresh_messages()

    # Tkinter GUI setup for the chat interface
    chat_root = tk.Tk()
    chat_root.title(f"Server: {current_server}")

    # Chat Window
    chat_window = scrolledtext.ScrolledText(chat_root, wrap=tk.WORD, state=tk.DISABLED, width=50, height=20)
    chat_window.pack(pady=10)

    # Message Entry
    message_label = tk.Label(chat_root, text="Message:")
    message_label.pack(pady=5)
    message_entry = tk.Entry(chat_root, width=50)
    message_entry.pack(pady=5)

    # Send Button
    send_button = tk.Button(chat_root, text="Send", command=send_message)
    send_button.pack(pady=10)

    # Initial loading of messages
    refresh_messages()

    # Start the Tkinter event loop
    chat_root.mainloop()

# Function to handle signup
def signup():
    username = signup_username_entry.get()
    password = signup_password_entry.get()
    
    if not username or not password:
        messagebox.showwarning("Input Error", "Username and password cannot be empty!")
        return
    
    users = load_users()
    if any(user['username'] == username for user in users):
        messagebox.showwarning("Signup Error", "Username already exists!")
        return

    save_user(username, password)
    messagebox.showinfo("Signup Successful", "You have successfully signed up!")
    signup_window.destroy()

# Function to handle login
def login():
    global current_user
    username = login_username_entry.get()
    password = login_password_entry.get()

    if not username or not password:
        messagebox.showwarning("Input Error", "Username and password cannot be empty!")
        return

    users = load_users()
    for user in users:
        if user['username'] == username and user['password'] == password:
            current_user = username
            messagebox.showinfo("Login Successful", f"Welcome {username}!")
            login_window.destroy()
            open_server_management()  # Open server management after login
            return
    
    messagebox.showerror("Login Error", "Invalid username or password!")

# Function to open the signup window
def open_signup_window():
    global signup_username_entry, signup_password_entry, signup_window

    signup_window = tk.Toplevel(root)
    signup_window.title("Signup")
    
    tk.Label(signup_window, text="Username:").pack(pady=5)
    signup_username_entry = tk.Entry(signup_window, width=30)
    signup_username_entry.pack(pady=5)
    
    tk.Label(signup_window, text="Password:").pack(pady=5)
    signup_password_entry = tk.Entry(signup_window, show="*", width=30)
    signup_password_entry.pack(pady=5)
    
    tk.Button(signup_window, text="Signup", command=signup).pack(pady=20)

# Function to open the login window
def open_login_window():
    global login_username_entry, login_password_entry, login_window

    login_window = tk.Toplevel(root)
    login_window.title("Login")
    
    tk.Label(login_window, text="Username:").pack(pady=5)
    login_username_entry = tk.Entry(login_window, width=30)
    login_username_entry.pack(pady=5)
    
    tk.Label(login_window, text="Password:").pack(pady=5)
    login_password_entry = tk.Entry(login_window, show="*", width=30)
    login_password_entry.pack(pady=5)
    
    tk.Button(login_window, text="Login", command=login).pack(pady=20)

# Function to open the server management interface after login
def open_server_management():
    global root, server_listbox

    root = tk.Tk()
    root.title("Server Management")

    # Server Listbox
    server_listbox = tk.Listbox(root, width=50, height=20)
    server_listbox.pack(pady=10)

    # Create, Delete, and Open Server Buttons
    create_button = tk.Button(root, text="Create Server", command=create_server)
    create_button.pack(pady=5)
    delete_button = tk.Button(root, text="Delete Server", command=delete_server)
    delete_button.pack(pady=5)
    open_button = tk.Button(root, text="Open Server", command=open_server)
    open_button.pack(pady=5)

    # Initial loading of servers
    refresh_server_list()

    # Start the Tkinter event loop for the server management interface
    root.mainloop()

# Tkinter GUI setup for login/signup interface
root = tk.Tk()
root.title("Login or Signup")

# Login and Signup Buttons
tk.Button(root, text="Login", command=open_login_window).pack(pady=10)
tk.Button(root, text="Signup", command=open_signup_window).pack(pady=10)

# Start the Tkinter event loop for the initial interface
root.mainloop()
