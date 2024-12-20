import random
#introduce to player
print("\n\n\nHi this is wordle. you guess a 5 letter word.\n")
print("🍚 = correct. 🦶 = correct letter wrong place. 💀 = wrong.\n")
print("have fun!\n")

# pick a word at random
word_list = ["soren","penis","sigma","alpha","bheem","skull","licks","willy","poops","shits"]
hidden_word = random.choice(word_list)

#Repeat for 6 guesses
for i in range(6):
    #guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "\n🍚"
    elif guess_word[0] in hidden_word:
        output += "\n🦶"
    else:
        output += "\n💀"

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[1] == hidden_word[1]:
        output += "🍚"
    elif guess_word[1] in hidden_word:
        output += "🦶"
    else:
        output += "💀"

# First letter (in python, counting starts at 0 not 1)
    if guess_word[2] == hidden_word[2]:
        output += "🍚"
    elif guess_word[2] in hidden_word:
        output += "🦶"
    else:
        output += "💀"

# First letter (in python, counting starts at 0 not 1)
    if guess_word[3] == hidden_word[3]:
        output += "🍚"
    elif guess_word[3] in hidden_word:
        output += "🦶"
    else:
        output += "💀"

# First letter (in python, counting starts at 0 not 1)
    if guess_word[4] == hidden_word[4]:
        output += "🍚\n\n"
    elif guess_word[4] in hidden_word:
        output += "🦶\n\n"
    else:
        output += "💀\n\n"

    #result
    print(output)
    if output == "\n🍚🍚🍚🍚🍚\n\n":
        print("\n\nʎOn MᴉN\n\n")
        break

print(f"You used {i+1} guesses")