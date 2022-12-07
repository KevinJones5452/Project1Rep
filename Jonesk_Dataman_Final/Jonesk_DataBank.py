# -*- coding: utf-8 -*-
"""
CTS-285
Kevin Jones
M2HW2
11/28/22

"""
#imports and variables
import random


bank = []
Answers = []


def Assign():
    
    print("Please enter 10 Problems to fill the data bank")

    for i in range(0, 10):
        num1 = input("Enter a number: ")
        do_what = input("Enter calculation symbols for calculation you want to perform: ")
        num2 = input("Enter another number: ")
        if do_what=='+':
             que = float(num1) + float(num2)
        elif do_what=='-':
             que = float(num1) - float(num2)
        elif do_what=='*':
                 que = float(num1) * float(num2)
        elif do_what=='/':
                 que = float(num1) / float(num2)
        bank.append(num1)
        bank.append(do_what)
        bank.append(num2)
        Answers.append(que)
        
        print(bank)
        print(Answers)
        print(" ")
        print(" ")
    print("Returning to main menu, you are now ready to use option 2 in the main menu.")
    Main2()
    Assign()

def Problem():
    (map(int, Answers))
    print(" Generating problems from the data bank.")
    Cho=random.randint(1, 10)
    Cho = 1
    if(Cho == 1):
            Ans = input(bank[0:3])
            print(int(Answers[0]))
            print(":")
            if(Ans == (int(Answers[1]))):
                Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                if(Rep == 1):
                    Problem()
                elif(Rep == 2):
                    print("Thank you, returning to main menu.")
                    Main2()
            elif(Ans != (int(Answers[1]))):
                print("Incorrect, please try again.")
                Ans = input(bank[0:3])
                print(":")
                if(Ans == (int(Answers[1]))):
                    Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                    if(Rep == 1):
                        Problem()
                    elif(Rep == 2):
                        print("Thank you, returning to main menu.")
                    Main2()
                elif(Ans != (int(Answers[1]))):
                    print("Incorrect, please review and try again. Returning to main menu.")
                    Main2()
    elif(Cho == 2):
            Ans = input(bank[3:6])
            print(":")
            if(Ans == (Answers[1])):
                Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                if(Rep == 1):
                    Problem()
                elif(Rep == 2):
                    print("Thank you, returning to main menu.")
                    Main2()
            elif(Ans != (Answers[1])):
                print("Incorrect, please try again.")
                Ans = input(bank[3:6])
                print(":")
                if(Ans == (Answers[1])):
                    Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                    if(Rep == 1):
                        Problem()
                    elif(Rep == 2):
                        print("Thank you, returning to main menu.")
                    Main2()
                elif(Ans != (Answers[1])):
                    print("Incorrect, please review and try again. Returning to main menu.")
                    Main2()
                    
    elif(Cho == 3):
            Ans = input(bank[6:9])
            print(":")
            if(Ans == (Answers[2])):
                Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                if(Rep == 1):
                    Problem()
                elif(Rep == 2):
                    print("Thank you, returning to main menu.")
                    Main2()
            elif(Ans != (Answers[2])):
                print("Incorrect, please try again.")
                Ans = input(bank[6:9])
                print(":")
                if(Ans == (Answers[2])):
                    Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                    if(Rep == 1):
                        Problem()
                    elif(Rep == 2):
                        print("Thank you, returning to main menu.")
                    Main2()
                elif(Ans != (Answers[2])):
                    print("Incorrect, please review and try again. Returning to main menu.")
                    Main2()
                    
    elif(Cho == 4):
            Ans = input(bank[9:12])
            print(":")
            if(Ans == (Answers[3])):
                Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                if(Rep == 1):
                    Problem()
                elif(Rep == 2):
                    print("Thank you, returning to main menu.")
                    Main2()
            elif(Ans != (Answers[3])):
                print("Incorrect, please try again.")
                Ans = input(bank[9:12])
                print(":")
                if(Ans == (Answers[3])):
                    Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                    if(Rep == 1):
                        Problem()
                    elif(Rep == 2):
                        print("Thank you, returning to main menu.")
                    Main2()
                elif(Ans != (Answers[3])):
                    print("Incorrect, please review and try again. Returning to main menu.")
                    Main2()
                    
    elif(Cho == 5):
            Ans = input(bank[12:15])
            print(":")
            if(Ans == (Answers[4])):
                Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                if(Rep == 1):
                    Problem()
                elif(Rep == 2):
                    print("Thank you, returning to main menu.")
                    Main2()
            elif(Ans != (Answers[4])):
                print("Incorrect, please try again.")
                Ans = input(bank[12:15])
                print(":")
                if(Ans == (Answers[4])):
                    Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                    if(Rep == 1):
                        Problem()
                    elif(Rep == 2):
                        print("Thank you, returning to main menu.")
                    Main2()
                elif(Ans != (Answers[4])):
                    print("Incorrect, please review and try again. Returning to main menu.")
                    Main2()
                    
    elif(Cho == 6):
            Ans = input(bank[15:18])
            print(":")
            if(Ans == (Answers[5])):
                Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                if(Rep == 1):
                    Problem()
                elif(Rep == 2):
                    print("Thank you, returning to main menu.")
                    Main2()
            elif(Ans != (Answers[5])):
                print("Incorrect, please try again.")
                Ans = input(bank[15:18])
                print(":")
                if(Ans == (Answers[5])):
                    Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                    if(Rep == 1):
                        Problem()
                    elif(Rep == 2):
                        print("Thank you, returning to main menu.")
                    Main2()
                elif(Ans != (Answers[5])):
                    print("Incorrect, please review and try again. Returning to main menu.")
                    Main2()
                    
    elif(Cho == 7):
            Ans = input(bank[18:21])
            print(":")
            if(Ans == (Answers[6])):
                Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                if(Rep == 1):
                    Problem()
                elif(Rep == 2):
                    print("Thank you, returning to main menu.")
                    Main2()
            elif(Ans != (Answers[6])):
                print("Incorrect, please try again.")
                Ans = input(bank[18:21])
                print(":")
                if(Ans == (Answers[6])):
                    Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                    if(Rep == 1):
                        Problem()
                    elif(Rep == 2):
                        print("Thank you, returning to main menu.")
                    Main2()
                elif(Ans != (Answers[6])):
                    print("Incorrect, please review and try again. Returning to main menu.")
                    Main2()
                    
    elif(Cho == 8):
            Ans = input(bank[21:24])
            print(":")
            if(Ans == (Answers[7])):
                Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                if(Rep == 1):
                    Problem()
                elif(Rep == 2):
                    print("Thank you, returning to main menu.")
                    Main2()
            elif(Ans != (Answers[7])):
                print("Incorrect, please try again.")
                Ans = input(bank[21:24])
                print(":")
                if(Ans == (Answers[7])):
                    Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                    if(Rep == 1):
                        Problem()
                    elif(Rep == 2):
                        print("Thank you, returning to main menu.")
                    Main2()
                elif(Ans != (Answers[7])):
                    print("Incorrect, please review and try again. Returning to main menu.")
                    Main2()
                    
    elif(Cho == 9):
            Ans = input(bank[24:27])
            print(":")
            if(Ans == (Answers[8])):
                Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                if(Rep == 1):
                    Problem()
                elif(Rep == 2):
                    print("Thank you, returning to main menu.")
                    Main2()
            elif(Ans != (Answers[8])):
                print("Incorrect, please try again.")
                Ans = input(bank[24:27])
                print(":")
                if(Ans == (Answers[8])):
                    Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                    if(Rep == 1):
                        Problem()
                    elif(Rep == 2):
                        print("Thank you, returning to main menu.")
                    Main2()
                elif(Ans != (Answers[8])):
                    print("Incorrect, please review and try again. Returning to main menu.")
                    Main2()
                    
    elif(Cho == 10):
            Ans = input(bank[27:30])
            print(":")
            if(Ans == (Answers[9])):
                Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                if(Rep == 1):
                    Problem()
                elif(Rep == 2):
                    print("Thank you, returning to main menu.")
                    Main2()
            elif(Ans != (Answers[9])):
                print("Incorrect, please try again.")
                Ans = input(bank[27:30])
                print(":")
                if(Ans == (Answers[9])):
                    Rep = int(input("Nice Job! Would you like another problem? 1 for yes, 2 for no."))
                    if(Rep == 1):
                        Problem()
                    elif(Rep == 2):
                        print("Thank you, returning to main menu.")
                    Main2()
                elif(Ans != (Answers[9])):
                    print("Incorrect, please review and try again. Returning to main menu.")
                    Main2()
                    

                
        
        
    
    
    
    Problem()


def Main2():
    print("Welcome to the Starman Data bank! Please use option 1 to create problems before using other options.")
    print("1. Add problems to the Data Bank")  
    print("2. Answer Problems for the Data Bank")
    print("3. Return to main menu")
    print("4. Exit")   
    users_choice = int(input("\nEnter a number: "))
    if users_choice == 1:
            Assign()
    elif users_choice == 2:
            Problem()
    elif users_choice == 3:
        import Jonesk_Dataman_Main.main as DM
        DM.main()
    elif users_choice == 4:
            print("Thank you for playing. Come back soon!")
            exit()
    else:
            print("Please choose a listed option")
Main2()