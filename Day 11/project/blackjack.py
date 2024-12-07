# this is my solution

import art
import random

deck_of_card = [
    11, 2, 3, 4,
    5, 6, 7, 8,
    9, 10, 10, 10
]

def draw_card(num_of_card = 2):
    return random.choices(deck_of_card, k=num_of_card)

def sum_card(card):
    return sum(card)

def calculated_score_info(user_card_list, computer_card_list):
    print(f"Your card: {user_card_list}, current score: {sum_card(user_card_list)}")
    print(f"Computer's first card: {computer_card_list[0]}")

def final_score(user_card_list, computer_card_list):
    print(f"Your final hand: {user_card_list}, final score: {sum_card(user_card_list)}")
    print(f"Computer's final hand: {computer_card_list}, final score: {sum_card(computer_card_list)}")

is_game_init = False
is_game_continue = False

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

if start_game == "y":
    is_game_init = True

while is_game_init:
    is_game_continue = True
    print(art.logo)
    user_card=draw_card()
    computer_card=draw_card()
    calculated_score_info(user_card, computer_card)

    while is_game_continue:
        continue_game = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if continue_game == "y":
            user_card.append(draw_card(num_of_card=1)[0])
            calculated_score_info(user_card, computer_card)
            if sum_card(user_card) > 21:
                final_score(user_card, computer_card)
                print(f"You went over. You lose T_T")
                restart_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()

                if restart_game == "y":
                    is_game_init = True
                    is_game_continue = False
                else:
                    is_game_init = False
                    is_game_continue = False
        else:
            is_game_init = False
            is_game_continue = False

    if not is_game_continue and not is_game_init:
        while sum_card(computer_card) < 17:
            computer_card.append(draw_card(num_of_card=1)[0])

        if sum_card(computer_card) > 21:
            final_score(user_card, computer_card)
            print(f"Opponent went over. You win")

        elif sum_card(computer_card) == 21:
            final_score(user_card, computer_card)
            print(f"You lose. Opponent has Blackjack")

        elif sum_card(computer_card) < 21 and sum_card(computer_card) > sum_card(user_card):
            final_score(user_card, computer_card)
            print(f"You lose.")

        elif sum_card(user_card) == 21:
            final_score(user_card, computer_card)
            print(f"You Win. You got Blackjack")

        elif sum_card(user_card) < 21 and sum_card(user_card) > sum_card(computer_card):
            final_score(user_card, computer_card)
            print(f"You Win.")

        elif sum_card(user_card) == sum_card(computer_card):
            final_score(user_card, computer_card)
            print(f"Draw")

        restart_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()

        if restart_game == "y":
            is_game_init = True


# Angela Solution

# import random
# from art import logo
#
#
# def deal_card():
#     """Returns a random card from the deck"""
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     card = random.choice(cards)
#     return card
#
#
# def calculate_score(cards):
#     """Take a list of cards and return the score calculated from the cards"""
#     if sum(cards) == 21 and len(cards) == 2:
#         return 0
#
#     if 11 in cards and sum(cards) > 21:
#         cards.remove(11)
#         cards.append(1)
#
#     return sum(cards)
#
#
# def compare(u_score, c_score):
#     """Compares the user score u_score against the computer score c_score."""
#     if u_score == c_score:
#         return "Draw 🙃"
#     elif c_score == 0:
#         return "Lose, opponent has Blackjack 😱"
#     elif u_score == 0:
#         return "Win with a Blackjack 😎"
#     elif u_score > 21:
#         return "You went over. You lose 😭"
#     elif c_score > 21:
#         return "Opponent went over. You win 😁"
#     elif u_score > c_score:
#         return "You win 😃"
#     else:
#         return "You lose 😤"
#
#
# def play_game():
#     print(logo)
#     user_cards = []
#     computer_cards = []
#     computer_score = -1
#     user_score = -1
#     is_game_over = False
#
#     for _ in range(2):
#         user_cards.append(deal_card())
#         computer_cards.append(deal_card())
#
#     while not is_game_over:
#         user_score = calculate_score(user_cards)
#         computer_score = calculate_score(computer_cards)
#         print(f"Your cards: {user_cards}, current score: {user_score}")
#         print(f"Computer's first card: {computer_cards[0]}")
#
#         if user_score == 0 or computer_score == 0 or user_score > 21:
#             is_game_over = True
#         else:
#             user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#             if user_should_deal == "y":
#                 user_cards.append(deal_card())
#             else:
#                 is_game_over = True
#
#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal_card())
#         computer_score = calculate_score(computer_cards)
#
#     print(f"Your final hand: {user_cards}, final score: {user_score}")
#     print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score, computer_score))
#
#
# while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
#     print("\n" * 20)
#     play_game()
#







