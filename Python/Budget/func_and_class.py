def NavigationFunction():
    entertainment = Budget("entertainment", 0)
    groceries = Budget("groceries", 0)
    housing = Budget("housing", 0)
    travel = Budget("travel", 0)

    while True:
        navigation = int(input(f"What would you like to do?"
                               f"\n1. Show budgets"
                               f"\n2. Set your budgets"
                               f"\n3. Increase your budgets"
                               f"\n4. Decrease your budget"
                               f"\n5. Transfer your budget to another category"
                               f"\n0. Exit"
                               f"\n:"))

        if navigation == 1:
            print(f"{entertainment.category} budget is £{entertainment.budget}")
            print(f"{groceries.category} budget is £{groceries.budget}")
            print(f"{housing.category} budget is £{housing.budget}")
            print(f"{travel.category} budget is £{travel.budget}")

        elif navigation == 2:
            entertainment.SetBudget(int(input("What budget would you like for your entertainment needs?")))
            groceries.SetBudget(int(input("What budget would you like for your grocery needs?")))
            housing.SetBudget(int(input("What budget would you like for your housing needs?")))
            travel.SetBudget(int(input("What budget would you like for your travel needs?")))

        elif navigation == 3:

            entertainment.IncreaseBudget(int(input("Increase you entertainment budget by: £ ")))
            groceries.IncreaseBudget(int(input("Increase you grocery budget by: £ ")))
            housing.IncreaseBudget(int(input("Increase you housing budget by: £ ")))
            travel.IncreaseBudget(int(input("Increase you travel budget by: £ ")))

        elif navigation == 4:
            entertainment.DecreaseBudget(int(input("Decrease you entertainment budget by: £ ")))
            groceries.DecreaseBudget(int(input("Decrease you grocery budget by: £ ")))
            housing.DecreaseBudget(int(input("Decrease you housing budget by: £ ")))
            travel.DecreaseBudget(int(input("Decrease you travel budget by: £ ")))


        elif navigation == 5:

            withdraw_from = input("Which category would you like to withdraw from?: ")
            deposit_to = input("Which category would you like to deposit to?: ")
            transfer_amount = int(input("How much would you like to transfer? : £ "))

            # Find the respective budget objects based on user inputs
            withdraw_category = None
            deposit_category = None
            if withdraw_from == "entertainment":
                withdraw_category = entertainment
            elif withdraw_from == "groceries":
                withdraw_category = groceries
            elif withdraw_from == "housing":
                withdraw_category = housing
            elif withdraw_from == "travel":
                withdraw_category = travel
            if deposit_to == "entertainment":
                deposit_category = entertainment
            elif deposit_to == "groceries":
                deposit_category = groceries
            elif deposit_to == "housing":
                deposit_category = housing
            elif deposit_to == "travel":
                deposit_category = travel
            if withdraw_category and deposit_category:
                withdraw_category.TransferBudget(deposit_category, transfer_amount)
            else:
                print("Invalid category names. Please try again.")

        elif navigation == 0:

            break


class Budget:

    def __init__(self, category, budget=0):
        self.category = category
        self.budget = budget

    def SetBudget(self, amount):
        self.budget = amount
        print(f"You have set your budget for {self.category} at £{self.budget}")
        return self.budget

    def IncreaseBudget(self, amount):
        self.budget += amount
        print(f"You have set your budget for {self.category} at £{self.budget}")
        return self.budget

    def DecreaseBudget(self, amount):
        self.budget -= amount
        print(f"You have set your budget for {self.category} at £{self.budget}")
        return self.budget

    def TransferBudget(self, select_category, amount):
        if amount < self.budget:
            self.DecreaseBudget(amount)
            select_category.IncreaseBudget(amount)
            return self.budget
