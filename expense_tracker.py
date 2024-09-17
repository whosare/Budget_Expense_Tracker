from src.models import Expense, User, Income, MonthlyData, Category
from typing import DefaultDict
from datetime import datetime

class ExpenseTracker:
    def __init__(self, user: User):
        self.user=user
    
    def add_expense(self, user: User, date_str: str, amount: float, category: Category):
        [year, month]= date_str.split("-")
        monthly_data=user.get_create_monthly_data(year, month)
        expense=Expense(date_str, amount, category)
        monthly_data.expenses.append(expense)
        print("Successfully added expense")

    def add_income(user: User, amount: int, date_str: str):
        #assuming date is in the form YYYY-MM
        [year, month]= date_str.split("-")
        monthly_data=user.get_create_monthly_data(year, month)
        income=Income(date_str, amount)
        monthly_data.incomes.append(income)
        print("Successfully added income")


    #function for setting one of the budgets in the month through category
    def set_budget_by_category(self, year: int, month: int, category: Category, amount: float):
        monthly_data=self.user.get_create_monthly_data(year, month) #obtain monthly data object to interact with budget
        monthly_data.budget[category]=amount#once the month object is found

    #@param: year month and category
    #returns: the expenses for a specific category. 
    def get_expenses_by_category(self, year: int, month: int, category: Category)->float:
        monthly_data_exp=self.user.get_create_monthly_data(year, month) #create or obtain the monthly data object with the date
        total=0 #initialize total variable to be returned
        for expense in monthly_data_exp.expenses:
            if expense.category==category:
                total+=expense.amount
        return total
    
    def get_budget_by_category(self, year: int, month: int, category: Category)-> float:
        monthly_data=self.user.get_create_monthly_data(year, month)
        return monthly_data.budget.get(category, 0.0)

        # if category in monthly_data.budget:
        #     print("\n", category, monthly_data.budget[Category.value], "\n")
        # else:
        #     print("\nNot found. ")
        # return monthly_data.budget.get(category, 0.0) #using get function to return value for category, if not exist: return 0.0

    def set_budgets_from_spending(self, year: int, month: int):
        monthly_data_budget=self.user.get_create_monthly_data(year, month)
        for category in Category:
            monthly_data_budget.budget[category]=self.get_expenses_by_category(year, month, category)
            print("Budget set for:", category)

    def get_total_expenses(self, year: int, month: int):
        total=0
        monthly_data=self.user.get_create_monthly_data(year, month)
        for cat in Category:
            total+=self.get_expenses_by_category(year, month, cat)
        return total    

    def category_switch(cat: str):
        for cate in Category:
            if cat==cate.value:
                return cate
        return  "NA"
    # def get_balance(self):
    #     return self.get_total_income()-self.get_total_expenses()
    #possible over budget function warning user

    #Function that displays important information
    #such as how much spending vs income
    #