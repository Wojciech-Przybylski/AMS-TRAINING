def NavigationFunction():
    while True:
        navigation = int(input(f"What would you like to do?"
                               f"\n1. Show budgets"
                               f"\n2. Set your budgets"
                               f"\n3. Increase your budgets"
                               f"\n4. Decrease your budget"
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

            entertainment.SetBudget(int(input("Increase you entertainment budget by: £ ")))
            groceries.SetBudget(int(input("Increase you grocery budget by: £ ")))
            housing.SetBudget(int(input("Increase you housing budget by: £ ")))
            travel.SetBudget(int(input("Increase you travel budget by: £ ")))

        elif navigation == 4:
            entertainment.DecreaseBudget(int(input("Decrease you entertainment budget by: £ ")))
            groceries.DecreaseBudget(int(input("Decrease you grocery budget by: £ ")))
            housing.DecreaseBudget(int(input("Decrease you housing budget by: £ ")))
            travel.DecreaseBudget(int(input("Decrease you travel budget by: £ ")))

        elif navigation == 0:
            break


class Budget:

    def __init__(self, category, budget=0):
        self.category = category
        self.budget = budget

    def SetBudget(self, amount):
        self.budget += amount
        print(f"You have set your budget for {self.category} at £{self.budget}")

    def DecreaseBudget(self, amount):
        self.budget -= amount
        print(f"You have set your budget for {self.category} at £{self.budget}")

