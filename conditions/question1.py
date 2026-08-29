Age = int(input("Enter the age in numbers: "))
if Age < 13:
    print("Child.")
elif 19 > Age > 13:
    print("Teenager.")
elif 59 > Age > 20:
    print("Adult.")
else:
    print("Senior.")