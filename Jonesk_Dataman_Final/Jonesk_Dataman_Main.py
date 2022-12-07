# -*- coding: utf-8 -*-
"""
CTS-285
Kevin Jones
Final Project
11/5/22

"""



import random



def guess():
    print("Welcome to the number guesser. Generating a number between 1 and 99.")
    num = random.randrange(1,10)
    think = int(input("Enter any number: "))
    if think < num:
            print("Too Low")
            think = int(input("Enter another number: "))
    elif think > num:
             print("Too high")
             think = int(input("Enter another number: "))
    elif think == num:
            print("Good job, you guessed it.")
            again = int(input("Would you like to play again? 1 for yes and 2 for no."))
            if again == 1:
                guess()
            else:
                print("Returning to main menu.")
                main()
            
                


                guess()



def main():
    print("Welcome to the Starman Calculation System!")
    print("Please choose one of out availble features using the numbered list below.")
    print("1. Starman Answer Checker")  
    print("2. Starman Data Bank")
    print("3. Starman Random Number Guesser")
    print("4. Exit")   
    choice = int(input("\nEnter a number: "))
    if choice == 1:
        import Jonesk_AnswerChecker_M2HW2 as AC
        AC.main1()
    elif choice == 2:
        import Jonesk_DataBank as DB
        DB.Main2()
    elif choice == 3:
        guess()
    elif choice == 4:
        print("Thank you for playing. Come back soon!")
        exit()
    else:
        print("Thank you for playing. Come back soon!")
    
    
    
    
    
    
    
main()