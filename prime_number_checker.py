#prime number checker program
while True:
    boring = input("\nIf you want to quit press 'q' : ")
    if boring == 'q':
        break

    num = int(input("\nEnter the num : "))
    if num % 2 == 0:
        print(f"The number {num} is not a prime !")
    else:
        print(f"The number {num} is prime !")
