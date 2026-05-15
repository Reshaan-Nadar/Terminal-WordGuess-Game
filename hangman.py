import random

words = [
    "python", "computer", "keyboard", "monitor", "internet", "science",
    "artificial", "intelligence", "machine", "learning", "algorithm",
    "database", "network", "software", "hardware", "programming",
    "developer", "function", "variable", "compiler", "terminal",
    "operator", "condition", "iteration", "exception", "package",
    "library", "framework", "application", "security", "analytics",
    "visualization", "dashboard", "engineering", "mathematics",
    "physics", "chemistry", "biology", "astronomy", "university",
    "education", "project", "portfolio", "website", "javascript",
    "pythonista", "hangman", "challenge", "adventure", "processor",
    "graphics", "storage", "wireless", "bluetooth", "encryption",
    "firewall", "protocol", "debugging", "automation"
]

word = random.choice(words)
guessed = []
wrong = []
lives = 6

display = ["_"] * len(word)

print("=== HANGMAN GAME ===")

while lives > 0 and "_" in display:
    print("\nWord:", " ".join(display))
    print("Wrong guesses:", " ".join(wrong))
    print("Lives left:", lives)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one letter.")
        continue

    if guess in guessed or guess in wrong:
        print("Already guessed.")
        continue

    if guess in word:
        guessed.append(guess)

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess

        print("Correct!")

    else:
        wrong.append(guess)
        lives -= 1
        print("Wrong!")

if "_" not in display:
    print("\nYou won! The word was:", word)

else:
    print("\nYou lost! The word was:", word)