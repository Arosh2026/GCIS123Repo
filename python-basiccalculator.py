def main():
    while True:
        print("----- BASIC CALCULATOR ------")
        print("1. Addition Operation")
        print("2. Subtraction Operation")
        print("3. Multiplication Operation")
        print("4. Division Operation")

        choice = input("Pick a choice (1-4): ")

        if choice == "1":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Sum =", a+b)

        elif choice == "2":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Difference =", a-b)

        elif choice == "3":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Product =", a*b)

        elif choice == "4":
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            print("Quotient =", a/b)

        else:
            print("Choice unavailable")
            input()

main()