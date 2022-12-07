# -*- coding: utf-8 -*-
"""
CTS-285
Kevin Jones
M2HW2
11/28/22

"""
#imports and variables
import random
num1 = float()
num2 = float()
num3 = float()

#addition module
def add():
    num1=random.randint(1, 10)
    num2=random.randint(1, 10)
    num3 = (num1 + num2)
    print("Now creating an addition problem.")
    print(" what is ", num1, " + ",num2," ?") 
    userAnswer = int(input("What is your answer? : "))
    if userAnswer != num3:
        print("Incorrect, please try again. ")
        print(" what is ", num1, " + ",num2," ?") 
        userAnswer = int(input("What is your answer? : "))
        if userAnswer != num3:
            print("Incorrect, the answer was ",num3)
            print("Returning to main menu, please try again.")
            main1()
        elif userAnswer == num3:
            print("Wonderful job!, would you like another question?")
            Lap = int(input("Please choose 1 for yes, or 2 for no."))
            if Lap == ("1"):
                add()
            else:
                print("Answer recieved, returning to the main menu.")
                main1()
    elif userAnswer == num3:
        print("Wonderful job!, would you like another question?")
        Lap = int(input("Please choose 1 for yes, or 2 for no."))
        if Lap == 1:
            add()
        else:
            print("Answer recieved, returning to the main menu.")
            main1()

#subtaction module
def sub():
    num1=random.randint(1, 10)
    num2=random.randint(1, 10)
    num3 = (num1 - num2)
    print("Now creating a subtraction problem.")
    print(" what is ", num1, " - ",num2," ?") 
    userAnswer = int(input("What is your answer? : "))
    if userAnswer != num3:
        print("Incorrect, please try again. ")
        print(" what is ", num1, " - ",num2," ?") 
        userAnswer = int(input("What is your answer? : "))
        if userAnswer != num3:
            print("Incorrect, the answer was ",num3)
            print("Returning to main menu, please try again.")
            main1()
        elif userAnswer == num3:
            print("Wonderful job!, would you like another question?")
            Lap = int(input("Please choose 1 for yes, or 2 for no."))
            if Lap == ("1"):
                sub()
            else:
                print("Answer recieved, returning to the main menu.")
                main1()
    elif userAnswer == num3:
        print("Wonderful job!, would you like another question?")
        Lap = int(input("Please choose 1 for yes, or 2 for no."))
        if Lap == 1:
            sub()
        else:
            print("Answer recieved, returning to the main menu.")
            main1()
            
#multiplication module
def mul():
    num1=random.randint(1, 10)
    num2=random.randint(1, 10)
    num3 = (num1 * num2)
    print("Now creating a multiplication problem.")
    print(" what is ", num1, " x ",num2," ?") 
    userAnswer = int(input("What is your answer? : "))
    if userAnswer != num3:
        print("Incorrect, please try again. ")
        print(" what is ", num1, " x ",num2," ?") 
        userAnswer = int(input("What is your answer? : "))
        if userAnswer != num3:
            print("Incorrect, the answer was ",num3)
            print("Returning to main menu, please try again.")
            main1()
        elif userAnswer == num3:
            print("Wonderful job!, would you like another question?")
            Lap = int(input("Please choose 1 for yes, or 2 for no."))
            if Lap == ("1"):
                mul()
            else:
                print("Answer recieved, returning to the main menu.")
                main1()
    elif userAnswer == num3:
        print("Wonderful job!, would you like another question?")
        Lap = int(input("Please choose 1 for yes, or 2 for no."))
        if Lap == 1:
            mul()
        else:
            print("Answer recieved, returning to the main menu.")
            main1()

#division module
#this module is a bit scuffed, having trobule with registering correct answers with decimal points.

def div():
    num1=random.randint(1, 10)
    num2=random.randint(1, 10)
    num3 = (num1 / num2)
    print("Now creating a divison problem.")
    print(" what is ", num1, " / ",num2," ?") 
    userAnswer = input("What is your answer? : ")
    if userAnswer != num3:
        print("Incorrect, please try again. ")
        print(" what is ", num1, " / ",num2," ?") 
        userAnswer = input("What is your answer? : ")
        if userAnswer != num3:
            print("Incorrect, the answer was ",num3)
            print("Returning to main menu, please try again.")
            main1()
        elif userAnswer == num3:
            print("Wonderful job!, would you like another question?")
            Lap = int(input("Please choose 1 for yes, or 2 for no. "))
            if Lap == ("1"):
                div()
            else:
                print("Answer recieved, returning to the main menu.")
                main1()
    elif userAnswer == num3:
        print("Wonderful job!, would you like another question?")
        Lap = int(input("Please choose 1 for yes, or 2 for no. "))
        if Lap == 1:
            div()
        else:
            print("Answer recieved, returning to the main menu.")
            main1()





#main/menu
def main1():
#Menu
    while True:  
        print("Welcome to the Starman answer checker System! Please choose which type of problem you would like to be tested with.")    
        print("1. Add")  
        print("2. Subtract")  
        print("3. Multiply")  
        print("4. Divide")
        print("5. Return to main menu")
        print("6. Exit")  
        users_choice = int(input("\nEnter a number: "))
        if users_choice == 1:
            add()
        elif users_choice == 2:
            sub()
        elif users_choice == 3:
            mul()
        elif users_choice == 4:
            div()
        elif users_choice == 5:
            import Jonesk_Dataman_Main.main as DM
            DM.main()
            
        elif users_choice == 6:
            print("Thank you for playing. Come back soon!")
            exit()
        else:
            print("Please choose a listed option")
            main1()
        
        
main1()