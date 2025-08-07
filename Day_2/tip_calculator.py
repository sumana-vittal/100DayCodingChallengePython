print("Welcome to the tip calculator!")
bill = input("What was the total bill? : $")
if bill.isnumeric() :
    bill = float(bill)
    tip = input("How much tip would you like to give? 10,12, or 15? ")
    if tip.isnumeric():
        tip = float(tip)
        no_of_people = input("How many people to split the bill? ")

        if no_of_people.isnumeric():
            no_of_people = int(no_of_people)
            bill_with_tip = bill + (bill * tip / 100)
            final_amt_per_person = bill_with_tip / no_of_people

            print(f"Each person should pay: ${round(final_amt_per_person, 2)}")
        else:
            print("Number of people to split should be an integer.")
    else:
        print("tip amount should be number")
else:
    print("total bill should be decimal or integer")



