from datetime import datetime
from enum import Enum
from typing import List, Optional, Dict

class Category(Enum):
    GROCERIES="Groceries"
    TRANSPORTATION="Transportation"
    # HOUSING="Housing"
    # UTILITIES="Utilities"
    # ENTERTAINMENT="ENTERTAINMENT"
    # SHOPPING="Shopping"
    # DEBT="Debt"
    # MISCELLANEOUS="Miscellaneous"
    # OUTSIDE_FOOD="Outside Food"
    # SAVING="Savings"
    # INSURANCE="Insurance"
    

class Expense:
    def __init__(self, date: str, amount: float, category: Category):
        self.date=date
        self.amount=amount
        self.category=category
 
class Income: #income object, that will contain the amount, time, and the source of the income for the user
    def __init__(self, date: str, amount: float, source: str):
        self.date=date
        self.amount=amount
        self.source=source

#Monthly data for month to month expenses for the user
class MonthlyData:
    def __init__(self, year: int, month: int):
        self.year=year
        self.month=month
        self.expenses: List[Expense]=[]
        self.incomes: List[Income]=[]
        self.budget: Dict[Category, Optional[float]]={category: None for category in Category} #setting each category amount to 0

#user class 
class User:
    def __init__(self, username: str):
        self.username=username
        self.monthly_data: Dict[str, MonthlyData]={} #YYYY-MM
    
    #function to create the monthly data object
    def get_create_monthly_data(self, year: int, month: int)->MonthlyData:
        key=f"{year}-{int(month):02d}" #creating a key in format of YYYY-MM
        if key not in self.monthly_data: #if it does not already exist in the dictionary
            self.monthly_data[key]=MonthlyData(year, month) #init month with key and MonthlyData as the value which has lists
        return self.monthly_data[key]
    
