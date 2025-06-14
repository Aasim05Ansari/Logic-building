while True:
    boring = input("\nif you want to quit press 'q' : ")
    if boring == 'q':
        break
    num1 = int(input("Enter the number 1 :"))
    num2 = int(input("Enter the number 2 :"))
    num3 = int(input("Enter the number 3 :")) 


    if num1 > num2:
       print(f"\n{num1} is greater than {num2}")
    elif num2 > num1:
       print(f"\n{num2} is greater than {num1}")
    elif num3 > num1:
       print(f"\n{num3} is greater than {num1}")








