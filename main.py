############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Blackjack Project Start #####################

# Imports
from art import logo
import random
from replit import clear

# Show logo
print(logo)

# Play or not
print("---------------------------------------------------------------")
start_game = input(
    "\nDo you want to PLAY a game of BLACKJACK a.k.a. 21?\n\nType 'd' + enter to DEAL, or...\nType 'e' + enter to EXIT...\n"
).lower()
print("---------------------------------------------------------------")

if start_game in ("d", "deal"):

    # Deck of 52 cards
    cards = [
        11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6,
        6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10,
        10, 10, 10, 10, 10, 10, 10, 10, 10
    ]

    # How many random cards to generate
    num_cards = 2


    # Function to select a certain number of cards
    def random_card_selector(number_of_cards):
        """Assign the number of cards needed to a variable:
           E.g. random_card_selector(number_of_cards=num_cards)
           ----
            OR
           ----
           Assign the number of cards needed to a number:
           E.g. random_card_selector(number_of_cards=3)
        """
        return random.sample(cards, number_of_cards)

    # Cards: Assign to player
    player_cards = random_card_selector(number_of_cards=num_cards)
    # Cards: Assign to dealer
    dealer_cards = random_card_selector(number_of_cards=num_cards)

    # Testing
    print(f"\nplayer_cards: {player_cards}")
    print(f"\ndealer_cards: {dealer_cards}")

    # Score: Assign 0 to player
    player_score = 0
    # Score: Assign 0 to dealer
    dealer_score = 0
    initial_dealer_score = 0
    
    # Slice: Assign a slice
    player_slice = sum(player_cards[:])
    dealer_slice = sum(dealer_cards[:])
    initial_dealer_slice = dealer_cards[0]
    
    # Update scores
    player_score += player_slice
    dealer_score += dealer_slice
    initial_dealer_score += initial_dealer_slice

    # Testing
    print(f"\nplayer_score: {player_score}")
    print(f"\ninitial_dealer_score: {initial_dealer_score}")
    print(f"\ndealer_score: {dealer_score}")

# elif start_game in ("e", "exit"):
#     clear()
#     print("\nSorry to see you go!\nGoodbye...\n\n")
