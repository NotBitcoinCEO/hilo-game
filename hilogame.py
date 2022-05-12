#HiLO game by Sean Layton (NotBitcoinCEO)
#instructions      
print("\n")
print("Welcome to the HiLo game for BYU-I CSE 210!")
print("Enter a number from 1-13.")
print("100 points FOR Gryffindor for a correct number.")
print("75 point FROM Gryffindor for an incorrect number.")
print("\n")


import random
score=300
print("Your current score is:",score)   
x=(random.randint(1,13))
guess=0

while guess != x and score > 0:
    guess= int(input("Guess at your own risk!"))

    if guess > x:
        print("Your guess was too high Try again.")
    if guess < x:
        print("Your guess was too low. Try again.")
    if guess == x: 
        print("Congrats, you are a winner!!")
    # if guess != int(1-13) and x >0: 
    #     print("That's an incorrect POTTER! 75 points from Gryffindor!")
        #subtract 75 points from score       

if guess == x:
    print("You won, good job!")


if guess <=0:
    print("Do or do not, there is no try.")



    # ---------------------------
