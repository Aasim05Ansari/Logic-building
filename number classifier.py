while True:
    boring = input("\nIf you want to quit enter 'q' : ")
    if boring.lower() == 'q':
        break

    number1 = int(input("\nEnter the 1st number : "))
    number2 = int(input("\nEnter the 2nd number : "))
    number3 = int(input("\nEnter the 3rd number : "))

    if number1 >= number2 and number1 >= number3:
        print(f"\n{number1} is the greatest number.")
    elif number2 >= number1 and number2 >= number3:
        print(f"\n{number2} is the greatest number.")
    else:
        print(f"\n{number3} is the greatest number.")
