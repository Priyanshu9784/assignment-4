  # 1 print all prime numbers in a list
  
  
numbers = [2, 4, 5, 7, 8, 11, 15, 17, 19]
print("Prime numbers in the list are:")
for num in numbers:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
         print(num)

         
# 2   multiplication table in matrix format

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()
    
    
# 3   function to count even numbers and sum odd numbers


def analyze_numbers(lst):
    even_count = 0
    odd_sum = 0
    for num in lst:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_sum += num
    return even_count, odd_sum
numbers = [1, 2, 3, 4, 5, 6]
count, total = analyze_numbers(numbers)
print("Count of Even Numbers:", count)
print("Sum of Odd Numbers:", total)\
    
    
#  4  simple interest using default arguments


def simple_interest(principal, rate=5, time=2):
    si = (principal * rate * time) / 100
    return si
print("SI =", simple_interest(10000))
print("SI =", simple_interest(principal=10000, rate=8, time=3))



#  5,6   Student Class and Grade Calculatioclass Student:


def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        def calculate_grade(self):
            if self.marks >= 90:
                return "A"
            elif self.marks >= 75:
                return "B"
            elif self.marks >= 60:
                return "C"
            else:
                return "D"
            s1 = Student("Aman", 92)
            s2 = Student("Rahul", 78)
            print(s1.name, "Grade:", s1.calculate_grade())
            print(s2.name, "Grade:", s2.calculate_grade())

# 7  BankAccount Class with Private Balanceclass BankAccount:


class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
        print("Deposited:", amount)
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawn:", amount)
        else:            print("Insufficient Balance")
    def show_balance(self):
        print("Current Balance:", self.__balance)
acc = BankAccount(5000)
acc.deposit(1000)
acc.withdraw(2000)
acc.show_balance()


# 8 Division with Exception Handling


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numbers only.")
    


# 9  Create a File, Write Student Data, Read and Display



file = open("student.txt", "w")
name = input("Enter student name: ")
marks = input("Enter marks: ")
file.write("Name: " + name + "\n")
file.write("Marks: " + marks)
file.close()
file = open("student.txt", "r")
print("\nFile Content:")
print(file.read())
file.close()

#10  read Numbers from a File and Calculate Total & Averag


try:
    file = open("numbers.txt", "r")
    total = 0
    count = 0
    for line in file:
        total += int(line.strip())
        count += 1
    average = total / count
    print("Total =", total)
    print("Average =", average)
    file.close()
except FileNotFoundError:
    print("Error: File does not exist.")