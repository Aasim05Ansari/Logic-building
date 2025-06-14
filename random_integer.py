import random as rand
while True:
    bore = input("If you are bored you want to quit press 'q' : " )
    if bore == 'q':
        break
    num = int(input("Enter the number you want to guess : "))
    if num == rand.randint:
        print(f"You guessed the correct number {num}")
    else:
        print("Please try again !")