############### Blackjack Project #####################

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
    # print(f"\nplayer_cards: {player_cards}")
    # print(f"\ndealer_cards: {dealer_cards}\n")
    # print("---------------------------------------------------------------")

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
    # print(f"\nplayer_score: {player_score}")
    # print(f"\ninitial_dealer_score: {initial_dealer_score}")
    # print(f"\ndealer_score: {dealer_score}\n")
    # print("---------------------------------------------------------------")

    ###############################################################
    #                          INITIALLY:
    ###############################################################
    
    # Prints initial output
    def initial_output():
        """Prints all the initial outputs and more"""
        clear()
        print(logo)
        print(
            "\n---------------------------------------------------------------\n"
        )
        print(f"Player's Cards:     {player_cards}")
        print(f"Player's Score:     {player_score}")
        print(f"\n")
        print(f"Dealer's Card(s):   {initial_dealer_slice}")
        print(f"Dealer's Score:     {initial_dealer_score}")
        print(
            "\n---------------------------------------------------------------\n\n"
        )

    # Prints ouputs
    def normal_output():
        """Prints all the outputs and more"""
        clear()
        print(logo)
        print(
            "\n---------------------------------------------------------------\n"
        )
        print(f"Player's Cards:     {player_cards}")
        print(f"Player's Score:     {player_score}")
        print(f"\n")
        print(f"Dealer's Card(s):   {dealer_cards}")
        print(f"Dealer's Score:     {dealer_score}")
        print(
            "\n---------------------------------------------------------------\n"
            )

    def inspect_winner(dealer_score, player_score):
        """Inspects the rules to determine
           if there is a winner...
        """

        # DEALER: Keep checking if value over 21, replace all 11's
        # with 1, until not the case
        if dealer_score > 21:
            for position in range(len(dealer_cards)):
                if dealer_cards[position] == 11 and dealer_score > 21:
                    dealer_cards[position] = 1
                    dealer_score = sum(dealer_cards)

        # PLAYER: Keep checking if value over 21, replace all 11's
        # with 1, until not the case
        if player_score > 21:
            for position in range(len(player_cards)):
                if player_cards[position] == 11 and player_score > 21:
                    player_cards[position] = 1
                    player_score = sum(player_cards)

        # If player cards is equal to two cards, certain rules apply
        if len(player_cards) <= 2:

            # If dealer and player have Blackjack, the dealer wins
            if dealer_score == 21 and player_score == 21:
                if 10 and 11 in dealer_cards or 10 and 11 in player_cards:
                    normal_output()
                    print(f" 😭 BLACKJACK: DEALER WINS! 😭\n")
                    print(
                        "---------------------------------------------------------------\n\n"
                    )
                else:
                    normal_output()
                    print(f" 🙄 DRAW 🙄\n")
                    print(
                        "---------------------------------------------------------------\n\n"
                    ) 

            # If dealer_score = 21 then dealer wins
            if dealer_score == 21:
                if 10 and 11 in dealer_cards:
                    normal_output()
                    print(f" 😭 BLACKJACK: DEALER WINS! 😭\n")
                    print(
                        "---------------------------------------------------------------\n\n"
                    )
                else:
                    normal_output()
                    print(f" 😭 DEALER WINS!! 😭\n")
                    print(
                        "---------------------------------------------------------------\n\n"
                    )

            # If player_score = 21 then player wins
            if player_score == 21:
                if 10 and 11 in player_cards:
                    normal_output()
                    print(f" 😎 BLACKJACK: PLAYER WINS!! 😎\n")
                    print(
                        "---------------------------------------------------------------\n\n"
                    )
                else:
                    normal_output()
                    print(f" 😎 PLAYER WINS!! 😎\n")
                    print(
                        "---------------------------------------------------------------\n\n"
                    )

        # If either's is equal to more than two cards, certain rules apply
        elif len(player_cards) > 2 or len(dealer_cards) > 2:

            # End Game: Both scores > 21
            if dealer_score > 21 and player_score > 21:
                normal_output()
                print(f" 😭 BUST! DEALER WINS! 😭\n")
                print(
                    "---------------------------------------------------------------\n\n"
                )

            # End Game: Dealer's score > 21
            if dealer_score > 21:
                normal_output()
                print(f" 😎 BUST! PLAYER WINS! 😎\n")
                print(
                    "---------------------------------------------------------------\n\n"
                )

            # End Game: Player's score > 21
            if player_score > 21:
                normal_output()
                print(f" 😭 BUST! DEALER WINS! 😭\n")
                print(
                    "---------------------------------------------------------------\n\n"
                )

            # If dealer and player have Blackjack, the dealer wins
            if dealer_score == 21 and player_score == 21:
                if 10 and 11 in dealer_cards or 10 and 11 in player_cards:
                    normal_output()
                    print(f" 🙄 BLACKJACK: DRAW! 🙄\n")
                    print(
                        "---------------------------------------------------------------\n\n"
                    )
                else:
                    normal_output()
                    print(f" 🙄 DRAW 🙄\n")
                    print(
                        "---------------------------------------------------------------\n\n"
                    ) 

            # If dealer_score = 21 then dealer wins
            if dealer_score == 21:
                if 10 and 11 in dealer_cards:
                    normal_output()
                    print(f" 😭 BLACKJACK: DEALER WINS! 😭\n")
                    print(
                        "---------------------------------------------------------------\n\n"
                    )
                else:
                    normal_output()
                    print(f" 😭 DEALER WINS!! 😭\n")
                    print(
                        "---------------------------------------------------------------\n\n"
                    )

            # If player_score = 21 then player wins
            if player_score == 21:
                if 10 and 11 in player_cards:
                    normal_output()
                    print(f" 😎 BLACKJACK: PLAYER WINS!! 😎\n")
                    print(
                        "---------------------------------------------------------------\n\n"
                    )
                else:
                    normal_output()
                    print(f" 😎 PLAYER WINS!! 😎\n")
                    print(
                        "---------------------------------------------------------------\n\n"
                    )

            # If dealer_score and player_score are the same: Draw
            if dealer_score == player_score:
                normal_output()
                print(f" 🙄 DRAW 🙄\n")
                print(
                    "---------------------------------------------------------------\n\n"
                )


    # Check if there is a winner
    inspect_winner(dealer_score=dealer_score, player_score=player_score)

    # Only continue if both player's and dealer's scores are below 21
    if player_score < 21 and dealer_score < 21:
        initial_output()

        ###########################################################
        #                      NEXT ROUND
        ###########################################################
        hit_or_stand = input(
            f"Type 'h' + enter to HIT and get another card, or...\nType 's' + enter to STAND and not get another card...\n"
        ).lower()

        # If 'HIT', player gets
        if hit_or_stand in ("h", "hit"):
            # Give the Player another card
            another_card = random.choice(cards)
            player_cards.append(another_card)

            # Update player sscore
            player_score += player_cards[-1]
            
            # Check if there is a winner
            inspect_winner(dealer_score=dealer_score, player_score=player_score)

            # Print output
            # normal_output()

elif start_game in ("e", "exit"):
    clear()
    print("\nSorry to see you go!\nGoodbye...\n\n")
