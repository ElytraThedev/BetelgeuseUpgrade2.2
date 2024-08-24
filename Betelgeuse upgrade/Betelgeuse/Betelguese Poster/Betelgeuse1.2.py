import tkinter as tk
from tkinter import messagebox, font, simpledialog, filedialog
import json
import os

# Data file path
DATA_FILE = 'user_data.json'

# Load or initialize user data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as f:
        users = json.load(f)
else:
    users = {}
# Betelgeuse
current_user = None

def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump(users, f, indent=4)

def create_login_window():
    global current_user

    window = tk.Tk()
    window.title("Betelgeuse Login")
    window.geometry("600x600")
    window.configure(bg="#f7f7f7")

    custom_font = font.Font(family="Arial", size=12)

    def handle_login():
        username = username_entry.get()
        password = password_entry.get()

        global current_user
        current_user = users.get(username)

        if current_user and current_user["password"] == password:
            window.withdraw()
            create_main_window()
        else:
            messagebox.showwarning("Login Error", "Invalid username or password.")

    def handle_signup():
        window.withdraw()
        create_signup_window()

    header_label = tk.Label(window, text="Betelgeuse", font=("Arial", 24, "bold"), bg="#f7f7f7")
    header_label.pack(pady=20)

    username_label = tk.Label(window, text="Username", font=custom_font, bg="#f7f7f7")
    username_label.pack(pady=5)
    username_entry = tk.Entry(window, width=50, font=custom_font)
    username_entry.pack(pady=5)

    password_label = tk.Label(window, text="Password", font=custom_font, bg="#f7f7f7")
    password_label.pack(pady=5)
    password_entry = tk.Entry(window, show="*", width=50, font=custom_font)
    password_entry.pack(pady=5)

    login_button = tk.Button(window, text="Log In", bg="#0095f6", fg="white", font=custom_font, width=50, command=handle_login)
    login_button.pack(pady=20)

    signup_frame = tk.Frame(window, bg="#f7f7f7")
    signup_frame.pack(pady=20)

    signup_label = tk.Label(signup_frame, text="Don't have an account?", bg="#f7f7f7", font=custom_font)
    signup_label.pack(side=tk.LEFT)

    signup_button = tk.Button(signup_frame, text="Sign Up", bg="#0095f6", fg="white", font=custom_font, command=handle_signup)
    signup_button.pack(side=tk.LEFT, padx=5)

    footer_frame = tk.Frame(window, bg="#f7f7f7")
    footer_frame.pack(side=tk.BOTTOM, pady=10)

    footer_label = tk.Label(footer_frame, text="© 2024 Betelgeuse", bg="#f7f7f7", font=("Arial", 10))
    footer_label.pack()

    window.mainloop()

def create_signup_window():
    signup_window = tk.Toplevel()
    signup_window.title("Betelgeuse Sign Up")
    signup_window.geometry("600x600")
    signup_window.configure(bg="#f7f7f7")

    custom_font = font.Font(family="Arial", size=12)

    def handle_signup():
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()

        if not username or not password or not email:
            messagebox.showwarning("Input Error", "All fields are required.")
            return

        if username in users:
            messagebox.showwarning("Signup Error", "Username already exists.")
            return

        users[username] = {
            "password": password,
            "email": email,
            "bio": "",
            "profile_picture": None,
            "posts": [],
            "followers": [],
            "following": [],
            "notifications": []
        }
        save_data()
        messagebox.showinfo("Sign Up Success", f"Account created for {username}!")
        signup_window.withdraw()
        create_login_window()

    header_label = tk.Label(signup_window, text="Create Account", font=("Arial", 24, "bold"), bg="#f7f7f7")
    header_label.pack(pady=20)

    username_label = tk.Label(signup_window, text="Username", font=custom_font, bg="#f7f7f7")
    username_label.pack(pady=5)
    username_entry = tk.Entry(signup_window, width=50, font=custom_font)
    username_entry.pack(pady=5)

    password_label = tk.Label(signup_window, text="Password", font=custom_font, bg="#f7f7f7")
    password_label.pack(pady=5)
    password_entry = tk.Entry(signup_window, show="*", width=50, font=custom_font)
    password_entry.pack(pady=5)

    email_label = tk.Label(signup_window, text="Email", font=custom_font, bg="#f7f7f7")
    email_label.pack(pady=5)
    email_entry = tk.Entry(signup_window, width=50, font=custom_font)
    email_entry.pack(pady=5)

    signup_button = tk.Button(signup_window, text="Sign Up", bg="#0095f6", fg="white", font=custom_font, width=50, command=handle_signup)
    signup_button.pack(pady=20)

    back_button = tk.Button(signup_window, text="Back to Login", bg="#0095f6", fg="white", font=custom_font, width=50, command=lambda: [signup_window.withdraw(), create_login_window()])
    back_button.pack(pady=10)

    signup_window.mainloop()

def create_main_window():
    main_window = tk.Toplevel()
    main_window.title("Betelgeuse Feed")
    main_window.geometry("800x600")
    main_window.configure(bg="#f7f7f7")

    custom_font = font.Font(family="Arial", size=12)

    def add_post():
        post_content = simpledialog.askstring("New Post", "Enter post content:")
        if post_content:
            file_path = filedialog.askopenfilename(title="Select an image (optional)", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
            post = {"content": post_content, "comments": [], "likes": 0, "image": file_path}
            current_user["posts"].append(post)
            save_data()
            update_feed()

    def delete_post(index):
        del current_user["posts"][index]
        save_data()
        update_feed()

    def add_comment(index):
        comment_content = simpledialog.askstring("New Comment", "Enter comment content:")
        if comment_content:
            current_user["posts"][index]["comments"].append(comment_content)
            save_data()
            update_feed()

    def like_post(index):
        current_user["posts"][index]["likes"] += 1
        save_data()
        update_feed()

    def update_feed():
        for widget in feed_frame.winfo_children():
            widget.destroy()

        for i, post in enumerate(current_user["posts"]):
            post_frame = tk.Frame(feed_frame, bg="#fff", relief=tk.RAISED, borderwidth=2)
            post_frame.pack(pady=10, padx=20, fill=tk.X)

            post_label = tk.Label(post_frame, text=f"Post {i + 1}", bg="#fff", font=custom_font)
            post_label.pack(pady=10)

            if post.get("image"):
                img = tk.PhotoImage(file=post["image"])
                image_label = tk.Label(post_frame, image=img, bg="#fff")
                image_label.image = img
                image_label.pack(pady=5)

            post_content = tk.Label(post_frame, text=post["content"], bg="#fff", font=custom_font)
            post_content.pack(pady=5)

            like_button = tk.Button(post_frame, text=f"Like ({post['likes']})", bg="#0095f6", fg="white", font=custom_font, command=lambda i=i: like_post(i))
            like_button.pack(side=tk.LEFT, padx=10, pady=5)

            comment_button = tk.Button(post_frame, text="Comment", bg="#0095f6", fg="white", font=custom_font, command=lambda i=i: add_comment(i))
            comment_button.pack(side=tk.LEFT, padx=10, pady=5)

            delete_button = tk.Button(post_frame, text="Delete Post", bg="#ff4d4d", fg="white", font=custom_font, command=lambda i=i: delete_post(i))
            delete_button.pack(side=tk.LEFT, padx=10, pady=5)

            comments_frame = tk.Frame(post_frame, bg="#fff")
            comments_frame.pack(pady=10, fill=tk.X)
            
            for comment in post.get("comments", []):
                comment_label = tk.Label(comments_frame, text=f"• {comment}", bg="#fff", font=custom_font)
                comment_label.pack(anchor=tk.W)

    def view_profile():
        profile_window = tk.Toplevel()
        profile_window.title("Profile")
        profile_window.geometry("500x500")
        profile_window.configure(bg="#f7f7f7")

        custom_font = font.Font(family="Arial", size=12)

        def save_profile():
            email = email_entry.get()
            bio = bio_entry.get("1.0", "end-1c")
            profile_picture = file_path_entry.get()

            current_user["email"] = email
            current_user["bio"] = bio
            current_user["profile_picture"] = profile_picture

            save_data()
            messagebox.showinfo("Profile Updated", "Profile updated successfully!")
            profile_window.withdraw()
            main_window.deiconify()

        header_label = tk.Label(profile_window, text="Edit Profile", font=("Arial", 24, "bold"), bg="#f7f7f7")
        header_label.pack(pady=20)

        email_label = tk.Label(profile_window, text="Email", font=custom_font, bg="#f7f7f7")
        email_label.pack(pady=5)
        email_entry = tk.Entry(profile_window, width=50, font=custom_font)
        email_entry.insert(0, current_user.get("email", ""))
        email_entry.pack(pady=5)

        bio_label = tk.Label(profile_window, text="Bio", font=custom_font, bg="#f7f7f7")
        bio_label.pack(pady=5)
        bio_entry = tk.Text(profile_window, height=4, width=50, font=custom_font)
        bio_entry.insert("1.0", current_user.get("bio", ""))
        bio_entry.pack(pady=5)

        file_path_label = tk.Label(profile_window, text="Profile Picture (path)", font=custom_font, bg="#f7f7f7")
        file_path_label.pack(pady=5)
        file_path_entry = tk.Entry(profile_window, width=50, font=custom_font)
        file_path_entry.insert(0, current_user.get("profile_picture", ""))
        file_path_entry.pack(pady=5)

        save_button = tk.Button(profile_window, text="Save Changes", bg="#0095f6", fg="white", font=custom_font, width=50, command=save_profile)
        save_button.pack(pady=20)

        back_button = tk.Button(profile_window, text="Back to Feed", bg="#0095f6", fg="white", font=custom_font, width=50, command=lambda: [profile_window.withdraw(), main_window.deiconify()])
        back_button.pack(pady=10)

    header_label = tk.Label(main_window, text="Betelgeuse Feed", font=("Arial", 24, "bold"), bg="#f7f7f7")
    header_label.pack(pady=20)

    profile_button = tk.Button(main_window, text="View Profile", bg="#0095f6", fg="white", font=custom_font, command=view_profile)
    profile_button.pack(pady=10)

    create_post_button = tk.Button(main_window, text="Create New Post", bg="#0095f6", fg="white", font=custom_font, command=add_post)
    create_post_button.pack(pady=20)

    feed_frame = tk.Frame(main_window, bg="#f7f7f7")
    feed_frame.pack(pady=20, fill=tk.BOTH, expand=True)

    update_feed()

    footer_frame = tk.Frame(main_window, bg="#f7f7f7")
    footer_frame.pack(side=tk.BOTTOM, pady=10)

    footer_label = tk.Label(footer_frame, text="© 2009 Betelgeuse", bg="#f7f7f7", font=("Arial", 10))
    footer_label.pack()

    main_window.mainloop()

# Start with the login window
create_login_window()
