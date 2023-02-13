class RentalProperty:
    def __init__(self, cost, rental_income, expenses):
        self.cost = cost
        self.rental_income = rental_income
        self.expenses = expenses
    def house_cost(self,cost):
        self.cost = cost
        cost = int(input('how much is the cost of the rental proprety? '))
    def income(self, rental_income):
        self.rental_income = rental_income
        rental_income =  int(input('how much is rental income? '))
    def m_expenses(self, expenses):
         self.expenses = expenses
         expenses = int(input('how much is your expense? '))
    def calculate_roi(self):
        return (self.rental_income - self.expenses) / self.cost