wrong_answers = 0
correct_answers = 0

answer = input("What year was the Wii made A) 2012, or B) 2006?\n")
if answer == "A":
    wrong_answers += 1
elif answer == "B":
    correct_answers += 1

answer = input("What was Sega's last console A) Sega Dreamcast, or B) Sega Saturn?\n")
if answer == "A":
    correct_answers += 1
elif answer == "B":
    wrong_answers += 1

answer = input("What Super Smash Bros was on Gamecube A) Super Smash Bros. Brawl, or B) Super Smash Bros. Melee?\n")
if answer == "A":
    wrong_answers += 1
elif answer == "B":
    correct_answers += 1

answer = input("What kind of console is the Playstation A) 64 bit console, or B) 32 bit console?\n")
if answer == "A":
    wrong_answers += 1
elif answer == "B":
    correct_answers += 1

answer = input("What year did Luigi make his first aperance A) 1983, or B) 1994?\n")
if answer == "A":
    correct_answers += 1
elif answer == "B":
    wrong_answers += 1

if wrong_answers > correct_answers:
    print("You failed!!! Stop touching grass and play some video games!")
elif correct_answers > wrong_answers:
    print("You passed. You did great and im sure you will acomplish many great things in life.")
elif wrong_answers == correct_answers:
    print("You did okay")