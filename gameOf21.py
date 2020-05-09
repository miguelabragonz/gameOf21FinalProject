'''
Created on May 8, 2020

@author: ITAUser
'''
#import random functiom
import random
#set variable keepPlaying to true
#While keepPlaying is true:
keepPlaying = True   
while(keepPlaying):
    #print statement welcoming players to the game
    print("Welcome to 21 or Black Jack")
    #print statement stating the rules ( Press 'q' to quit)
    print("Rules:Get as close to 21 as possible without going over it. To win, you need to get closer to 21 than the dealer. Press d to draw another card or press s to stay where you are at. Press Space to quit")
    #def deck(2,3,4,5,6,7,8,9,10,11,12,13,14)*4 to account for 52 cards
    deck=[2,3,4,5,6,7,8,9,10,11,12,13,14]*4
    #J=11, Q=12, K=13, A=1
    #set player hand and computer hand to 0
    card=[]
    hand=[]
    def deal(deck):
            random.shuffle(deck)
            if card==11:card="J"
            if card==12:card="Q"
            if card==13:card="K"
            if card==14:card="A"
    dealer_hand=[]
    player_hand=[]
    def total(hand):
        total=0
        for card in hand:
            if card=="J" or card="Q" or card="K":
                total+=10
        elif card=="A"
            if total >= 11: total+= 1
            else: total+= 11
    return total
    #shuffle deck 
    
    #Add card to hand
    
    #Print statement saying if they want to draw another card or stay. d=draw s=stay
    
    #if player draws then add another random card to hand
    #check if player's hand is above 21 if so, print out you lose
    #else compare computer and player's hand. If player hand is larger than computer hand, player wins
    #print out you win
    #elif player hand is smaller than computer hand
    #print out you lose! try again.
    choice = 0
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    while choice != "q":
        print ("The dealer has " + str(dealer_hand[0]))
        print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
        blackjack(dealer_hand, player_hand)
        choice = input("Do you want to [D]raw, [S]tay, or [Q]uit: ").lower()
        clear()
        if choice == "d":
            card = deck.pop()
            if card == 11:card = "J"
            if card == 12:card = "Q"
            if card == 13:card = "K"
            if card == 14:card = "A"
            hand.append(player_hand)
            return hand
            while total(dealer_hand) < 17:
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "s":
            while total(dealer_hand) < 17:
            card = deck.pop()
            if card == 11:card = "J"
            if card == 12:card = "Q"
            if card == 13:card = "K"
            if card == 14:card = "A"
            hand.append(dealer_hand)
            score(dealer_hand, player_hand)
            play_again()
        elif choice == "q":
            print ("Bye!")
            exit()