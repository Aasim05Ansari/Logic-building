def add(x, y):
    return x + y
def substract(x, y):
    return x - y
def divide(x, y):
    if y == 0:
        print("Cannot divide with zero !")
    return x / y
def multiply(x, y):
    return x * y

def calculator():
    while True:
        try:
            num1=float(input("Enter the first number: "))
            num2=float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input, please enter numbers only. ")
            continue

        print("Select operation: ")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit the calculator !")
        choice = input("Select a valid choice among (1/2/3/4/5) : ")
        if choice in ('1', '2', '3', '4', '5'):
            if choice == 1:
                print(num1, "+", num2, "=",add(num1, num2))
            elif choice == 2:
                print(num1 ,"-", num2, "=" ,substract(num1, num2))
            elif choice == 3:
                print(num1 ,"*", num2, "=" ,multiply(num1, num2))
            elif choice == 4:
                print(num1, "/" , num2, "=" ,divide(num1, num2))
        elif choice == 5:
                print("Exiting calculator !")
                break
        else:
                print("Enter the valid input !!")

            
if __name__ == "__main__":
    calculator()
            
