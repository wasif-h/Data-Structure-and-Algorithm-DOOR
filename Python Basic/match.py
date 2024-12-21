grade = input("Enter your Grade : ").upper()

match(grade):
    case 'A+':
        print("Great Work, Champ")
    case 'A':
        print("Great Work, Try Better Next Time")
    case 'B':
        print("Good , But u can do more")
    case 'F':
        print("No Worries - Try Again")
    case _:
        print("Invalid Entry")
    