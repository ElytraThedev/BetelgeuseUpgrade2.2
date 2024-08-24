import tkinter
import tkinter.ttk

window = tkinter.Tk()

# Variables to store username and password
username_var = tkinter.StringVar()
password_var = tkinter.StringVar()

def Title():
    window.title("Betelgeuse")

def Geometry():
    window.geometry("385x600")

def Icon():
    icon_path = r'C:\Users\Vivek bhimrao shinde\Downloads\mango_icon.ico'
    window.iconbitmap(icon_path)

def Label_Betlegeuse():
    label = tkinter.Label(window, text="Betelgeuse", font=("Brush Script MT", 32, "bold", "italic"))
    label.pack()

def Entry():
    window.configure(bg="#fafafa")
    main_frame = tkinter.Frame(window, bg="#fafafa", padx=50, pady=50)
    main_frame.pack(fill="both", expand=True)
    title_label = tkinter.Label(main_frame, text="Login", font=("Brush Script MT", 30, "bold"), bg="#fafafa")
    title_label.pack(pady=(0, 20))
    
    username_frame = tkinter.Frame(main_frame, bg="#fafafa")
    username_frame.pack(fill="x", pady=(0, 10))
    username_entry = tkinter.Entry(username_frame, bd=1, relief="solid", width=25, bg="#e0e0e0", textvariable=username_var)
    username_entry.insert(0, "Username")
    username_entry.config(fg="gray")
    username_entry.bind("<FocusIn>", lambda e: (
        username_entry.delete(0, tkinter.END) if username_entry.get() == "Username" else None,
        username_entry.config(fg="black")
    ))
    username_entry.bind("<FocusOut>", lambda e: (
        username_entry.insert(0, "Username") if not username_entry.get() else None,
        username_entry.config(fg="gray") if username_entry.get() == "Username" else None
    ))
    username_entry.pack(fill="x")
    
    password_frame = tkinter.Frame(main_frame, bg="#fafafa")
    password_frame.pack(fill="x", pady=(0, 20))
    password_entry = tkinter.Entry(password_frame, bd=1, relief="solid", width=25, bg="#e0e0e0", show="*", textvariable=password_var)
    password_entry.insert(0, "Password")
    password_entry.config(fg="gray")
    password_entry.bind("<FocusIn>", lambda e: (
        password_entry.delete(0, tkinter.END) if password_entry.get() == "Password" else None,
        password_entry.config(fg="black")
    ))
    password_entry.bind("<FocusOut>", lambda e: (
        password_entry.insert(0, "Password") if not password_entry.get() else None,
        password_entry.config(fg="gray") if password_entry.get() == "Password" else None
    ))
    password_entry.pack(fill="x")
    
    login_button = tkinter.Button(main_frame, text="Login", bg="#0095f6", fg="white", font=("Arial", 12, "bold"), relief="flat",command=Login)
    login_button.pack(pady=10)

def Login():
      username = username_var.get()
      password = password_var.get()
      username
      password
      window.destroy()
      ui = tkinter.Tk()
      ui.title("Profile")
      icon_path1 = r'C:\Users\Vivek bhimrao shinde\Downloads\mango_icon.ico'
      ui.iconbitmap(icon_path1)
      ui.geometry("385x600")
      icon_path2 = r'C:\Users\Vivek bhimrao shinde\Downloads\Profile_icon.png'
      photo = tkinter.PhotoImage(file=icon_path2)
      label = tkinter.Label(ui, image=photo, bg="black")
      label.pack()
      label = tkinter.Label(ui, text = username, font=('Arial', 20, "italic", ), background="#dbdbc8")
      label.pack()
      canvas = tkinter.Canvas(ui, width=350, height=1, bg="grey")
      canvas.pack()
      label3 = tkinter.Label(ui, text = "\n", font=('Arial', 11, "italic", ))
      label3.pack()
      entry = tkinter.Entry(ui)
      entry.pack(pady=10)
      def on_submit():
        post = entry.get()
        post
        labelo = tkinter.Label(ui, text= post)
        labelo.pack()
      submit_button = tkinter.Button(ui, text="Submit", command=on_submit)
      submit_button.pack(pady=10)   
      labelo = tkinter.Label(ui, text= entry.get())
      labelo.pack()
      ui.mainloop()

class System:
    def Run():
        Title()
        Geometry()
        Icon()
        Label_Betlegeuse()
        Entry()
        window.mainloop()

System.Run()