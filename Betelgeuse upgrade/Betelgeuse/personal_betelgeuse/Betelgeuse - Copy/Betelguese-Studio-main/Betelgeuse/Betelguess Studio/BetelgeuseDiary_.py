import tkinter as tk
from tkinter import filedialog, messagebox

def save_text():
    # Get the content of the text widget
    text_content = text_widget.get("1.0", tk.END)

    # Ask the user to select a directory to save the file
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    
    if file_path:
        # Save the content to the file
        with open(file_path, "w") as file:
            file.write(text_content)
        messagebox.showinfo("Success", f"File saved to {file_path}")

def open_file():
    # Ask the user to select a file to open
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    
    if file_path:
        # Open the selected file and read its content
        with open(file_path, "r") as file:
            text_content = file.read()
        text_widget.delete("1.0", tk.END)  # Clear existing text
        text_widget.insert(tk.END, text_content)  # Insert new content

def undo_action():
    text_widget.edit_undo()  # Undo the last action

def redo_action():
    text_widget.edit_redo()  # Redo the last undone action

# Create the main window
window = tk.Tk()
window.title("Betelgeuse Diary")
window.geometry("550x475")

# Create a frame to hold the menu bar and give it a border-like appearance
menu_frame = tk.Frame(window, bd=2, relief="raised")
menu_frame.pack(fill=tk.X)

# Create a menu bar
menu_bar = tk.Menu(window)  # Attach menu_bar directly to window

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Save", command=save_text)
file_menu.add_command(label="Open", command=open_file)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create an "Edit" menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=undo_action)
edit_menu.add_command(label="Redo", command=redo_action)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Attach the menu bar to the window
window.config(menu=menu_bar)

# Add a Text widget with undo/redo capabilities enabled
text_widget = tk.Text(window, undo=True)
text_widget.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

window.mainloop()

