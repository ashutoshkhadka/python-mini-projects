import random, os
from art import vs, logo
from data import data


def retrieve_unique_data():
    """
    Gets unique data from the datalist
    :return: unique element from the data
    """
    while True:
        fresh_data = random.choice(data)
        if fresh_data not in used_data:
            break
    used_data.append(fresh_data)
    return fresh_data


def print_elem(option, entry):
    name = entry["name"]
    desc = entry["description"]
    country = entry["country"]
    print(f"Option {option}: {name}, a {desc}, from {country}")


def has_more_followers(choice1, choice2):
    return choice1["follower_count"] > choice2["follower_count"]


def correct_answer(score):
    score += 1
    print("Correct")
    os.system("clear")
    print(logo)
    print(f"You're right 🥳. Current score: {score}")
    return score


def wrong_answer(score):
    os.system("clear")
    print(logo)
    print(f"Sorry, that's wrong 😥. Your Final score is: {score}")


def play_game():
    print(logo)
    score = 0
    choice1 = retrieve_unique_data()
    choice2 = retrieve_unique_data()

    while True:
        print_elem("A", choice1)
        print(vs)
        print_elem("B", choice2)

        if input("Who's got more followers? A or B??\n").lower() == "a":
            if has_more_followers(choice1, choice2):
                score = correct_answer(score)
                choice2 = retrieve_unique_data()
            else:
                wrong_answer(score)
                break
        else:
            if has_more_followers(choice2, choice1):
                score = correct_answer(score)
                choice1 = retrieve_unique_data()
            else:
                wrong_answer(score)
                break

used_data = []
play_game()
