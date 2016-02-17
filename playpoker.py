# File: playpoker.py
# Description: Program designed to simulate a game of '5-Card Draw' by recieving user input on the number of hands to be dealt
#              and then assigning ranks to each hand based on the traditional rules of this poker game type. It then prints
#              the hands in order of rank and assigns a winner.
# Student's Name: Connor Kelly
# Student's UT EID: cjk673
# Course Name: CS 313E
# Unique Number: 50597
#
# Date Created: 9/24/15
# Date Last Modified: 9/25/15

import random

# create card objects with suit and rank attributes
class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank, suit):
    self.rank = rank
    self.suit = suit

  # print letters for correspondingly ranked face cards 
  def __str__ (self):
    if self.rank == 14:
      rank = 'A'
    elif self.rank == 13:
      rank = 'K'
    elif self.rank == 12:
      rank = 'Q'
    elif self.rank == 11:
      rank = 'J'
    else:
      rank = self.rank
    return str(rank) + self.suit

  # set methods to compare card ranks

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)

# Create deck class to use when initializing deck in class poker
class Deck (object):

  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    # shuffle deck
    random.shuffle (self.deck)

  def deal (self):
    # Deal cards, fail if deck is empty
    if len(self.deck) == 0:
      return None
    else:
      return self.deck.pop(0)

# Create Poker object      
class Poker (object):
  def __init__ (self, numHands):
    self.deck = Deck()              # create a deck
    self.deck.shuffle()             # shuffle it
    self.hands = []
    numCards_in_Hand = 5

    for i in range (numHands):
      # Deal 5 cards into empty list: hand
      hand = []
      for j in range (numCards_in_Hand):
        hand.append (self.deck.deal())
      self.hands.append (hand)

  # Print hands in order of rank
  def play (self):
    print()
    for i in range (len(self.hands)):
      sortedHand = sorted (self.hands[i], reverse = True)
      hand = ''
      for card in sortedHand:
        hand = hand + str(card) + ' '
      print ('Hand ' + str(i + 1) + ': ' + hand)

    print()

    # Compile point value list for different hands
    handList = []
    for i in range(len(self.hands)):
      sortedHand = sorted(self.hands[i], reverse = True)
      # Calculate the point total for hand and append to list
      rankHand = self.point_calc(sortedHand)
      handList.append(rankHand[0])
      print('Hand' + str(i + 1) + ': ' + rankHand[1])

    # Find ties, put tied hands into list
    highHand = 0
    ties = []
    for i in range(len(self.hands)):
      if handList[highHand] == handList[i]:
        ties.append(i)
      # If hand was larger, reset highHand to i
      elif handList[i] > handList[highHand]:
        highHand = i
        ties = []

    # Print game winner or possible ties
    print()
    if len(ties) > 0:
      print('Hands', highHand + 1, end = '')
      for i in ties:
        print(', ' + str(i + 1), end = '')
      print('tied.')
    else:
      print('Hand', highHand + 1, 'wins.')

  # Returns points and rank per hand
  def point_calc(self, hand):
    value = self.is_royal(hand)
    if value > 0:
      return (value, 'Royal Flush')
    value = self.is_straight_flush(hand)
    if value > 0:
      return (value, 'Straight Flush')
    value = self.is_four(hand)
    if value > 0:
      return (value, 'Four of a Kind')
    value = self.is_full(hand)
    if value > 0:
      return (value, 'Full House')
    value = self.is_flush(hand)
    if value > 0:
      return (value, 'Flush')
    value = self.is_straight(hand)
    if value > 0:
      return (value, 'Straight')
    value = self.is_three(hand)
    if value > 0:      
      return (value, 'Three of a Kind')
    value = self.is_two(hand)
    if value > 0:
      return (value, 'Two Pair')
    value = self.is_one(hand)
    if value > 0:
      return (value, 'One Pair')
    value = self.is_high(hand)
    if value > 0:
      return (value, 'High Card')

  #returns total point value for cards * value of hand
  def point_total(self, h, c1, c2, c3, c4, c5):
    return (h * 13**5) + (c1.rank * 13**4) + (c2.rank * 13**3) + (c3.rank * 13**2) + (c4.rank * 13) + c5.rank  


  # If hand hand satisfies is_straight and is_flush, check if rank is royal
  def is_royal (self, hand):
    if self.is_straight_flush(hand) == True and (hand[0].rank == 14 and hand[1].rank == 13 and hand[2].rank == 12 and hand[3].rank == 11 and hand[4].rank == 10):
      return self.point_total(10, hand[0], hand[1], hand[2], hand[3], hand[4])
    else:
      return 0

  # If hand satisfies is_straight and is_flush
  def is_straight_flush (self, hand):
    if self.is_flush(hand) == True and self.is_straight(hand) == True:
      return self.point_total(9, hand[0], hand[1], hand[2], hand[3])
    else:
      return 0

  # Check indecies 0-3 and 1-4 for match            
  def is_four (self, hand):
    if (hand[0] == hand[1] == hand[2] == hand[3]) or (hand[1] == hand[2] == hand[3] == hand[4]):
      return self.point_total(8, hand[0], hand[1], hand[2], hand[3], hand[4])
    else:
      return 0

  # Possible index combos are: 0-2/3-4 or 0-1/2-4, check both for three of a kind and pair
  def is_full (self, hand):
    if (hand[0] == hand[1] == hand[2] and hand[3] == hand[4]):
      return self.points_total(7, hand[0], hand[1], hand[2], hand[3], hand[4]) 
    elif (hand[0] == hand[1] and hand[2] == hand[3] == hand[4]):
      return self.point_total(7, hand[2], hand[3], hand[4], hand[0], hand[1])
    else:
      return 0

  # Check if rank of cards in hand is same
  def is_flush (self, hand):
    if hand[0].rank == hand[1].rank + 1 == hand[2].rank + 2 == hand[3].rank + 3 == hand[4].rank + 4:
      return self.point_total(6, hand[0], hand[1], hand[2], hand[3], hand[4])
    else:
      return 0

  # Check if cards in hand[1-4] are in single number, descending order to hand[0] via addition
  def is_straight (self, hand):
    if hand[0].rank == hand[1].rank + 1 == hand[2].rank + 2 == hand[3].rank + 3 == hand[4].rank + 4:
      return self.point_total(5, hand[0], hand[1], hand[2], hand[3], hand[4])
    else:
      return 0

  # Possible indecies include: 0-2, 1-3, or 2-4. Check these. Use % 5 t adjust offset if unrelated cards come first 
  def is_three (self, hand):
    for i in range (0, 3):
      if hand[i] == hand[i+1] == hand[i+2]:
         return self.point_total(4, hand[i], hand[i+1], hand[i+2], hand[(i+3)%5], hand[(i+4)%5])
    return 0

  # Possible index combos: 0-1/2-3, 0-1/3-4, or 1-2/3-4. Check these.
  def is_two (self, hand):
    if hand[0] == hand[1] and hand[2] == hand[3]:
      return self.point_total(3, hand[0], hand[1], hand[2], hand[3], hand[4])
    elif hand[0] == hand[1] and hand[3] == hand[4]:
      return self.point_total(3, hand[0], hand[1], hand[3], hand[4], hand[2])
    elif hand[1] == hand[2] and hand[3] == hand[4]:
      return self.point_total(3, hand[1], hand[2], hand[3], hand[4], hand[0])
    else:
      return 0

  # Find index of pair, use % 5 to adjust offset like is_three
  def is_one (self, hand):
    for i in range (0, 4):
      if hand[i] == hand[i + 1]:
        return self.point_total(2, hand[i], hand[i + 1], hand[(i + 2) % 5], hand[(i + 3) % 5], hand[(i + 4) % 5])
    return 0

  # Everything else checked, return point value
  def is_high (self, hand):
    return self.point_total(1, hand[0], hand[1], hand[2], hand[3], hand[4])


def main():
  # User inputs number of hands to play
  numHands = int (input ('Enter number of hands to play: '))
  while (numHands < 2 or numHands > 6):
    numHands = int (input ('Enter number of hands to play: '))
  # Play poker
  game = Poker (numHands)
  game.play()

main()
