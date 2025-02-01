def input_validator(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Error: Value must be greater than 0. Please try again.")
            else:
                return value
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


def simple_interest():
    principal = input_validator("Enter the principal amount: ")
    rate = input_validator("Enter the rate (in percentage): ") / 100
    time = input_validator("Enter the time (in years): ")

    answer = principal * rate * time
    print(f"The Simple Interest on {principal} for {time} year(s) is {answer:.2f}")


def compound_interest():
    principal = input_validator("Enter the principal amount: ")
    rate = input_validator("Enter the rate (in percentage): ") / 100
    time = input_validator("Enter the time (in years): ")

    while True:
        try:
            number = int(input("Enter the number of times interest is compounded per year: "))
            if number <= 0:
                print("Error: Value must be greater than 0. Please try again.")
            else:
                break
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

    amount = principal * (1 + rate / number) ** (number * time)
    interest = amount - principal

    print(f"The Compound Interest on {principal} for {time} year(s) is {interest:.2f}")
    print(f"The total amount after {time} year(s) is {amount:.2f}")


def interest():
    while True:
        try:
            print("\nWelcome to the Interest Calculator.")
            option = int(input("Choose an option: \n1. Simple Interest Calculator \n2. Compound Interest Calculator\n3. Exit \n"))

            if option == 1:
                simple_interest()
            elif option == 2:
                compound_interest()
            elif option == 3:
                print("The calculation operation has been terminated.")
                break
            else:
                print("Invalid input. Choose between 1, 2, and 3.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")


if __name__ == "__main__":
    interest()
