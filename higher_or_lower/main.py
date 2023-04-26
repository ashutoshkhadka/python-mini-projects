import random
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


print(logo)
used_data = []

choice1 = retrieve_unique_data()
choice2 = retrieve_unique_data()

print_elem("A", choice1)
print("vs")
print_elem("B", choice2)

if input("Who's got more followers? A or B??\n").lower() == "a":
    if has_more_followers(choice1, choice2):
        print("Correct")
    else:
        print("Sorry, you lose")
else:
    if has_more_followers(choice2, choice1):
        print("Correct")
    else:
        print("Sorry, you lose")

print(f"{choice1['name']}: {choice1['follower_count']}")
print(f"{choice2['name']}: {choice2['follower_count']}")
