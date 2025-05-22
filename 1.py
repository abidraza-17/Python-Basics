# print("Hello,Abid! Welcome to Data Science")
# Tasks:
#1 print Name and Age

print("My name is: Abid")
print("My age is: 21")

#2 Function to check given number is even or odd

def check_even(num):
    if num % 2==0:
        return "even"
    else:
        return "odd"
num=int(input())
print(check_even(num))

#3 A list of 5 fruits – print each using a loop

fruits=["apple","banana","papaya","grapes","jackfruit"]
for i in fruits:
    print(i)

#4 A dictionary with your info: name, branch, year, interests

About ={"name":"Abid","Branch":"CSE","Intersets":"playing"}
print(About)

#5 A simple calculator with add/sub/mul/div options
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def calculator():
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
            print(x+y)

        elif choice == '2':
            print(x-y)

        elif choice == '3':
            print(x*y)

        elif choice == '4':
            print(x/y)

    else:
        print("Invalid Input")

if __name__ == "__main__":
    calculator()

