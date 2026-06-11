# what kind of inputs we are taking from the end user
# total rents
# total food orders
# electricity units soends
# charge per units


# output
# total amount you've to pay is 


try :
    total_rent = int(input("Enter your total rent = "))
    total_food_cost = int(input("Enter the total amount you have spend on food"))
    total_roomates = int(input("How many roomates do you have ? "))
    unit_spend = int(input("Enter the total electricity unit you have used ? "))
    ele_unit = int(input("ENter the charge of per units = "))
    total = (total_rent/total_roomates) + (total_food_cost/total_roomates) +((unit_spend*ele_unit)/total_roomates)
except ValueError:
    print("Enter the valide values = ")

else:
    print(f"Spend on Rent = {total_rent/total_roomates}")
    print(f"Spend on Food = {total_food_cost/total_roomates}")
    print(f"total spend on electricty = {(unit_spend*ele_unit)/total_roomates}")
    print(f"the total spend = {total}")
finally:
    print("Thank you ")   