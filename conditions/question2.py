day = input("Enter the day : ")
age = int(input("Enter the age : "))
if day.lower() == "wednesday" :
    if age >= 18:
        print("Your ticket price is $10 ")
    else :
        print("Your ticket price is $6")
else:
    if age >= 18:
        print("Your ticket price is $12 ")
    else :
        print("Your ticket price is $8")
    