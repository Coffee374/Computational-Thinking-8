import time

def type_writer(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # To move to the next line after the text is fully printed

# words

type_writer("\n\n\n\n\n---Hey there buddy---\n")
type_writer("Use the command in the terminal ani-cli\n")
type_writer("Search for your anime and pick what you want\n")
type_writer("Then go to ports and use noVNC to watch your anime\n\n")
