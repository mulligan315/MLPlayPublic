import random
selection = ['rock','paper','scissors']
randNumber = random.randint(0,2)
compSelect=selection[randNumber]
userInt=int(input("Please enter '0' for rock, '1' for paper, '2' for scissors, and '8' for exit.\n"))
compScore = 0
userScore = 0
while userInt != 8:
    randNumber = random.randint(0,2)
    compSelect=selection[randNumber]
    userSelection = selection[userInt]
    print("You selected "+userSelection+".")
    if compSelect == userSelection:
        print("The Computer also selected "+compSelect+".  It's a tie!")
    elif compSelect =="rock":
        print("The Computer selected rock.")
        if userSelection == "paper":
            print("Paper covers rock. You win!")
            userScore +=1
        elif userSelection == "scissors":
            print("Rock smashed scissors. You lose!")
            compScore +=1
    elif compSelect == "paper":
        print("The Computer selected paper.")
        if userSelection == "rock":
            print("Paper covers rock. You lose!")
            compScore +=1
        elif userSelection == "scissors":
            print("Scissors cut paper. You win!")
            userScore +=1
    elif compSelect =="scissors":
        print("The Computer selected scissors.")
        if userSelection == "rock":
            print("Rock smashed scissors. You win!")
            userScore +=1
        elif userSelection == "scissors":
            print("Scissors cut paper. You lose!")
            compScore +=1
            
    print("\nComputer: "+str(compScore)+" User: "+str(userScore))
    userInt=int(input("\nPlease enter '0' for rock, '1' for paper, '2' for scissors, and '8' for exit.\n"))
