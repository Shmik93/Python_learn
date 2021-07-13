import random
from art import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

def deal_card(player_cards, cards_list):
    rand_card = random.choice(cards_list)
    player_cards.append(rand_card)

# first deal
for deals in range(2): 
    deal_card(user_cards, cards)
    deal_card(computer_cards, cards)
 
print(f"Computer: {computer_cards} Summary: {sum(computer_cards)} \n Player: {user_cards} Summary: {sum(user_cards)} ")

if sum(user_cards) == 21:
    print("Player: Blackjack \n You win!")
elif sum(computer_cards) == 21:
    print("Computer: Blackjack \n You lose!")     


more_cards = True
answer = input("more?")
if answer == "n":
    more_cards = False


while more_cards:
    deal_card(user_cards, cards)
    deal_card(computer_cards, cards)
    print(f"Computer: {computer_cards} Summary: {sum(computer_cards)} \n Player: {user_cards} Summary: {sum(user_cards)} ")
    answer = input("more?")
    if answer == "n":
        more_cards = False