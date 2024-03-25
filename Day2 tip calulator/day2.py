#Tip Calculate

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip percentage would you like to give? 5, 10, 12, or 15? %"))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
#bill_with_tip = bill * (1 + tip / 100)
total_bill = bill_with_tip / people
final_amount = round(total_bill, 2)
final_amount = '{:.2f}'.format(total_bill)
print(f"Each person is to pay ${final_amount} of the bill.")




