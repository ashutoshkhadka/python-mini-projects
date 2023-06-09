import random
from hangman_imgs import logo, word_list, stages

print(logo)
guess_word = random.choice(word_list)
dashboard = []
lives = 6

for i in range(len(guess_word)):
    dashboard.append("_")

while "_" in dashboard and lives > 0:
    user_guess = input("Guess a letter\n").lower()
    present = False
    for i in range(len(guess_word)):
        if user_guess == guess_word[i]:
            dashboard[i] = user_guess
            present = True
    if not present:
        lives = lives - 1;
        print(f"You guessed {user_guess}, that is not in the word. You lose a life.")
        print(f"Remaining lives : {lives}")
        print(stages[lives])
    print(" ".join(dashboard))

if not "_" in dashboard:
    print("Congratulations you win!")

print(guess_word)

