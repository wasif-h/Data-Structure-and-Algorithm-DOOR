i = 0
while (i < 5):
    print("Hello", i+1)
    i += 1

# pattern making
i = 0
while (i < 5):
    j = 0
    while (j < 7):
        print(j + 1, end=" ")
        j += 1

    i += 1
    print()

# do while loop by using while loop

n = 1
while True:
    print("Running.....")
    n += 1
    if(n > 3):
        break
    
v = 1
while True:
    print("Walking.....")
    v += 1
    if(v > 1):
        break
