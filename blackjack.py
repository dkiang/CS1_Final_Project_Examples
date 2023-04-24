import random

# Define a function to draw a card from the deck
def draw_card(deck):
    card = random.choice(deck)
    deck.remove(card)
    return card

# Define a function to calculate the total value of a hand
def calculate_hand(hand):
    total = 0
    num_aces = 0
    for card in hand:
        if card[0] == 'A':
            num_aces += 1
            total += 11
        elif card[0] in ['K', 'Q', 'J']:
            total += 10
        else:
            total += int(card[0])
    while num_aces > 0 and total > 21:
        total -= 10
        num_aces -= 1
    return total

# Define a function to simulate a full game of blackjack
def play_game(num_players):
    # Define the deck of cards
    suits = ['hearts', 'diamonds', 'clubs', 'spades']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = [(rank, suit) for suit in suits for rank in ranks]

    # Shuffle the deck
    random.shuffle(deck)

    # Initialize variables for tracking the players' hands and scores
    player_hands = [[] for _ in range(num_players)]
    player_scores = [0 for _ in range(num_players)]

    # Deal the initial cards
    for i in range(num_players):
        player_hands[i].append(draw_card(deck))
    dealer_hand = [draw_card(deck), draw_card(deck)]

    # Print the initial hands
    print("Dealer's hand:", dealer_hand[0])
    for i in range(num_players):
        print("Player", i+1, "'s hand:", player_hands[i])

    # Players' turns
    for i in range(num_players):
        while True:
            choice = input("Player " + str(i+1) + "'s turn: Hit or stand? ")
            if choice.lower() == 'hit':
                player_hands[i].append(draw_card(deck))
                print("Player", i+1, "'s hand:", player_hands[i])
                if calculate_hand(player_hands[i]) > 21:
                    print("Player", i+1, "busts!")
                    break
            elif choice.lower() == 'stand':
                break
            else:
                print("Invalid choice. Please enter 'hit' or 'stand'.")
        player_scores[i] = calculate_hand(player_hands[i])

    # Dealer's turn
    while calculate_hand(dealer_hand) < 17:
        dealer_hand.append(draw_card(deck))
    print("Dealer's hand:", dealer_hand)

    # Determine the winners
    dealer_total = calculate_hand(dealer_hand)
    for i in range(num_players):
        if player_scores[i] > 21:
            print("Player", i+1, "loses: bust!")
        elif dealer_total > 21:
            print("Player", i+1, "wins: dealer busts!")
        elif player_scores[i] > dealer_total:
            print("Player", i+1, "wins!")
       
play_game(1)
