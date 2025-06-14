while True:
    boring = input("\nIf you are over with this game enter 'q' to quit : ")
    if boring == 'q':
        break


    number = int(input('\nEnter the number :'))
    if number % 2 == 0:
        print(f'\nThe number {number} is even !')
    else :
        print(f'\nThe number {number} is odd')

    
    
    
