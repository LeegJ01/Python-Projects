# This is a tip calculator I created while trying to learn basic python through a Udemy online self-paced class. 

print("Welcome to the Tip Calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12,0r 15?"))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount_per_person = round(bill_per_person, 2)
final_amount_per_person = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: {final_amount_per_person}")
