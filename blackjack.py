import random
import time
import os

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"
    
    def get_numeric_value(self):
        if self.value in ["Jack", "Queen", "King"]:
            return 10
        elif self.value == "Ace":
            return 11  # Default value, will be adjusted in Hand class
        else:
            return int(self.value)

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        
        # Update hand value
        self.value += card.get_numeric_value()
        
        # Track aces
        if card.value == "Ace":
            self.aces += 1
        
        # Adjust for aces if needed
        self.adjust_for_ace()
    
    def adjust_for_ace(self):
        # If total value > 21 and we have aces, convert some aces from 11 to 1
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
    
    def get_value(self):
        return self.value
    
    def is_blackjack(self):
        return len(self.cards) == 2 and self.value == 21

    def __str__(self):
        return ", ".join(str(card) for card in self.cards)

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = None
        self.dealer_hand = None
        self.player_chips = 100
        self.current_bet = 0
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def deal_initial_cards(self):
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        
        # Deal 2 cards to player and dealer
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal())
            self.dealer_hand.add_card(self.deck.deal())
    
    def show_some_cards(self):
        print("\nDealer's Hand:")
        print("<card hidden>")
        print(self.dealer_hand.cards[1])
        print("\nPlayer's Hand:", *self.player_hand.cards, sep="\n")
        print(f"Player's Hand Value: {self.player_hand.get_value()}")
    
    def show_all_cards(self):
        print("\nDealer's Hand:", *self.dealer_hand.cards, sep="\n")
        print(f"Dealer's Hand Value: {self.dealer_hand.get_value()}")
        print("\nPlayer's Hand:", *self.player_hand.cards, sep="\n")
        print(f"Player's Hand Value: {self.player_hand.get_value()}")
    
    def place_bet(self):
        while True:
            try:
                print(f"\nYou have {self.player_chips} chips.")
                bet = int(input("How many chips would you like to bet? "))
                
                if bet <= 0:
                    print("Bet must be positive!")
                elif bet > self.player_chips:
                    print("You don't have enough chips!")
                else:
                    self.current_bet = bet
                    self.player_chips -= bet
                    break
            except ValueError:
                print("Please enter a number.")
    
    def player_hit(self):
        self.player_hand.add_card(self.deck.deal())
    
    def dealer_hit(self):
        self.dealer_hand.add_card(self.deck.deal())
    
    def player_wins(self):
        self.player_chips += self.current_bet * 2
        print(f"Player wins! You now have {self.player_chips} chips.")
    
    def dealer_wins(self):
        print(f"Dealer wins. You now have {self.player_chips} chips.")
    
    def push(self):
        self.player_chips += self.current_bet
        print(f"It's a tie! Your bet is returned. You now have {self.player_chips} chips.")
    
    def player_busts(self):
        print(f"Player busts! You now have {self.player_chips} chips.")
    
    def dealer_busts(self):
        self.player_chips += self.current_bet * 2
        print(f"Dealer busts! Player wins! You now have {self.player_chips} chips.")
    
    def player_blackjack(self):
        self.player_chips += int(self.current_bet * 2.5)
        print(f"Blackjack! Player wins 1.5x the bet! You now have {self.player_chips} chips.")
    
    def play_round(self):
        # Check if we need a new deck
        if len(self.deck.cards) < 10:
            print("Reshuffling the deck...")
            self.deck = Deck()
            self.deck.shuffle()
        
        # Place bet
        self.place_bet()
        
        # Deal initial cards
        self.deal_initial_cards()
        
        # Show cards (one dealer card hidden)
        self.show_some_cards()
        
        # Check for player blackjack
        if self.player_hand.is_blackjack():
            if self.dealer_hand.is_blackjack():
                self.show_all_cards()
                self.push()
            else:
                self.show_all_cards()
                self.player_blackjack()
            return
        
        # Player's turn
        while self.player_hand.get_value() < 21:
            choice = input("\nWould you like to (H)it or (S)tand? ").lower()
            
            if choice.startswith('h'):
                self.player_hit()
                self.show_some_cards()
            elif choice.startswith('s'):
                break
            else:
                print("Please enter H or S.")
        
        # Check if player busts
        if self.player_hand.get_value() > 21:
            self.show_all_cards()
            self.player_busts()
            return
        
        # Dealer's turn
        print("\nDealer's turn...")
        self.show_all_cards()
        time.sleep(1)
        
        while self.dealer_hand.get_value() < 17:
            print("Dealer hits...")
            self.dealer_hit()
            self.show_all_cards()
            time.sleep(1)
        
        # Check results
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()
        
        if dealer_value > 21:
            self.dealer_busts()
        elif dealer_value > player_value:
            self.dealer_wins()
        elif player_value > dealer_value:
            self.player_wins()
        else:  # Tie, dealer wins
            self.dealer_wins()
    
    def play_game(self):
        print("Welcome to Blackjack!")
        
        while self.player_chips > 0:
            self.clear_screen()
            print("\n" + "="*50)
            print(f"You have {self.player_chips} chips.")
            
            play = input("Would you like to play a hand? (Y/N): ").lower()
            
            if play.startswith('y'):
                self.play_round()
            else:
                break
            
            input("\nPress Enter to continue...")
        
        if self.player_chips <= 0:
            print("\nYou've run out of chips! Game over.")
        
        print(f"\nThanks for playing! You leave with {self.player_chips} chips.")

if __name__ == "__main__":
    game = Game()
    game.play_game()
