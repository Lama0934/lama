#######_Question 1
#######_A:

L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]

d = dict(zip(L1, L2))
print(d)

#######_B:

def calculate_factorial(num):
    if num == 0:
        return 1
    else:
        return num * calculate_factorial(num - 1)

num = int(input("Enter a number to calculate its factorial: "))
factorial = calculate_factorial(num)
print(f"The factorial of {num} is {factorial}")

######_C:

L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']

for item in L:
    if item.startswith('B'):
        print(item)

#####_D:

d = {x: x+1 for x in range(11)}
print(d)

######_Question 2

def binary_to_decimal(binary):
    decimal = 0
    power = 0
    
    for digit in binary[::-1]:
        if digit == '1':
            decimal += 2 ** power
        elif digit != '0':
            return None
        power += 1
    
    return decimal

while True:
    binary_number = input("الرجاء إدخال رقم ثنائي: ")

    if not all(char in '01' for char in binary_number):
        print("رقم ثنائي غير صالح. يرجى إدخال رقم ثنائي يتكون من 0 و 1 فقط.")
    else:
        decimal_number = binary_to_decimal(binary_number)
        
        if decimal_number is not None:
            print(f"الرقم العشري المكافئ لـ {binary_number} هو: {decimal_number}")
            break
        else:
            print("رقم ثنائي غير صالح. يرجى إدخال رقم ثنائي صحيح.")

#####_Question 3

import json

with open('lama.json', 'r',encoding='utf-8') as f:
    question_with_user = json.load(f)

score = 0

for question, answer in question_with_user.items():
    user_answer = input(question + " ")
    if user_answer.lower() == answer.lower():
        score += 1

print("You answered", score, "Questions correctly")


user_name = input("Enter your name: ")
results_with_user = {user_name: score}
with open('results_user.json', 'w') as f:
    json.dump(results_with_user, f)

#########_Question 4

class BankAccount:
    def _init_(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def _init_(self, account_number, account_holder, interest_rate):
        super()._init_(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount
        print(f"Applied interest at rate {self.interest_rate}%. New balance: ${self.balance}")

    def print(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ${self.balance}")
        print(f"Interest Rate: {self.interest_rate}%")

# Create an instance of SavingsAccount
savings_account = SavingsAccount("987654321", "lama", 2.5)

# Perform a deposit of $2000
savings_account.deposit(2000)

# Apply interest to the balance based on the interest rate
savings_account.apply_interest()

# Print the current balance and rate
savings_account.print()