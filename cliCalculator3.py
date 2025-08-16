APP_NAME = "CALCULATOR"
print(APP_NAME)

initial_message = "Continuous Calculator"

operation_signs = ('+','-','*','/','=')


def main():
    result = None
    active = True
    print(initial_message)
    print(f'Use this signs for operation: \n{operation_signs}')
    while active:
        num = int(input("Enter a number:"))
        if result == None:
            result = num
            operation = input("Enter operation:")
            while operation not in operation_signs: 
                print("Dumbass")
                operation = input("Enter operation:")
            continue
        else:
            if operation == "+":
                result = adding(result,num)
            if operation == "-":
                result = subbing(result,num)
            if operation == "*":
                result = subbing(result,num)
            if operation == "/":
                result = subbing(result,num)
                
            print(f"Result: {result}")
            operation = input("Enter operation:")
            while operation not in operation_signs: 
                print("Dumbass")
                operation = input("Enter operation:")
                
            if operation == "=":
                print(f"Final Result: {result}")
                quit = input("Quit?[y/n]")
                if quit == "y" or quit == "Y":
                    active = False
                    break
                else: 
                    result = None
                    continue

    
        
def adding(num1, num2):
    return num1 + num2


def subbing(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2

main()