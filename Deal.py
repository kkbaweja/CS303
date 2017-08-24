# File: Deal.py

# Description: A program that simulates the game of Let's Make a Deal 

# Student Name: Keerat Baweja 

# Student UT EID: kkb792

# Course Name: CS 303E

# Unique Number: 50860 

# Date Created: 03/03/2016

# Date Last Modified: 03/03/2016

import math 
import random 

def main ():
  # prompt the user to enter the number of times they want to play the game 
  rounds = eval(input("Enter number of times you want to play: "))
  print("")
  print('{0:^9}{1:^13}{2:^10}{3:^11}'.format("Prize","Guess","View","New Guess"))

  # variable to keep track of how many times the contestant wins my switching 
  switch_wins = 0

  # while loop to play the game as many times as the user has asked 
  counter = 1
  while (counter <= rounds):
    prize = random.randint(1,3)
    guess = random.randint(1,3)
	  
	# calculate the value of view 
    if (prize != guess):
      view = 6 - prize - guess
    else:
      view = 1
      while (view == prize):
        view = view + 1
		
	# calculate the value of new guess
    newGuess = 6 - guess - view 
	
	# see if the contestant won by switching 
    if (newGuess == prize):
      switch_wins = switch_wins + 1
	  
	# print out results 
    print('{0:^9}{1:^13}{2:^10}{3:^11}'.format(prize,guess,view,newGuess))
    counter = counter + 1
	
  # calculate probabilities
  switch = switch_wins/rounds
  not_switch = 1 - switch
  
  # print out probabilities 
  print("")
  print("Probability of winning if you switch = ", "{0:.2f}".format(switch))
  print("Probability of winning if you do not switch = ", "{0:.2f}".format(not_switch))
main()