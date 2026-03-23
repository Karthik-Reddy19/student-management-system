class Bank:
    def __init__(self,name,accno,balance):
        self.name=name
        self.accno=accno
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        
    def withdraw(self,amount):
        if amount > self.balance:
           print("Insufficient balance")
        else:
           self.balance -= amount
    def display(self):
        print("Name of acc_holder:",self.name)
        print("Account Number:",self.accno)
        print("Balance:",self.balance)
    def check_bal(self):
        print(f"Balance is {self.balance}")
def acc_no():
    import random
    return str(random.randint(10000,99999))
def create_acc():
    name=input("Enter the name of account holder:")
    num=acc_no()
    balance=int(input("Enter the amount:"))
    with open("bank.txt","a") as f:
        f.write(f"{name},{num},{balance}\n")
def read_data():
    data = []
    try:
        with open("bank.txt", "r") as f:
            for line in f:
                name, accno, balance = line.strip().split(',')
                data.append([name, accno, int(balance)])
    except FileNotFoundError:
        pass
    return data
def write_data(data):
    with open("bank.txt", "w") as f:
        for record in data:
            f.write(f"{record[0]},{record[1]},{record[2]}\n")
def search():
    sn=input("Enter the acc_no:")
    data=read_data()
    for record in data:
        if record[1]==sn:
            print("Record found")
            print("Name:",record[0])
            print("Account_no:",record[1])
            print("Balance:",record[2])
            return
    print("Record not found")
def deposit():
    sn=input("ENter the account number:")
    amount=int(input("ENter the amount"))
    data=read_data()
    for record in data:
        if record[1]==sn:
            record[2]+=amount
            write_data(data)
            print("Amount deposited")
            return
    print("Account not found")
def withdraw():
    sn=input("ENter the account no:")
    amount=int(input("Enter the amount:"))
    data=read_data()
    for record in data:
        if record[1]==sn:
            if amount>record[2]:
                print("Insufficient balance")
            else:
                record[2]-=amount
                write_data(data)
                print("Withdrawal successsful")
                return
    print("Account not found")
def delete_acc():
    dn=input("Enter the acc_no:")
    data=read_data()
    new_data=[]
    found=False
    for record in data:
        if record[1]!=dn:
            new_data.append(record)
        else:
            found=True
    write_data(new_data)
    if found:
        print("Account deleted")
    else:
        print("Account not found")
    

while True:
    print("MENU")
    print("\n1.Create Account\n2.Search Account\n3.Deposit\n4.Withdraw\n5.Delete Account\n6.Exit")
    choice=int(input("Enter your choice:"))
    if choice == 1:
        create_acc()
    elif choice == 2:
        search()
    elif choice == 3:
        deposit()
    elif choice == 4:
        withdraw()
    elif choice == 5:
        delete_acc()
    elif choice == 6:
        break
    else:
        print(" Invalid choice")