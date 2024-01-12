import dbConnect as db
import datetime

class Teen:
    def __init__(self, name, email, username, password):
        self.name = name
        #self.doB = datetime.date(doB)
        self.email = email
        self.username = username
        self.password = password
        print("-------")
        print(self.name, self.email,"inside db")
        print("print value",self.username, self.password, self.email, self.name)

    '''def ageCalculator(self, doB):
        today = datetime.date.today()
        age = today.year - doB.year
        return age'''

    def display(self):
        print(self.name)
        #print(self.doB)
        print(self.email)
        print(self.username)
        print(self.password)

class Data: 
  def __init__(self, monthly_budget, monthly_earning, item_name, item_value, classify):
    self.monthly_budget = monthly_budget
    self.monthly_earning = monthly_earning
    self.item_name = item_name
    self.item_value = item_value
    self.classify = classify
  def display(self):
    print(self.monthly_budget, self.monthly_earning,
    self.item_name, self.item_value,
    self.classify)


#T1 = Teen("Shraddha", 4, 10, 1981, "bhnagale@gmail.com", "sharddha",
#          "Bhangale23")
#db.log(T1)
#T2 = Teen("Pooja", 25, 11, 2005, "abc@abc.co.in", "pabc", "1234def")
#db.log(T2)
#print(db.view(T1))

'''class Expence:
  def __init__(self,category, amount, discription, expDate):
    self.category = category
    self.amount = amount
    self.description = description
    self.expDate = expDate'''

