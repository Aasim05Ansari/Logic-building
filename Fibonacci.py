num = int(input("Enter the number for fibonnaci sequence : "))
a,b = 0,1
for _ in  range(num):
    print(a, end='')
    a,b = b, a+b


