#Question 4

grade_point=int(input("Enter Your Grade Points= "))
if (4<=grade_point<=10):
    if (grade_point==4):
        print("Performance=Poor\nLetter Grade=D")
    elif (grade_point==5):
        print("Perforn=mance=Below Average\nLetter Grade=C")
    elif (grade_point==6):
        print("Performance=Average\nLetter Grade=C+")
    elif (grade_point==7):
        print("Performance=Good\nLetter Grade=B")
    elif (grade_point==8):
        print("Performnace=Very Good\nLetter Grade=B+")
    elif (grade_point==9):
        print("Performance=Excellent\nLetter Grade=A")
    elif (grade_point==10):
        print("Performance=Outstanding\nLetter Grade=A+")
else:
    print("Error")
