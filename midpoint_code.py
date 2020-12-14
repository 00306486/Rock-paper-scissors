#Anthony Rodriguez 00306486
#12/8/20
#Intro to programming final
##
#In this program I will create a game of rock paper scissors lizard spoke, that will create and update a log
#of how many games it has played, who it has played with, and also keep track of how many times a player
#wins, loses or ties with the program.
###

#Imports
###
import random
###

#list
###
results = [(0,2),(2,1),(1,0),(0,3),
           (3,4),(4,2),(2,3),(3,1),(1,4),(4,0)]

#Variables needed for the code
###
menu = 0
playerChoice = 0
compChoice = 0
###

#Functions in code
###
#Main menu
def main():
    print("Welcome to Rock Paper Scissors Lizard Spock!\n What would you like to do?\n1:)Play the Game\n2:)Check Stats\n")
#work in progress tag
def inProg():
    print("This feature is being worked on")
#The game
def rpsls(playerChoice): 
    choise = intString(playerChoice)
    print ("Player chooses " + choise)
    compChoice = random.randrange(0,5)
    print ("Computer chooses " + intString(compChoice))
    if playerChoice == compChoice:
        print("it's a draw!")
    elif(playerChoice,compChoice) in results:
        print("Player wins!")
    elif(compChoice,playerChoice) in results:
        print("Computer wins!")
    
    print    
#Converts the choices of player and computer to strings
def intString(int):
    if int == 0:
        return "rock"
    elif int == 1:
        return "paper"
    elif int == 2:
        return "scissors"
    elif int == 3:
        return "lizard"
    elif int == 4:
        return "spock"
    else:
        return "Invalid number entered"
###
    
#Welcoming the user to Rpsls and what they would like to do within their main menu?
###
    ## Main menu
if menu == 0:
    main()
    menu = input(':')

while int(menu) == 1:
    print("Pick your choice to play against the computer!\n0 - rock\n1 - Spock\n2 - paper\n3 - lizard\n4 - scissors\n5 - quit")
    playerChoice = int(input(":"))
    rpsls(playerChoice)
    if playerChoice == 5:
        menu = 0
        main()
        menu = input(':')
    


if int(menu) == 2:
    inProg()
    
