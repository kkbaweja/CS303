#  File: Hailstone.py

#  Description: A program that computes the hailstone sequence for every number in a user defined range

#  Student Name: Keerat Baweja 

#  Student UT EID: kkb792

#  Course Name: CS 303E

#  Unique Number: 50860

#  Date Created: 2/7/2016

#  Date Last Modified: 2/9/2016

def main():
  # Prompt the user to enter the starting number 
  start = input("\nEnter starting number of the range: ")

  # Prompt the user to enter the ending number 
  finish = input("\nEnter ending number of the range: ")

  # Check to make sure start is positive
  while (start <= 0):
    start = input("\nEnter starting number of the range: ")
    finish = input("\nEnter ending number of the range: ")
	
  # Check to make sure the end is positive	
  while (finish <= 0):
    start = input("\nEnter starting number of the range: ")
    finish = input("\nEnter ending number of the range: ")
    while (start <= 0):
      start = input("\nEnter starting number of the range: ")
      finish = input("\nEnter ending number of the range: ")
	  
  # Check to make sure the start is smaller than the end   
  while (start >= finish):
    start = input("\nEnter starting number of the range: ")
    finish = input("\nEnter ending number of the range: ")
    while (start <= 0):
      start = input("\nEnter starting number of the range: ")
      finish = input("\nEnter ending number of the range: ")
    while (finish <= 0):
      start = input("\nEnter starting number of the range: ")
      finish = input("\nEnter ending number of the range: ")
      while (start <= 0):
        start = input("\nEnter starting number of the range: ")
        finish = input("\nEnter ending number of the range: ")
  
  # Initialize variables
  max_num = 0
  number = start
  max_cycle_length = 0 
   
  # Perform the calculation to find the hailstone sequence for each number in the range
  while (number <= finish):
    result = number
    cycle_length = 0
    while (result != 1):
      if (result % 2 == 0):
        result = result // 2
      elif (result % 2 == 1):
        result = 3*result + 1
      cycle_length = cycle_length + 1
    if (cycle_length >= max_cycle_length):
      max_cycle_length = cycle_length 
      max_num = number
    number = number + 1
  
  # Print out result 
  print("")
  print ("The number", max_num, "has the longest cycle length of", str(max_cycle_length) + ".")
 	
# Call main function 
main()
