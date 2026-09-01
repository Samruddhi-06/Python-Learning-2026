# use of static method

class Math:
    def __init__(self, num):
        self.num = num

    def add_num(self,n):
        self.num = self.num + n

    @staticmethod
    def add(x,y):
        return x+y

m = Math(5)
print(m.num)
m.add_num(6)
print(m.num)
print("Using instance :-",m.add(5,2))
print("Using class name :-",Math.add(5,2))

# class Variable vs instance variable  example

class Company:
    revenue_2026 = "$523000"
    company_name = "Google"
    net_profit = 80326

    def __init__(self, sales, initial_profit):
        self.sales = sales
        self.initial_profit = initial_profit

    def sales_details(self):
        self.sales = self.sales * 0.2
        print(f"The revenue generated for the company {self.company_name} this year is {self.revenue_2026} and their sales this year is ${self.sales}")

    def profit_details(self, added_profit):
        self.profit = self.initial_profit + added_profit + Company.net_profit
        print(f"Total calculated profit of this year for {self.company_name} is ${self.profit}")

c1 = Company(50000, 45932)
print("------------------------------------------")
c1.sales_details()
c1.profit_details(888000)