import tkinter
import json
from pathlib import Path
from tkinter import messagebox
from tkinter import Canvas, Tk
import os
import time

json_file_path = Path.home() / 'insta_login_data.json'

if json_file_path.exists():
    with open(json_file_path, 'r') as f:
        users = json.load(f)
else:
    users = {}

current_user = None

def save_data():
    with open(json_file_path, 'w') as f:
        json.dump(users, f, indent=4)

def do():
    y = tkinter.Tk()
    y.title("About Betelgeuse")
    y.geometry("600x600")
    
    u = tkinter.Label(y, text="""Betelgeuse is an amazing software that stands out with its myriad of features,\n
providing an unparalleled user experience across various domains.\n
Its versatile functionality makes it a powerhouse for professionals and enthusiasts alike.\n
The software is equipped with advanced tools for data analysis, allowing users to perform complex computations with ease.\n
Its intuitive interface ensures that even beginners can navigate through its numerous capabilities without hassle.\n
\n
The integration of real-time collaboration features enables teams to work together seamlessly, sharing insights and progress instantly.\n
Additionally, Betelgeuse boasts robust security measures, ensuring that user data remains protected against unauthorized access.\n
The software's modular architecture allows for easy customization, enabling users to tailor the application to their specific needs.\n
\n
Whether you're engaged in software development, data science, or creative projects, Betelgeuse provides a comprehensive suite of tools designed to enhance productivity and creativity.\n
The frequent updates and active community support ensure that users always have access to the latest features and improvements.\n
\n
With its high performance and reliability, Betelgeuse has earned a reputation as a leading software solution in its category,\n
setting new standards for excellence and innovation.\n
Its adaptability and feature-rich design make it an invaluable asset for anyone seeking to leverage cutting-edge technology to achieve their goals efficiently and effectively.\n
\n
Betelgeuse's rich set of features includes everything from advanced analytics to intuitive design tools,\n
making it the go-to choice for a wide range of applications.\n
Its user-friendly interface combined with powerful functionality ensures that both novice and expert users can make the most out of its capabilities.\n
\n
In summary, Betelgeuse is not just a tool but a comprehensive solution that addresses the needs of modern users.\n
Its continuous evolution and commitment to excellence make it a standout choice in the software industry,\n
providing unparalleled value to its users.""", font=("Helvetica", 10, "bold"))
    u.pack(pady=10, padx=10)
    
    button = tkinter.Button(y, text="Close", command=y.destroy)
    button.pack(pady=20)
    
    y.mainloop()

def do2():
    z = tkinter.Tk()
    z.title("Create Package")
    z.geometry("400x300")

    text = tkinter.Text(z)
    text.pack(expand=True, fill='both')

    def save_content():
        content = text.get("1.0", "end-1c")
        documents_path = os.path.expanduser("~/Documents")
        file_path = os.path.join(documents_path, "betelgeuse_package.txt")
        with open(file_path, 'w') as file:
            file.write(content)
        messagebox.showinfo("Save Successful", "Content saved to betelgeuse_package.txt")

    save_button = tkinter.Button(z, text="Save", command=save_content)
    save_button.pack(pady=10)

    z.mainloop()

def main():
    global current_user
    x = tkinter.Tk()
    x.title("Betelgeuse Main Window")
    x.geometry("600x450")
    
    t = tkinter.Label(x, text=f"Welcome, {current_user}! to The Betelgeuse Explore", font=("Helvetica", 20, "bold"))
    t.pack(pady=10)
    
    canvas = tkinter.Canvas(x, width=200, height=200, bg='white')
    canvas.pack()
    
    canvas.create_oval(40, 40, 160, 160, fill='#0078D4', outline='#0078D4')
    canvas.create_arc(30, 30, 170, 170, start=45, extent=270, outline='#F1C40F', width=4)
    canvas.create_arc(30, 30, 170, 170, start=45, extent=120, outline='#F1C40F', width=4)
    canvas.create_arc(20, 20, 180, 180, start=30, extent=120, outline='#F1C40F', width=3)
    canvas.create_arc(20, 20, 180, 180, start=150, extent=120, outline='#F1C40F', width=3)
    canvas.create_oval(80, 80, 120, 120, fill='white', outline='#0078D4')
    canvas.create_arc(70, 70, 130, 130, start=60, extent=150, style='arc', outline='#F1C40F', width=3)
    canvas.create_arc(70, 70, 130, 130, start=210, extent=150, style='arc', outline='#F1C40F', width=3)

    button = tkinter.Button(x, text="Explore Help", command=do)
    button.pack(pady=10)

    button2 = tkinter.Button(x, text="Explore Create Directory", command=do2)
    button2.pack(pady=10)

    button3 = tkinter.Button(x, text="Settings", command=open_settings)
    button3.pack(pady=10)
    
    button4 = tkinter.Button(x, text="Logout", command=logout)
    button4.pack(pady=10)
    
    x.mainloop()

def open_settings():
    settings_window = tkinter.Tk()
    settings_window.title("Settings")
    settings_window.geometry("300x200")

    def save_settings():
        # Dummy implementation for saving settings
        messagebox.showinfo("Settings Saved", "Settings have been saved!")

    label = tkinter.Label(settings_window, text="Settings Page")
    label.pack(pady=10)

    save_button = tkinter.Button(settings_window, text="Save Settings", command=save_settings)
    save_button.pack(pady=20)

    settings_window.mainloop()

def view_profile():
    global current_user
    profile_window = tkinter.Tk()
    profile_window.title("Profile")
    profile_window.geometry("300x200")

    def update_profile():
        new_username = username_entry.get()
        if new_username:
            users[new_username] = users.pop(current_user)
            save_data()
            current_user = new_username
            messagebox.showinfo("Profile Updated", "Profile updated successfully!")
            profile_window.destroy()
            main()

    label = tkinter.Label(profile_window, text=f"Profile: {current_user}")
    label.pack(pady=10)

    username_entry = tkinter.Entry(profile_window, width=30)
    username_entry.pack(pady=5)

    update_button = tkinter.Button(profile_window, text="Update Profile", command=update_profile)
    update_button.pack(pady=20)

    profile_window.mainloop()

def view_recent_activities():
    activities_window = tkinter.Tk()
    activities_window.title("Recent Activities")
    activities_window.geometry("400x300")

    activities = tkinter.Text(activities_window)
    activities.pack(expand=True, fill='both')

    activities.insert("end", "Recent Activities:\n")
    activities.insert("end", "Login from IP 192.168.1.1\n")
    activities.insert("end", "Password change on 2024-08-11\n")

    activities_window.mainloop()

def password_recovery():
    recovery_window = tkinter.Tk()
    recovery_window.title("Password Recovery")
    recovery_window.geometry("300x200")

    def recover_password():
        username = username_entry.get()
        if username in users:
            messagebox.showinfo("Password Recovery", f"Password recovery email sent to {username}!")
            recovery_window.destroy()
        else:
            messagebox.showwarning("Error", "Username not found")

    label = tkinter.Label(recovery_window, text="Enter your username")
    label.pack(pady=10)

    username_entry = tkinter.Entry(recovery_window, width=30)
    username_entry.pack(pady=5)

    recover_button = tkinter.Button(recovery_window, text="Recover Password", command=recover_password)
    recover_button.pack(pady=20)

    recovery_window.mainloop()

def logout():
    global current_user
    current_user = None
    create_login_signup_window()

def search_users():
    search_window = tkinter.Tk()
    search_window.title("Search Users")
    search_window.geometry("300x200")

    def search():
        query = search_entry.get()
        results = [user for user in users if query.lower() in user.lower()]
        results_text.delete("1.0", "end")
        if results:
            results_text.insert("end", "\n".join(results))
        else:
            results_text.insert("end", "No users found.")

    label = tkinter.Label(search_window, text="Search for users")
    label.pack(pady=10)

    search_entry = tkinter.Entry(search_window, width=30)
    search_entry.pack(pady=5)

    search_button = tkinter.Button(search_window, text="Search", command=search)
    search_button.pack(pady=10)

    results_text = tkinter.Text(search_window, height=6)
    results_text.pack(pady=10)

    search_window.mainloop()

def create_login_signup_window():
    global current_user
    window = tkinter.Tk()
    window.title("Betelgeuse Login")
    window.geometry("300x400")
    window.configure(bg="#fafafa")

    def handle_login():
        global current_user
        username = username_entry.get()
        password = password_entry.get()
        if users.get(username) == password:
            current_user = username
            window.destroy()
            main()
        else:
            h = tkinter.Label(window, text="Invalid Username or Password", fg="Red")
            h.pack(pady=5)

    def handle_signup():
        username = username_entry.get()
        password = password_entry.get()
        if username in users:
            h = tkinter.Label(window, text="Signup Error: Username already exists", fg="Red")
            h.pack(pady=5)
        else:
            users[username] = password
            save_data()
            messagebox.showinfo("Sign Up Success", f"Account created for {username}!")

    username_label = tkinter.Label(window, text="Username", bg="#fafafa")
    username_label.pack(pady=5)
    username_entry = tkinter.Entry(window, width=30)
    username_entry.pack(pady=5)

    password_label = tkinter.Label(window, text="Password", bg="#fafafa")
    password_label.pack(pady=5)
    password_entry = tkinter.Entry(window, show="*", width=30)
    password_entry.pack(pady=5)

    login_button = tkinter.Button(window, text="Log In", bg="#0095f6", fg="white", command=handle_login)
    login_button.pack(pady=20)

    signup_button = tkinter.Button(window, text="Sign Up", bg="#0095f6", fg="white", command=handle_signup)
    signup_button.pack(pady=10)

    forgot_password_button = tkinter.Button(window, text="Forgot Password", command=password_recovery)
    forgot_password_button.pack(pady=10)

    search_button = tkinter.Button(window, text="Search Users", command=search_users)
    search_button.pack(pady=10)

    footer = tkinter.Label(window, text="©2024 Betelgeuse Inc.", bg="#fafafa", fg="gray")
    footer.pack(side="bottom", pady=5)

    window.mainloop()

create_login_signup_window()
