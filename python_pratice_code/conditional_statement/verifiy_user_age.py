person_Age = int(input("Enter the your age: "))

if person_Age<13:
    print("child")
elif person_Age<20:
    print("Teenager")
elif person_Age<60:
    print("Adult")
else:
    print("Senior citizen")
