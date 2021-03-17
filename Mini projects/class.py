class Bank():
    def __init__(self,Deposit,Withdraw,Loan):
        self.Deposit=Deposit
      
       #Setting Default value
       self.Savings=0

    def DepCash(self):
        print('\nDeposited Ksh '+str(Customer.Deposit))
    
    def WithCash(self):
        print('Withdrawn Ksh '+str(Customer.Withdraw))
    
    def LoanCash(self):
        print('Loaned Ksh '+str(Customer.Loan))

    def saveCash(self):
        print('Saved Ksh '+str(self.Savings))

   


#Accessing arguments in init method
Customer=Bank(20000,50000,5700)

#Modifying Default value directly
Customer.Savings=4300

#Calling Methods of a class
Customer.DepCash()
Customer.WithCash()
Customer.LoanCash()
Customer.saveCash()



#Inheritance
class Airtime(Bank):
    def __init__(self,Deposit,Withdraw,Loan):
    
        super().__init__(Deposit,Withdraw,Loan)

airtPurchase=Airtime(9000,6,7)
print("Airtime purchase:"+str(airtPurchase.Deposit))