budget_food = int(input("Please set a budget for Food spending: "))
budget_entertainment = int(input("Please set a budget for Entertainment spending: "))
budget_transportation = int(input("Please set a budget for Transportation spending: "))
spending_food = 0
spending_entertainment = 0
spending_transportation = 0

purchase = 1

while True:
    purchase = int(input("Please enter a purchase amount. If you have entered all your purchases, enter '0': "))
    if purchase == 0:
        break
    category = input("What category is this for? ")
    if category == 'Food':
        spending_food += purchase
    elif category == 'Entertainment':
        spending_entertainment += purchase
    elif category == 'Transportation':
        spending_transportation += purchase
    else:
        print("No such category exists. Please try again.")

total = spending_transportation + spending_entertainment + spending_food

print(f"Total spending: {total}")
print(f"Food spending: {spending_food}")
if budget_food < spending_food:
    print(f"Food spending was over budget by {spending_food - budget_food}")
else:
    print(f"Food spending was under budget by {budget_food - spending_food}")
print(f"Entertainment spending: {spending_entertainment}")
if budget_entertainment < spending_entertainment:
    print(f"Food spending was over budget by {spending_entertainment - budget_entertainment}")
else:
    print(f"Food spending was under budget by {budget_entertainment - spending_entertainment}")
print(f"Transportation spending: {spending_transportation}")
if budget_transportation < spending_transportation:
    print(f"Food spending was over budget by {spending_transportation - budget_transportation}")
else:
    print(f"Food spending was under budget by {budget_transportation - spending_transportation}")

