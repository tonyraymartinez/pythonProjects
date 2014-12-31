import random

p1Cards = [] #array to hold player 1 cards
p2Cards = [] #array to hold player 2 cards
p1Total = 0  #variable to hold player 1 total
p2Total = 0  #variable to hold player 2 total
global game
game = True #variable for game loop termination
#create deck of cards for point reference
deck = {'2s':2,
       '3s':3,
       '4s':4,
       '5s':5,
       '6s':6,
       '7s':7,
       '8s':8,
       '9s':9,
       '10s':10,
       'Js':10,
       'Qs':10,
       'Ks':10,
       'As':1,
       '2h':2,
       '3h':3,
       '4h':4,
       '5h':5,
       '6h':6,
       '7h':7,
       '8h':8,
       '9h':9,
       '10h':10,
       'Jh':10,
       'Qh':10,
       'Kh':10,
       'Ah':1,
       '2d':2,
       '3d':3,
       '4d':4,
       '5d':5,
       '6d':6,
       '7d':7,
       '8d':8,
       '9d':9,
       '10d':10,
       'Jd':10,
       'Qd':10,
       'Kd':10,
       'Ad':1,
       '2c':2,
       '3c':3,
       '4c':4,
       '5c':5,
       '6c':6,
       '7c':7,
       '8c':8,
       '9c':9,
       '10c':10,
       'Jc':10,
       'Qc':10,
       'Kc':10,
       'Ac':1}

#create a deck of cards that will be used to deal
#create deck of cards
deckShuffled = {'2s':2,
       '3s':3,
       '4s':4,
       '5s':5,
       '6s':6,
       '7s':7,
       '8s':8,
       '9s':9,
       '10s':10,
       'Js':10,
       'Qs':10,
       'Ks':10,
       'As':1,
       '2h':2,
       '3h':3,
       '4h':4,
       '5h':5,
       '6h':6,
       '7h':7,
       '8h':8,
       '9h':9,
       '10h':10,
       'Jh':10,
       'Qh':10,
       'Kh':10,
       'Ah':1,
       '2d':2,
       '3d':3,
       '4d':4,
       '5d':5,
       '6d':6,
       '7d':7,
       '8d':8,
       '9d':9,
       '10d':10,
       'Jd':10,
       'Qd':10,
       'Kd':10,
       'Ad':1,
       '2c':2,
       '3c':3,
       '4c':4,
       '5c':5,
       '6c':6,
       '7c':7,
       '8c':8,
       '9c':9,
       '10c':10,
       'Jc':10,
       'Qc':10,
       'Kc':10,
       'Ac':1}

# function to generate random suit value
def suitRand():
  num = random.randint(1,4)
  if num == 1:
    return 's'
  elif num == 2:
    return 'h'
  elif num == 3:
    return 'd'
  else:
    return 'c'

#function to generate random card value
def cardRand():
  num = random.randint(2,14)
  if num <= 10:
    return str(num)
  elif num == 11:
    return 'J'
  elif num == 12:
    return 'Q'
  elif num == 13:
    return 'K'
  else:
    return 'A'

#function to deal random card to player
def deal():
  value = cardRand()
  suit = suitRand()
  return str(value+suit)

#function to give player another card
#pass function player's card array as argument
def hit(x):
  x.append(deal())

#function to total up player cards
def total(x):
  y = 0 #set total points to zero
  for i in x:
    y += deck[i] #add value of each card to total
  return y

#function to check for player bust
#pass players cards into function to find out if player busted
def checkBust(x):
  if total(x) > 21:
    print "You busted and the game is over. Your hand was " + ', '.join(p1Cards) + " and your total was " +   str(total(p1Total))
    game = False
  else:
    game = True

#functin for initial deal
def initDeal():
  hit(p1Cards)
  hit(p1Cards)
  hit(p2Cards)
  hit(p2Cards)

#function that will initialize game
def play():
  while game == True:
    print "Your cards are " + ', '.join(p1Cards) + " and your total is " + str(total(p1Cards)) + "."
    hitme = raw_input("Would you like another card?\nenter y or n\n")
    if total(p1Cards) > 21:
      print "Your have" + str(total(p1Cards)) + ", you busted."
      game = False
    elif hitme == 'y':
      hit(p1Cards)
      play()
    elif hitme == 'n':
      print "Your cards are " + ', '.join(p1Cards) + " and your final total is " + str(total(p1Cards)) + "."
      game = False

#deal each player 2 cards
initDeal()
#start game
play()