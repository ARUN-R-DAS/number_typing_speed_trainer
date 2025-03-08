import tkinter as tk
import random
import time


def generate_number():
    global current_number
    current_number = random.randint(0, 9)
    number_label.config(text=str(current_number))


def clear_info_label():
    info_label.config(text="")


def check_input(event):
    global points, clear_label_after,correct_count,wrong_count
    user_input = event.char

    if user_input == "q":
        exit_game()
    elif user_input.isdigit() and int(user_input) == current_number:
        points += 1
        correct_count += 1
        score_label.config(text=f"Score: {points}")
        info_label.config(text="CORRECT +1 point", fg='#00f')
    else:
        points -= 1
        wrong_count += 1
        score_label.config(text=f"Score: {points}")
        info_label.config(text=f"WRONG you entered {user_input} \n-1 point", fg='#f00')

    # Cancel any previous scheduled clear event
    root.after_cancel(clear_label_after)
    clear_label_after = root.after(1000, clear_info_label)  # Clear after 1 second

    generate_number()


def exit_game():
    end_time = time.time()
    time_program_ran = round(end_time - start_time)
    result_text = f"You scored {points} points in {time_program_ran} seconds.\n Correct : {correct_count} \n Wrong : {wrong_count}"
    number_label.config(fg="#f0f",text = "made by Arun",font = 10)

    label.config(text="Game Over!")

    score_label.config(text=result_text)
    root.unbind("<Key>")
    exit_button.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Number speed type")
root.geometry("400x300")

points = correct_count = wrong_count =0
start_time = time.time()
clear_label_after = root.after(0, lambda: None)  # Initialize with a dummy event

label = tk.Label(root, text="Press the number shown below", font=("Arial", 14))
label.pack(pady=10)

number_label = tk.Label(root, text="", font=("Arial", 24, "bold"))
number_label.pack(pady=10)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
score_label.pack(pady=10)

info_label = tk.Label(root, text="", font=("Arial", 14), fg='#f0f')
info_label.pack(pady=10)

exit_button = tk.Button(root, text="Exit (Q)", command=exit_game, font=("Arial", 12))
exit_button.pack(pady=10)

root.bind("<Key>", check_input)

generate_number()
root.mainloop()
