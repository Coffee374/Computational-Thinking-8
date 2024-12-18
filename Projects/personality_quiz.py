#Super cool video game quiz


#sets variables to 0
#varibles to determine if you got enough right or wrong

wrong_answers = 0
correct_answers = 0

#questions and stuff
#asks and gives you points based on that

answer = input("\n\n\nWhat year was the Wii made A) 2012, or B) 2006?\n")
if answer == "A":
    wrong_answers += 1
elif answer == "B":
    correct_answers += 1

answer = input("\nWhat was Sega's last console A) Sega Dreamcast, or B) Sega Saturn?\n")
if answer == "A":
    correct_answers += 1
elif answer == "B":
    wrong_answers += 1

answer = input("\nWhat Super Smash Bros was on Gamecube A) Super Smash Bros. Brawl, or B) Super Smash Bros. Melee?\n")
if answer == "A":
    wrong_answers += 1
elif answer == "B":
    correct_answers += 1

answer = input("\nWhat kind of console is the Playstation A) 64 bit console, or B) 32 bit console?\n")
if answer == "A":
    wrong_answers += 1
elif answer == "B":
    correct_answers += 1

answer = input("\nWhat year did Luigi make his first appearance A) 1983, or B) 1994?\n")
if answer == "A":
    correct_answers += 1
elif answer == "B":
    wrong_answers += 1

answer = input("\nWhat did Nintendo make before video games? A) instant rice and love hotels, or B) computers and fireworks\n")
if answer == "A":
    correct_answers += 1
elif answer == "B":
    wrong_answers += 1

answer = input("\nWhat is Nintendo's worst selling console? A) the Virtual Boy, or B) the Wii U\n")
if answer == "A":
    correct_answers += 1
elif answer == "B":
    wrong_answers += 1

answer = input("\nWhat console did the Nintendo Power glove work on? A) the Nintendo 64, or B) the Nintendo Entertainment System\n")
if answer == "A":
    wrong_answers += 1
elif answer == "B":
    correct_answers += 1

answer = input("\nWhat year did Mario make his first appearance A) 1981, or B) 1983?\n")
if answer == "A":
    correct_answers += 1
elif answer == "B":
    wrong_answers += 1

#adds up all variables and sees if you passed or not

if wrong_answers > correct_answers:
    print("\n\nYou failed!!! Stop touching grass and play some video games!\n\n")
elif correct_answers > wrong_answers:
    print("\n\nYou passed. You did great and im sure you will acomplish many great things in life.\n\n")
elif wrong_answers == correct_answers:
    print("\n\nYou did okay\n\n")