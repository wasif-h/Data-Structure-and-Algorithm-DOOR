# Basic Even ODD Analysis

num = int(input("Enter num : "))

if(num > 0):
    if(num % 2 == 0):
        print("Even")
    else:
        print("Odd")
elif(num < 0):
    print("Negative Number")
elif(num == 0):
    print("Zero")
else:
    print("Invalid Entry")



