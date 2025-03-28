

#Guess a random number
import math  
import random

playing = True
number = str(random.randint(10,20))

print("I will generate random numbers between 10 and 20")

while playing:
    guess =input("Guess a number between 10 and 20")
    if number == guess:
        print("You win")
        print("The number guessed was")
        break
    else:
        print("Your guess was wrong try again !")
        
        

#rock paper scissors

import random

options = ["Rock", "Paper", "Scissors"]

user_choice = input("Choose Rock, Paper, or Scissors: ")

computer_choice = random.choice(options)

print("You chose:", user_choice)
print("Computer chose:", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "Rock" and computer_choice == "Scissors":
    print("Rock smashes scissors! You win!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("Paper covers rock! You win!")
elif user_choice == "Scissors" and computer_choice == "Paper":
    print("Scissors cuts paper! You win!")
else:
    print("You lose!. ")
    
#math module 

print(math.sin(45))
print(math.cos(45))
print(math.tan(45))

print(math.ceil(45.490))
print(math.floor(45.890))
print(math.factorial(5))

#activity 4
import math  #importing math module

x = float('nan')
if math.isnan(x): #to check whether the given value is number or not
    print('It is not a number')
x = float('inf')
y = 45
if math.isinf(x): #to check whether the given number is infinite or not
    print('It is Infinity')
print(math.isfinite(x)) #x is not a finite number
print(math.isfinite(y)) #y is a finite number

#acitvity5
import math #importing module

#isclose function to check whether to value are close or not

print(math.isclose(12.014, 12.56))

print(math.isclose(12.014, 12.014))

print(math.isclose(12.45, 12.46))

print(math.isclose(12.014, 12.434, abs_tol = 0.5))

print(math.isclose(12.014, 12.018, rel_tol = 0.2))





