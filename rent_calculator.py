# here we are calculating the total bill amount and individual cost for each person
# living in a hostel/flat based on their rent, food expenses, electricity expenses,
# and the number of persons sharing the expenses.
rent = int(input("Enter your Hostel/Flat rent amount: "))
food = int(input("Enter your Food expenses amount: "))
electricity_spend = int(input("Enter your Electricity units consumed: "))
charge_per_unit = int(input("Enter your Electricity charge per unit: "))
persons = int(input("Enter the number of persons living in the hostel/flat: "))

total_bill = rent + food
electricity_cost = electricity_spend * charge_per_unit
money = total_bill + electricity_cost
print("Total bill amount is:", money)
individual_cost = money / persons
print("Each person has to pay:", individual_cost)