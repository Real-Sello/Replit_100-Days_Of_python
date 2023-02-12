#Extend your bill calculator
#A tip function that adds the total tip to the bill before splitting it equally between the people
print("=================================")
print("====== Bill-Tip calculator ======")
print("=================================")
print()
bill = float(input("How much money did you spend?: "))
print()
people = int(input("How many people?: "))
print()
tip_percentage = int(input("Tip percentage?: "))
print()
tip = bill * tip_percentage / 100
total_bill = bill + tip
total_per_person = total_bill / people

print("The total bill amount due is ", round(total_per_person, 2))