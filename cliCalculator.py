APP_NAME = "CALCULATOR"
print(APP_NAME)

initial_message = "Pick a number to choose an operation:"

operations = ("additon", "subtraction", "multiplication", "division", "reminder", "quit")

def main():
    ACTIVE = True # this is the constand variable for the while loop in main()0
    while ACTIVE:
        print(initial_message)
        # equation = (input(operations.index(operation), operation) for operation in operations)
        for operation in operations:
            print(operations.index(operation), operation.title())
            
        try:
            operation = int(input(":"))
            print(f"You chose: {operations[operation].title()}")
        except ValueError:
            print("Choise is not on the list, try again")
            continue
        
        match operation:
            case 0:
                ans = adding()
                print(ans)
            case 1:
                ans = subbing()
                print(ans)
            case 2:
                ans = multiply()
                print(ans)
            case 3:
                ans = divide()
                print(ans)
            case 4:
                ans = reminder()
                print(ans)
            case 5:
                ACTIVE = False
                # active = [False if ans == 'quit'else True]
            case _:
                print("You input something wrong dumbass")
        
        
def adding():
    
    num1 = int(input("Enter first number:"))
    
    num2 = int(input("Enter second number:"))
    
    return num1 + num2


def subbing():
    
    num1 = int(input("Enter first number:"))
    
    num2 = int(input("Enter second number:"))
    
    return num1 - num2


def multiply():
    
    num1 = int(input("Enter first number:"))
    
    num2 = int(input("Enter second number:"))
    
    return num1 * num2


def divide():
    
    num1 = int(input("Enter first number:"))
    
    num2 = int(input("Enter second number:"))
    
    return num1 / num2


def reminder():
    
    num1 = int(input("Enter first number:"))
    
    num2 = int(input("Enter second number:"))
    
    return num1 % num2



main()