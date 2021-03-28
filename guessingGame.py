import random
number = random.randint(1,9)
guess = input("Enter a number between 1 and 9")
chances = 0

while chances < 5 : 
    for i in guess :
        chances = chances + 1
        

        if chances == 1:
            print("Try again.The no. is greater than",number-5 )
            guess=input("Enter the number")
            break
        if chances == 2:
            print("Try again.The no. is greater than",number-4 )
            guess=input("Enter the number")
            break
        if chances == 3:
            print("Try again.The no. is greater than",number-3 )
            guess=input("Enter the number")
            break
        if chances == 4:
            print("Try again.The no. is greater than",number-2 )
            guess=input("Enter the number")
            break
        if guess == number : 
            print("Congraulations !! You won !!")
            break
        if not chances < 5 :
            print("YOU LOSE !! The number is",number)
            break