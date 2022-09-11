############### Blackjack Project #####################
# There is one rare bug where the player can win with a score of 22 and that is when the first two cards dealt are both Aces. This can be solved by checking for the Ace earlier
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

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run


def deal_card():
  '''Pick one card at random from the list of cards'''
  return cards[random.randint(0,12)]


def hit_me():
  '''Ask the player if they want another card.'''

  hit = input("Type 'y' to get another card, type 'n' to pass: ").lower()
  #if the player enters "n", no card will be added to their hand
  if hit == "n":
    return None
  #if the player enters "y" this function will return the deal_card function which will     return a randomly picked card from the list or deck
  elif hit == 'y':
    return deal_card()


def play_on():
  '''Ask the player if they'd like to play a hand'''

  play = input("Would you like to play a hand? 'y' or 'n': ").lower()
  #if the player enters 'y', this function returns the boolean 'True'
  if play == 'y':
    return True
  #if the player enters 'n', this function returns the boolean 'False'
  else:
    return False

import random #import the random library
#from replit import clear #import the clear function from the replit library
import os
from art import logo #import the variable 'logo' from the 'art' script
clear = os.system('cls') #import the clear output command from os
play_replay = play_on() #create a variable that takes the boolean returned by the play_on function 

while play_replay: #Loop until the value of play_replay is False
  clear #clear the output screen
  print(logo) #print the value of the varialbe 'logo'

  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #Define the deck of cards
  your_cards = [] #define an empty list for the player's cards
  dealer_cards = [] #define an empty list for the dealer's cards
  player_sum = 0 #define a variable that is the sum of the player's cards
  dealer_sum = 0 #define a variable that is the sum of the dealer's cards

  bust = False #create a variable called bust and give it a default value of False

  your_cards.append(deal_card()) #Add one card to the player's hand
  your_cards.append(deal_card()) #Add another card to the player's hand
  player_sum = sum(your_cards) #Sum up the player's hand

  dealer_cards.append(deal_card()) #Add one card to the dealer's hand
  dealer_cards.append(deal_card()) #Add another card to the dealer's hand
  dealer_sum = sum(dealer_cards) #Sum up the dealer's hand

  print(f"Your cards: {your_cards}, Current Score: {player_sum}") #Show the player's hand and score
  print(f"Dealer's first card: {dealer_cards[0]}") #Show the dealer's first card only

  another_card = True #create a boolean variable called 'another_card' and make it True by default
  if player_sum ==21:  #If the player's score is 21 make another_card False
    another_card = False
  while another_card: #While another_card remains True a 'new_player_card' variable is assigned the value returned by the 'hit_me' function.
    new_player_card = hit_me()
    #If the value of the 'new_player_card' is 'None', another_card becomes false
    if new_player_card == None: 
      another_card=False
    elif new_player_card == 11 and player_sum+new_player_card>21:
      new_player_card = 1
      your_cards.append(new_player_card) #Add the new card to the player's hand
      player_sum += new_player_card #Sum up the player's hand
      if player_sum ==21:
        another_card = False
      else:
        print(f"Your cards: {your_cards}, Current Score: {player_sum}") #Display the player's hand and score
        print(f"Dealer's first card: {dealer_cards[0]}") #Display the dealer's first card
    #if the value of 'new_player_card' is not 'None' the new card is added to the player's hand
    else:
      your_cards.append(new_player_card) #Add the new card to the player's hand
      player_sum += new_player_card #Sum up the player's hand
      
      if player_sum ==21: #If player's score is 21 don't prompt for new card
        another_card = False
      elif player_sum>21: #if player's score is over 21 declare the dealer as winner
        print(f"Your final hand:{your_cards}, final score: {player_sum}")
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_sum}")
        print("Bust! The Dealer Takes the Loot!😭")
        another_card = False #Don't prompt for extra card
        bust = True #bust variable set to True
        play_replay = play_on() #Ask player if they want to player another game
      else:
        print(f"Your cards: {your_cards}, Current Score: {player_sum}") #Display the player's hand and score
        print(f"Dealer's first card: {dealer_cards[0]}") #Display the dealer's first card

  #if the bust variable is still false i.e. player score is 21 or less and player doesn't want extra cards, start on this loop.
  if not bust:
    print(f"Dealer's Hand:{dealer_cards}, Dealer Score: {dealer_sum}") #Show the dealer's hand
    #Loop until dealer's score is 17 or higher
    while dealer_sum<17:
      new_dealer_card = deal_card() #Add a new card to dealer's hand
      if new_dealer_card == 11 and dealer_sum+new_dealer_card>21:
        new_dealer_card = 1
      dealer_cards.append(new_dealer_card) #Add the new card to the player's hand
      print(dealer_cards) #show dealer's hand
      dealer_sum=sum(dealer_cards) #sum up dealer's hand and assign to variable dealer_sum
      
      #If dealer's score is over 21, player wins
    if dealer_sum>21:
      print(f"Your final hand:{your_cards}, final score: {player_sum}")
      print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_sum}")
      print("Like a Boss! You win this hand!😎")
      play_replay = play_on()
    #if dealer's score is greater than player's score, dealer wins
    elif dealer_sum > player_sum:
      print(f"Your final hand:{your_cards}, final score: {player_sum}")
      print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_sum}")
      print("Bust! The Dealer Takes the Loot! 😭")
      play_replay = play_on()
    #if dealer's score is equal to player's score, it's a draw
    elif dealer_sum == player_sum:
      print(f"Your final hand:{your_cards}, final score: {player_sum}")
      print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_sum}")
      print("It's a Draw!🤯")
      play_replay = play_on()
    #Anything else is a victory for the player
    else:
      print(f"Your final hand:{your_cards}, final score: {player_sum}")
      print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_sum}")
      print("Like a Boss! You win this hand!😎")
      play_replay = play_on()

     
  

 
      
  

    
        
  
    

  



