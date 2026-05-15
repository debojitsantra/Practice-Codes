import random
import os
import operator
import time


ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}

def fancy_print(text, delay=0.02):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()


def print_ui_box(r1, op, r2, user_input=None):
    line = "-" * 25
    print(line)
    print(line)

    if op == "/":
        question = f"{r1} {op} {r2} (int only)"
    else:
        question = f"{r1} {op} {r2}"

    centered_q = question.center(21)
    print(f"--{centered_q}--")
    print(line)

    if user_input is not None:
        answer_line = str(user_input).center(21)
        print(f"--{answer_line}--")
        print(line)


def game(l, u, level):
    r1 = random.randint(l, u)
    r2 = random.randint(l, u)
    op = random.choice(list(ops.keys()))

    if op == '/' and r2 == 0:
        r2 = 1

    func = ops[op]
    result = func(r1, r2)

    print_ui_box(r1, op, r2)

    try:
        uinp = int(input("--     "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return False, l, u

    print_ui_box(r1, op, r2, uinp)

    if uinp == result:
        os.system("cls" if os.name == "nt" else "clear")
        fancy_print("\nCorrect Answer!")
        l = u
        u = u + u * level
        return True, l, u
    else:
        fancy_print("\nWrong Answer!", 0.05)
        return False, l, u


def save(level, l, u):
    with open("data.txt", "w") as file:
        file.write(f"{level},{l},{u}")


def access():
    try:
        with open("data.txt", "r") as file:
            data = file.read().strip().split(",")
            level = int(data[0])
            l = int(data[1])
            u = int(data[2])
            return level, l, u
    except (FileNotFoundError, ValueError, IndexError):
        return l, u, level


def run(level, l, u):
    while True:
        correct, l, u = game(l, u, level)
        if correct:
            level += 1
            fancy_print(f"\nLevel {level} \n", 0.03)
        else:
            os.system("cls" if os.name == "nt" else "clear")
            fancy_print(f"\nYou Played Till Level {level}")
            save(level, l, u)
            break


def ui():
    while True:
        print('''----------------------------
-       MathMoy        -
----------------------------''')
        print('''
1. Play from Level 1
2. Load Your Achievement
3. Exit''')

        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Please enter a number.")
            continue

        match choice:
            case 1:
                run(1, 1, 5)
            case 2:
                level, l, u = access()
                os.system("cls" if os.name == "nt" else "clear")
                print(f"\nPlaying from saved Level {level}")
                run(level, l, u)
            case 3:
                fancy_print("\nThanks for playing! Goodbye 😊")
                exit()
            case _:
                print("Invalid choice. Please choose 1, 2, or 3.")


ui()