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
comp_win=0
comp_loss=0
comp_draw=0
player_win=0
player_loss=0
player_draw=0
totalGames=0
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
    ### Converting ints to be global to work within function
    global comp_win
    global comp_loss
    global comp_draw
    global player_win
    global player_loss
    global player_draw 
    choice = intString(playerChoice)
    print ("Player chooses " + choice+"\n")
    compChoice = random.randrange(0,5)
    print ("Computer chooses " + intString(compChoice)+"\n")
    if playerChoice == compChoice:
        print("it's a draw!\n")
        player_draw+=1
        comp_draw+=1
    elif(playerChoice,compChoice) in results:
        print("Player wins!\n")
        player_win+=1
        comp_loss+=1
    elif(compChoice,playerChoice) in results:
        print("Computer wins!\n")
        player_loss+=1
        comp_win+=1
        ###
###Delivers computers results
def comp_results():
    print("\nComputer stats:\n"+'Wins:'+str(comp_win)+"\n"+'Losses:'+str(comp_loss)+"\n"+'Draws:'+str(comp_draw)+'\n')
    return
###Delivers Players results
def player_results():
    print('\n'+ name+" stats:\n"+'Wins:'+str(player_win)+"\n"+'Losses:'+str(player_loss)+"\n"+'Draws:'+str(player_draw)+'\n')
    return
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
while menu == 0:
    name = input("Who is playing? ")
    print("Thank you\n")
    main()
    menu = input(':')
#Starts the game and if the game is exited using the 5 option it appends it to a text file
while int(menu) == 1:
    print("Pick your choice to play against the computer!\n0 - rock\n1 - paper\n2 - scissors\n3 - lizard\n4 - spock\n5 - quit")
    playerChoice = int(input(":"))
    rpsls(playerChoice)
    if playerChoice == 5:
        outcome = open ("roshambo-stats.txt","a")
        outcome.write(str(comp_results))
        outcome.write(str(player_results))
        outcome.close()
        menu = 0
        main()
        menu = input(':')
    

### Gives the amount of wins losses and draws a user has gotten during the session
while int(menu) == 2:
    print("Welcome to the stats screen!\nWho's stats would you like to see?")
    statChoice = input("1: Computer Stats\n2: Player Stats\n3:Quit Stats Check\n:")
    if int(statChoice) == 1:
        comp_results()
    if int(statChoice) == 2:
        player_results()
    if int(statChoice) == 3:
        menu=0
        main()
        menu = input(':')
    
