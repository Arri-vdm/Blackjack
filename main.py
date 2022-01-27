############### Blackjack Project #####################

# Imports
from art import logo
import random
from replit import clear


# Make sure all is cleared
clear()

# Start of game
def blackjack():

    # Initially restart is set to False
    restart = False

    # Show logo
    print(logo)

    # Play or not
    print("---------------------------------------------------------------")
    start_game = input(
        "\nWelcome to BLACKJACK a.k.a. 21?\n\nType 'd' + enter to DEAL, or...\nType 'x' + enter to EXIT...\n"
    ).lower()
    print("---------------------------------------------------------------")

    while not restart:
        
        if restart == False:

            # A function to restart or exit after playing has begun
            def restart():
                end_of_blackjack = input(
                    "Type 'r' + enter to RESTART or to choose from more options...\n"
                    ).lower()
                if end_of_blackjack in ("r", "restart"):
                    clear()
                    blackjack()
        
        
            if start_game in ("d", "deal"):

                # Six Deck of 52 cards
                # Modern blackjack, as played in most land-based casinos 
                # from Las Vegas to Macau, uses six to eight decks of the 
                # standard 52 playing cards.
                cards = [
                    11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,11, 11, 11, 11, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 
                ]


                print(cards)

                # Cards: Assign to player
                player_cards = random.sample(cards, 2)
                # Cards: Assign to dealer
                dealer_cards = random.sample(cards, 2)

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
                        "\n---------------------------------------------------------------\n"
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

                # Is it the end of the game
                end_of_game = False
                
                # Inspect to see if there is a winner
                def inspect_winner(dealer_score, player_score, end_of_game):
                    """Inspects the rules to determine
                    if there is a winner...
                    """

                    # While the game coninues
                    if end_of_game == False:

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
                            
                            # If dealer_score = 21 then dealer wins
                            if dealer_score == 21:
                                if 10 and 11 in dealer_cards:
                                    normal_output()
                                    print(f" 😭 BLACKJACK: DEALER WINS!! 😭\n")
                                    print(
                                        "---------------------------------------------------------------\n"
                                    )
                                    # Is it the end of the game
                                    end_of_game = True
                                    restart()
                                else:
                                    normal_output()
                                    print(f" 😭 DEALER WINS!! 😭\n")
                                    print(
                                        "---------------------------------------------------------------\n"
                                    )
                                    # Is it the end of the game
                                    end_of_game = True
                                    restart()
                            
                            # If player_score = 21 then player wins
                            elif player_score == 21:
                                if 10 and 11 in player_cards:
                                    normal_output()
                                    print(f" 😎 BLACKJACK: PLAYER WINS!! 😎\n")
                                    print(
                                        "---------------------------------------------------------------\n"
                                    )
                                    # Is it the end of the game
                                    end_of_game = True
                                    restart()
                                else:
                                    normal_output()
                                    print(f" 😎 PLAYER WINS!! 😎\n")
                                    print(
                                        "---------------------------------------------------------------\n"
                                    )
                                    # Is it the end of the game
                                    end_of_game = True
                                    restart()
                            
                            # If dealer and player have Blackjack, the dealer wins
                            elif dealer_score == 21 and player_score == 21:
                                if 10 and 11 in dealer_cards or 10 and 11 in player_cards:
                                    normal_output()
                                    print(f" 🙄 BLACKJACK: DRAW!! 🙄\n")
                                    print(
                                        "---------------------------------------------------------------\n"
                                    )
                                    # Is it the end of the game
                                    end_of_game = True
                                    restart()

                            # If dealer_score and player_score are the same: Draw
                            elif dealer_score == player_score:
                                normal_output()
                                print(f" 🙄 DRAW!! 🙄\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()

                            # If player score > 21 and dealer score < 21, the dealer wins
                            elif player_score > 21 and dealer_score < 21:
                                normal_output()
                                print(f" 😭 BUST! DEALER WINS!! 😭\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()
                            
                            # If dealer score > 21 and player score < 21, the player wins
                            elif dealer_score > 21 and player_score < 21:
                                normal_output()
                                print(f" 😭 BUST! PLAYER WINS!! 😭\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()

                            # End Game: Both scores > 21
                            elif dealer_score > 21 and player_score > 21:
                                normal_output()
                                print(f" 😎 PLAYER WINS!! 😎\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()
                            
                            # End Game: Player's score = 21 and dealer's score > 21
                            elif player_score == 21 and dealer_score > 21:
                                normal_output()
                                print(f" 😎 PLAYER WINS!! 😎\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()
                            
                            # End Game: Dealer's score = 21 and player's score > 21
                            elif dealer_score == 21 and player_score > 21:
                                normal_output()
                                print(f" 😭 DEALER WINS!! 😭\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()

                            # End Game: Dealer's score > 21
                            elif dealer_score > 21:
                                normal_output()
                                print(f" 😎 BUST! PLAYER WINS!! 😎\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()

                            # End Game: Player's score > 21
                            elif player_score > 21:
                                normal_output()
                                print(f" 😭 BUST! DEALER WINS!! 😭\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()                            # If dealer_score = 21 then dealer wins
                            if dealer_score == 21:
                                if 10 and 11 in dealer_cards:
                                    normal_output()
                                    print(f" 😭 BLACKJACK: DEALER WINS!! 😭\n")
                                    print(
                                        "---------------------------------------------------------------\n"
                                    )
                                    # Is it the end of the game
                                    end_of_game = True
                                    restart()
                                else:
                                    normal_output()
                                    print(f" 😭 DEALER WINS!! 😭\n")
                                    print(
                                        "---------------------------------------------------------------\n"
                                    )
                                    # Is it the end of the game
                                    end_of_game = True
                                    restart()
                            
                            # If player_score = 21 then player wins
                            elif player_score == 21:
                                if 10 and 11 in player_cards:
                                    normal_output()
                                    print(f" 😎 BLACKJACK: PLAYER WINS!! 😎\n")
                                    print(
                                        "---------------------------------------------------------------\n"
                                    )
                                    # Is it the end of the game
                                    end_of_game = True
                                    restart()
                                else:
                                    normal_output()
                                    print(f" 😎 PLAYER WINS!! 😎\n")
                                    print(
                                        "---------------------------------------------------------------\n"
                                    )
                                    # Is it the end of the game
                                    end_of_game = True
                                    restart()
                            
                            # If dealer and player have Blackjack, the dealer wins
                            elif dealer_score == 21 and player_score == 21:
                                if 10 and 11 in dealer_cards or 10 and 11 in player_cards:
                                    normal_output()
                                    print(f" 🙄 BLACKJACK: DRAW!! 🙄\n")
                                    print(
                                        "---------------------------------------------------------------\n"
                                    )
                                    # Is it the end of the game
                                    end_of_game = True
                                    restart()

                            # If dealer_score and player_score are the same: Draw
                            elif dealer_score == player_score:
                                normal_output()
                                print(f" 🙄 DRAW!! 🙄\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()

                            # End Game: Both scores > 21
                            elif dealer_score > 21 and player_score > 21:
                                normal_output()
                                print(f" 😎 PLAYER WINS!! 😎\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()
                            
                            # End Game: Player's score = 21 and dealer's score > 21
                            elif player_score == 21 and dealer_score > 21:
                                normal_output()
                                print(f" 😎 PLAYER WINS!! 😎\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()
                            
                            # End Game: Dealer's score = 21 and player's score > 21
                            elif dealer_score == 21 and player_score > 21:
                                normal_output()
                                print(f" 😭 DEALER WINS!! 😭\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()
                            
                            # If player score > 21 and dealer score < 21, the dealer wins
                            elif player_score > 21 and dealer_score < 21:
                                normal_output()
                                print(f" 😭 BUST! DEALER WINS!! 😭\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()
                            
                            # If dealer score > 21 and player score < 21, the player wins
                            elif dealer_score > 21 and player_score < 21:
                                normal_output()
                                print(f" 😭 BUST! PLAYER WINS!! 😭\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()

                            # End Game: Dealer's score > 21
                            elif dealer_score > 21:
                                normal_output()
                                print(f" 😎 BUST! PLAYER WINS!! 😎\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()

                            # End Game: Player's score > 21
                            elif player_score > 21:
                                normal_output()
                                print(f" 😭 BUST! DEALER WINS!! 😭\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()

                        # If either's is equal to more than two cards, certain rules apply
                        if len(player_cards) >= 3 and len(dealer_cards) >= 1 or len(dealer_cards) >= 2:

                            # If dealer_score = 21 then dealer wins
                            if dealer_score == 21:
                                if 10 and 11 in dealer_cards:
                                    normal_output()
                                    print(f" 😭 BLACKJACK: DEALER WINS!! 😭\n")
                                    print(
                                        "---------------------------------------------------------------\n"
                                    )
                                    # Is it the end of the game
                                    end_of_game = True
                                    restart()
                                else:
                                    normal_output()
                                    print(f" 😭 DEALER WINS!! 😭\n")
                                    print(
                                        "---------------------------------------------------------------\n"
                                    )
                                    # Is it the end of the game
                                    end_of_game = True
                                    restart()
                            
                            # If player_score = 21 then player wins
                            elif player_score == 21:
                                if 10 and 11 in player_cards:
                                    normal_output()
                                    print(f" 😎 BLACKJACK: PLAYER WINS!! 😎\n")
                                    print(
                                        "---------------------------------------------------------------\n"
                                    )
                                    # Is it the end of the game
                                    end_of_game = True
                                    restart()
                                else:
                                    normal_output()
                                    print(f" 😎 PLAYER WINS!! 😎\n")
                                    print(
                                        "---------------------------------------------------------------\n"
                                    )
                                    # Is it the end of the game
                                    end_of_game = True
                                    restart()
                            
                            # If dealer and player have Blackjack, the dealer wins
                            elif dealer_score == 21 and player_score == 21:
                                if 10 and 11 in dealer_cards or 10 and 11 in player_cards:
                                    normal_output()
                                    print(f" 🙄 BLACKJACK: DRAW!! 🙄\n")
                                    print(
                                        "---------------------------------------------------------------\n"
                                    )
                                    # Is it the end of the game
                                    end_of_game = True
                                    restart()

                            # If dealer_score and player_score are the same: Draw
                            elif dealer_score == player_score:
                                normal_output()
                                print(f" 🙄 DRAW!! 🙄\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()

                            # If player score > 21 and dealer score < 21, the dealer wins
                            elif player_score > 21 and dealer_score < 21:
                                normal_output()
                                print(f" 😭 BUST! DEALER WINS!! 😭\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()
                            
                            # If dealer score > 21 and player score < 21, the player wins
                            elif dealer_score > 21 and player_score < 21:
                                normal_output()
                                print(f" 😭 BUST! PLAYER WINS!! 😭\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()

                            # End Game: Both scores > 21
                            elif dealer_score > 21 and player_score > 21:
                                normal_output()
                                print(f" 😎 PLAYER WINS!! 😎\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()
                            
                            # End Game: Player's score = 21 and dealer's score > 21
                            elif player_score == 21 and dealer_score > 21:
                                normal_output()
                                print(f" 😎 PLAYER WINS!! 😎\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()
                            
                            # End Game: Dealer's score = 21 and player's score > 21
                            elif dealer_score == 21 and player_score > 21:
                                normal_output()
                                print(f" 😭 DEALER WINS!! 😭\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()

                            # End Game: Dealer's score > 21
                            elif dealer_score > 21:
                                normal_output()
                                print(f" 😎 BUST! PLAYER WINS!! 😎\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()

                            # End Game: Player's score > 21
                            elif player_score > 21:
                                normal_output()
                                print(f" 😭 BUST! DEALER WINS!! 😭\n")
                                print(
                                    "---------------------------------------------------------------\n"
                                )
                                # Is it the end of the game
                                end_of_game = True
                                restart()
                    
                    # Set end of game back to False
                    else:
                        # Is it the end of the game
                        end_of_game = False


                # Check if there is a winner
                inspect_winner(dealer_score=dealer_score, player_score=player_score, end_of_game=end_of_game)

                # if end_of_game = True RESTART
                # *******************************************************************************


                # Only continue if both player's and dealer's scores are below 21
                while (end_of_game == False) and (player_score < 21 and dealer_score < 21):
                    initial_output()

                    ###########################################################
                    #                      NEXT ROUND
                    ###########################################################
                    hit_or_stand = input(
                        f"Type 'h' + enter to HIT and get another card, or...\nType 's' + enter to STAND and not get another card...\n"
                    ).lower()

                    # Create a list of hits
                    hits = 0

                    # Create a list of stand
                    stand = 0

                    #  'HIT'
                    if hit_or_stand in ("h", "hit"): 

                        # For every "hit", add 1 to the hits list
                        hits += 1
                        
                        # Give the Player another card
                        player_card_1 = random.choice(cards)
                        player_cards.append(player_card_1)

                        # Update player score
                        player_score += player_cards[-1]

                        # If hits list contains more or equal to 1 element 
                        if hits >= 1:
                            # If player has 21, give dealer more cards
                            if player_score == 21:
                                # Keep adding cards to dealer until the 
                                # dealer's score is no longer less than 21
                                while dealer_score < 21 and not dealer_score > 21:
                                    # Give the Dealer another card
                                    dealer_card_1 = random.choice(cards)
                                    dealer_cards.append(dealer_card_1)
                                    # Update dealer score
                                    dealer_score += dealer_cards[-1]

                        # Print output
                        normal_output()

                        # Check if there is a winner
                        inspect_winner(dealer_score=dealer_score, player_score=player_score, end_of_game=end_of_game)
                    
                    #  'STAND'
                    if hit_or_stand in ("s", "stand"): 
                        
                        # For every "stand", add 1 to the stand list
                        stand += 1

                        # Give the Dealer another card
                        dealer_card_1 = random.choice(cards)
                        dealer_cards.append(dealer_card_1)

                        # Update dealer score
                        dealer_score += dealer_cards[-1]

                        # If hits list contains more or equal to 1 element 
                        if stand >= 1:

                            # Keep adding cards to dealer until the 
                            # dealer's score is no longer less than 21
                            while dealer_score < 21 and not dealer_score >= 21:
                                # Give the Dealer another card
                                dealer_card_1 = random.choice(cards)
                                dealer_cards.append(dealer_card_1)
                                # Update dealer score
                                dealer_score += dealer_cards[-1]

                        # Print output
                        normal_output()

                        # Check if there is a winner
                        inspect_winner(dealer_score=dealer_score, player_score=player_score, end_of_game=end_of_game)

            else:
                clear()

                print(logo)
                print(
                    "\n---------------------------------------------------------------\n"
                    )
                print("\nSorry to see you go!\nGoodbye...\n\n")

blackjack()
