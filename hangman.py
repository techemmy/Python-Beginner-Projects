import random

words = "hello there yeah dope".upper().split()
word = random.choice(words)
used_letters = []
trials = 0
misses = 0

HANGMAN_PICS = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

def display(word, guessed_letters):
    result = ""
    for i in word:
        if i in guessed_letters:
            result += i + " "
        else:
            result += "_" + " "
    return result

print(HANGMAN_PICS[0])
print(display(word, used_letters))
while True:
    letter = input("Enter a guess: ").upper()

    if letter in used_letters:
        print("You've used the letter")
    else:
        trials += 1
        used_letters.append(letter)

        if letter not in word:
            misses += 1
    
        print(HANGMAN_PICS[misses])
        state = display(word, used_letters)
        print(state)

    if misses == len(HANGMAN_PICS)-1:
        print("The man is hanged...")
        print("The word is", word)
        break
    

    if used_letters:
        print("Used Letters:", ", ".join(used_letters))

    if "_" not in state:
        print("Good job")
        print("You tried", trials, "time(s)")
        break
