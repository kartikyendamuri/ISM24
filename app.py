# Welcome message to confirm Python is running
print("Welcome to my simple calculator!")

# Ask user for number
number = input("Enter a number: ")

try:
    # convert to float and perform a calculation
    value = float(number)

    # Basic calculation (example: multiply by 5)
    result = value*5

    # Display result
    print(f"Your number multiplied by 5 is: {result}")

except ValueError:
    # Error message if the input can't be converted
    print("Please enter a valid number next time.")
