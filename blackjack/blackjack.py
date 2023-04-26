import random

from art import logo
import os

############### Our Blackjack House Rules #####################
## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():
    return random.choice(cards)


def calc_score(list):
    if 11 in list:
        if sum(list) == 21:
            return 0
        elif sum(list) > 21:
            list.remove(11)
            list.append(1)
            return sum(list)
    return sum(list)


def draw_n_cards(list, num):
    for i in range(num):
        list.append(draw_card())


def compareScores(user_score, pc_score):
    if user_score > 21 and pc_score > 21:
        return "You went over. You lose 😤"

    if user_score == pc_score:
        return "It's a draw 🙃"
    elif pc_score == 0:
        return "Sorry, you lose. The opponent has a Blackjack 😱"
    elif user_score == 0:
        return "Wohooo...Win with a Blackjack 😎"
    elif user_score > 21:
        return "Oops, you went over. You lose 😭"
    elif pc_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > pc_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    ## Print Logo
    print(logo)

    ## Setup game
    user_cards = []
    pc_cards = []

    ##Draw Cards for 1st round
    draw_n_cards(pc_cards, 2)
    draw_n_cards(user_cards, 2)

    game_over = False
    while not game_over:
        ## Calculate Scores
        user_score = calc_score(user_cards)
        pc_score = calc_score(pc_cards)
        print(f"Your cards: {user_cards}, current score: {calc_score(user_cards)}")
        print(f"Computer's first card: {pc_cards[0]}")

        if user_score == 0 or pc_score == 0 or user_score > 21:
            game_over = True

        playNext = input("Type 'y' to get another card, type 'n' to pass:").lower()
        if playNext == 'y':  # User wants to play again
            draw_n_cards(user_cards, 1)
        else:
            game_over = True

        while pc_score != 0 and pc_score < 17:
            draw_n_cards(pc_cards, 1)
            pc_score = calc_score(pc_cards)

        print(f"Your final hand: {user_cards}, final score: {calc_score(user_cards)}")
        print(f"Computer's final hand: {pc_cards}, final score: {calc_score(pc_cards)}")
        print(compareScores(user_score, pc_score))



while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    os.system('clear')
    play_game()
