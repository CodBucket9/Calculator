#Created by Charlie Perry
#You may use this for your projects.

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def calculator():
    print("Enhanced Calculator")
    print("Available operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        try:
            choice = int(input("Enter the operation number (1/2/3/4) or 0 to exit: "))
            
            if choice == 0:
                print("Exiting the calculator.")
                break
            
            if choice not in [1, 2, 3, 4]:
                print("Invalid choice! Please try again.")
                continue

            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == 1:
                print("Result:", add(num1, num2))
            elif choice == 2:
                print("Result:", subtract(num1, num2))
            elif choice == 3:
                print("Result:", multiply(num1, num2))
            elif choice == 4:
                print("Result:", divide(num1, num2))
        except ValueError:
            print("Invalid input! Please enter a number.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    calculator()
