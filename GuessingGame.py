#  File: GuessingGame.py

#  Description: A guessing game that is based on the binary search algorithm 

#  Student Name: Keerat Baweja 

#  Student UT EID: kkb792		

#  Course Name: CS 303E

#  Unique Number: 50860 

#  Date Created: 4/13/2016

#  Date Last Modified: 4/13/2016

def main():
  # Ask the user to start the game
  print("Think of a number between 1 and 100 inclusive.\nAnd I will guess what it is in 7 tries or less.")
  print("")
  answer = input("Are you ready? (y/n): ")
  print("")
  while answer != 'n' and answer != 'y':
    answer = input("Are you ready? (y/n): ")
    print("")
  if answer == 'n':
    print("Bye")
    return

  # Initialize variables 
  lo = 0
  hi = 100
  mid = (lo + hi)//2
  response = '5'
  tries = 1

  # While loop to go through the guessing game 
  while response != '0' and tries <= 7:
    print("Guess", tries, ": The number you thought was", mid)
    response = input("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
    print("")
  
    # While loop to check for correct response and adjust low based on response from user 
    while response != '1' and response != '-1' and response != '0':
      print("Guess", tries, ": The number you thought was", mid)
      response = input("Enter 1 if my guess was high, -1 if low, and 0 if correct: ")
      print("")
	
    if response == '1':
      hi = mid
    elif response == '-1':
      lo = mid
    elif response == '0':
      print("Thank you for playing the Guessing Game.")
      return  
    mid = (lo + hi)//2
    tries += 1  
  
  # Print error message 
  print("Either you guessed a number out of range or you had an incorrect entry.")
  return 

main()

