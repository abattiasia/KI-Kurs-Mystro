#
class Bank:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        self.balance=0

    def deposit(self,amout):
        self.balance += amout
        print(f"my Balance =  {self.balance}")
        return
    def withdrow(self,amount):

        if amount < self.balance:
            self.balance -= amount
            print(f"my Balance =  {self.balance}")
            return
        return print(f"my Balance is not enough")
    
    def info(self):
        print(f"my Name =  {self.name}")
        print(f"my Age =  {self.age}")
        print(f"my Balance =  {self.balance}")
        return

b1=Bank("Attia", 39)
b1.deposit(500)
b1.withdrow(300)
print(b1.balance)
print(b1.age)
b1.info()