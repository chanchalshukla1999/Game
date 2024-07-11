import random
print("Winning Rule Of Game are:\n"
      +"Rock Vs Paper -> Paper Win:\n"
      +"Rock Vs Scissor -> Rock Win:\n"
      +"Scissor Vs Paper -> Scissor Win\n")
while True:
    print("Enter Your Choice \n 1 - Rock \n 2 - Paper \n 3 - Scissor\n")
    choice = int(input("Enter Your Choice:"))
    if choice == 1:
        choice_name = "Rock"
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissor"
        
        while choice > 3 or  choice < 1:
            choice = int(input("Enter Valid Choice As Per The Game Instruction:"))
    print("Your Entered Choice Is:\n",choice_name)
    print("Now Its Computer Turn.......")
    comp_choice = random.randint(1,3)

    while comp_choice == choice:
        comp_choice = random.randint(1,3)

    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissor"
    print("Computer Choice:",comp_choice_name)
    print(comp_choice_name ,"Vs" ,choice_name)
# condition of lossing the game
    if (choice == comp_choice):
        print("Its a Draw:",end="")
        result = "DRAW"
# condition of winning   
    if (choice == 1 and comp_choice == 2):
        print("Paper Wins =>",end="")
        result = "Paper"
    elif(choice == 2 and comp_choice == 1):
        print("Paper Wins =>",end="")
        result = "Paper"

    if (choice == 1 and comp_choice == 3):
        print("Rock Wins =>",end="")
        result = "Rock"
    elif(choice == 3 and comp_choice == 1):
        print("Rock Wins =>",end="")
        result = "Rock"
    if (choice == 2 and comp_choice == 3):
        print("Scissor Wins =>",end="")
        result = "Scissor"
    elif(choice == 3 and comp_choice == 2):
        print("Scissor Wins =>",end="")
        result = "Scissor"
    
    if result == "DRAW":
        print("<== Its a Tie ==>")
    elif result == choice_name:
        print("<== User Wins ==>")
    else:
        print("<== Computer Wins ==>")
        print("Do You Want To Play Again?(Y/N)")
    ans =input().lower()
    if ans == "n":
        break
Print("Thanks for Playing:")

    




 

