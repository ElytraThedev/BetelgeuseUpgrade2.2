import tkinter as tk

def run_script1():
    import Betelgeuse_  # Adjust with the actual path or module name

def run_script2():
    import Betelgeuse2_  # Adjust with the actual path or module name

def run_script3():
    import BetelgeuseDiary_  # Adjust with the actual path or module name

def run_script4():
    import BetelgeuseMassenger_  # Adjust with the actual path or module name

# Create the main window
window = tk.Tk()
window.title("Betelgeuse Studio")
window.geometry("400x150")

# Create a frame for the buttons
button_frame = tk.Frame(window)
button_frame.pack(side=tk.TOP, padx=10, pady=10, fill=tk.X)

# Create buttons
button1 = tk.Button(button_frame, text="Run Script 1", command=run_script1)
button1.pack(side=tk.LEFT, padx=5)

button2 = tk.Button(button_frame, text="Run Script 2", command=run_script2)
button2.pack(side=tk.LEFT, padx=5)

button3 = tk.Button(button_frame, text="Run Script 3", command=run_script3)
button3.pack(side=tk.LEFT, padx=5)

button4 = tk.Button(button_frame, text="Run Script 4", command=run_script4)
button4.pack(side=tk.LEFT, padx=5)


window.mainloop()
