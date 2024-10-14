def sum(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Invalid function!"

def to_the_power(x, y):
    return x ** y

while True:
    print("\n1. Sum\n2. Subtraction\n3. Multiplication\n4. Division\n5. To The Power\n6. Exit")
    choice = input("Choose an operation: ")

    if choice in ("1", "2", "3", "4", "5"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if choice == "1":
            print(f"result: {sum(num1, num2)}")

        elif choice == "2":
            print(f"result: {subtraction(num1, num2)}")

        elif choice == "3":
            print(f"result: {multiplication(num1, num2)}")

        elif choice == "4":
            print(f"result: {division(num1, num2)}")

        elif choice == "5":
            print(f"result: {to_the_power(num1, num2)}")

    elif choice == "6":
        break
    else:
        print("Invalid Input!")
