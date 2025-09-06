#Contribution: Creating main function for more optimal use.
from calculator import *
from area_circle import *

def main():
    print("\n******************************")
    print("*** Welcome to Calculator! ***")
    print("******************************\n")
    print("Please select a operation you would like to perform by typing its name.\n")

    menu_txt = "--> Add\n--> Subtract\n--> Multiply\n--> Divide\n--> Power\n--> Square\n--> Square Root\n--> Circle Area"
    exit_txt = "That didn't match a operation or it was mispelled.\nExiting..."

    print(menu_txt)
    user_inp = input("Operation: ")

    match user_inp:
        case "Add" | "add":
            print("TESTing")
        case "Subtract" | "subtract":
            print("TESTING")
        case "Multiply" | "multiply":
            print("TESTING")
        case "Divide" | "divide":
            print("TESTING")
        case "Power" | "power":
            print("TESTING")  
        case "Square" | "square":
            print("TESTING")
        case "Square Root" | "square root":
            print("TESTING")
        case "Circle Area" | "circle area":
            print(area_circle())   
        case _:
            print(exit_txt)

if __name__ == "__main__":
    main()