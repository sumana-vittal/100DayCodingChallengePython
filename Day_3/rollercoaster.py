
height = int(input("Enter your height: "))

if height >= 120:
    age = int(input("Enter your age: "))
    if age < 12 :
        print("You pay $5")
    elif age > 12 and age < 18:
        print("you pay $7")
    else:
        print("you pay $12")
else:
    print("Can't ride")
