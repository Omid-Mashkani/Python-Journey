
  #Project: Score Review Evaluator
    #Author: Omid Mashkani
    #Description: A simple script to evaluate grades using loops and conditionals.


#کدی از امید - code from omid

print("Hello! Im ready to review your score.")
print("To exit, enter the number 0.")

while True:
    n = float(input(" Enter your score: "))

    if n == 0:
        print("Goodbye! Good job."  )
        break
    
    elif n > 20:
        print("Please enter a number smaller than 20.")

    elif n >= 10:
        print("Congratulations! You got in.")
    
    elif n < 0:
        print("Please enter a number greater than 0.   ")

    else:
        print("Unfortunately, your grades are low. you need to put in more effort.")
