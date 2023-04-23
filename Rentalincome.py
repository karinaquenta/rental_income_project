class Rental_Roi():
       
    def __init__(self, income=0, expenses=0, down_payment=0):
        self.user_input = None
        self.income = income
        self.expenses = expenses
        self.down_payment = down_payment

    def get_user_input(self):
        print("Welcome to EasyAccessROI! We will ask you a few questions to get your ROI. Easy as that!")
        self.user_input = input("Are you ready to begin? Please press 1 for yes, 2 for Not Right Now:  ")
        if self.user_input == '1':
            self.income = int(input('Please enter your income(monthly): ').replace(",", ""))
            self.expenses = int(input('Now enter your expenses(monthly): ').replace(",", ""))
            self.down_payment = int(input('Estimated down payment: ').replace(",", ""))   
        if self.user_input =='2':
            print("Thank you for considering EasyAccessROI. Please come back when you are ready to begin. ")
            exit()

    def main_roi(self):
        self.get_user_input()
        self.calc_cash_flow_monthly()
        self.calc_cash_flow_yearly()
        return(self.calc_roi())

    def calc_cash_flow_monthly(self):
        self.cash_flow_monthly = self.income - self.expenses

    def calc_cash_flow_yearly (self):
        self.cash_flow_yearly = self.cash_flow_monthly * 12

    def calc_roi(self):
        if self.down_payment == 0:
            return "Error: Down payment cannot be zero. Please re-enter your information."
        else:     
            self.roi = round((self.cash_flow_yearly/self.down_payment)*100, 1)  
            return(f"Cash on cash ROI is {self.roi}% We did the calculations for you! EasyAccessROI is here to make your life easier. Thank you!")

my_rental_roi = Rental_Roi()
print(my_rental_roi.main_roi()) 
print('''
       *
      /\ 
     /  \ 
    /    \ 
   /------\ 
  / |    | \ 
    |    |   
 ___|____|___
''')
#User Input:
#income, expenses
#cash flow for each month x 12 = cash flow for the year
#Down payment/upfront money 
#roi = cash flow for the year/down payment x 100, 1 <-round number
#print(f"cash on cash ROI: {ROI}%")
