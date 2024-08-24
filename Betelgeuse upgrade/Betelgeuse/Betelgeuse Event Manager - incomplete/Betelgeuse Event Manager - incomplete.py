import tkinter
import random

def Carnival():
    global points, wins, losses  # Declare these variables as global
    
    points = 0
    wins = 0
    losses = 0

    def update_stats():
        stats_label.config(text=f"Points: {points} | Wins: {wins} | Losses: {losses}")

    def show_menu():
        clear_window()
        button_roll_dice.pack(pady=10)
        button_slot_machine.pack(pady=10)
        button_guessing_game.pack(pady=10)
        update_stats()
        stats_label.pack(pady=20)

    def roll_dice():
        global points, wins, losses
        points = 0
        clear_window()
        result = random.randint(1, 6)
        if result == 6:
            result_label.config(text=f"You rolled a {result}! You win!")
            points += 10
            wins += 1
        else:
            result_label.config(text=f"You rolled a {result}. Try again!")
            points -= 5
            losses += 1
        result_label.pack(pady=20)
        back_button.pack(pady=10)
        update_stats()

    def slot_machine():
        global points, wins, losses
        clear_window()
        symbols = ['🍒', '🍋', '🍊', '🍉', '🍇']
        result = [random.choice(symbols) for _ in range(3)]
        if len(set(result)) == 1:
            result_label.config(text=' | '.join(result) + " - Jackpot! You win!")
            points += 50
            wins += 1
        else:
            result_label.config(text=' | '.join(result) + " - Better luck next time!")
            points -= 10
            losses += 1
        result_label.pack(pady=20)
        back_button.pack(pady=10)
        update_stats()

    def guessing_game():
        global points, wins, losses

        def check_guess():
            global points, wins, losses
            try:
                guess = int(guess_entry.get())
                number = random.randint(1, 10)
                if guess == number:
                    result_label.config(text=f"Correct! The number was {number}. You win!")
                    points += 20
                    wins += 1
                else:
                    result_label.config(text=f"Wrong! The number was {number}. Try again!")
                    points -= 10
                    losses += 1
                update_stats()
            except ValueError:
                result_label.config(text="Please enter a valid number.")

        clear_window()
        guess_label = tkinter.Label(window, text="Guess a number between 1 and 10:", font=("Comic Sans MS", 14), bg='#f8d7da')
        guess_label.pack(pady=10)
        guess_entry = tkinter.Entry(window, font=("Comic Sans MS", 14))
        guess_entry.pack(pady=10)
        guess_button = tkinter.Button(window, text="Submit Guess", font=("Helvetica", 16, "bold"), bg="#ffcc00", fg="#000", padx=20, pady=10, command=check_guess)
        guess_button.pack(pady=10)
        result_label.pack(pady=20)
        back_button.pack(pady=10)
        update_stats()

    def clear_window():
        for widget in window.winfo_children():
            widget.pack_forget()

    window = tkinter.Tk()
    window.title("Betelgeuse Carnival")
    window.geometry("600x500")
    window.configure(bg='#f8d7da')

    button_roll_dice = tkinter.Button(window, text="🎲 Play Dice Roll 🎲", font=("Helvetica", 16, "bold"), bg="#ffcc00", fg="#000", padx=20, pady=10, command=roll_dice)
    button_slot_machine = tkinter.Button(window, text="🎰 Play Slot Machine 🎰", font=("Helvetica", 16, "bold"), bg="#ffcc00", fg="#000", padx=20, pady=10, command=slot_machine)
    button_guessing_game = tkinter.Button(window, text="🎯 Play Guessing Game 🎯", font=("Helvetica", 16, "bold"), bg="#ffcc00", fg="#000", padx=20, pady=10, command=guessing_game)
    back_button = tkinter.Button(window, text="Back to Menu", font=("Helvetica", 14, "bold"), bg="#ffcc00", fg="#000", padx=20, pady=10, command=show_menu)

    result_label = tkinter.Label(window, text="", font=("Comic Sans MS", 18, "italic"), bg='#f8d7da', fg='#d9534f')
    stats_label = tkinter.Label(window, text="", font=("Comic Sans MS", 14, "bold"), bg='#f8d7da', fg='#d9534f')

    show_menu()

    text_label = tkinter.Label(window, text="Welcome to the Carnival App!", font=("Comic Sans MS", 18, "italic"), bg='#f8d7da', fg='#d9534f')
    text_label.pack()

    window.mainloop()

# Main window setup
m = tkinter.Tk()
m.geometry("378x600")
m.title("Betelgeuse Events")
b1 = tkinter.Button(m, text="Carnival", command=Carnival)
b1.pack()
ba = tkinter.Button(m, text="↓")
ba.pack()
bb = tkinter.Button(m, text="Events")
bb.pack()
bc = tkinter.Button(m, text="↓")
bc.pack()
b3 = tkinter.Button(m, text="Facilities")
b3.pack()
bd = tkinter.Button(m, text="↓")
bd.pack()
b4 = tkinter.Button(m, text="Help")
b4.pack()

# Use a proper image path and file format
image_path = 'C:/Users/Vivek bhimrao shinde/Downloads/bgs.png'
photo = tkinter.PhotoImage(file=image_path)
label = tkinter.Label(m, image=photo)
label.pack()

m.mainloop()
