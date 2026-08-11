# Introduction to Python: error handling with try/except

print("Safe division calculator")
print("-" * 28)

try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
except ValueError:
    # Runs when the input cannot be converted to a number
    print("Error: please enter valid numbers.")
except ZeroDivisionError:
    # Runs when the denominator is 0
    print("Error: cannot divide by zero.")
else:
    # Runs only if no exception was raised
    print(f"Result: {result}")
finally:
    # Always runs, whether an error occurred or not
    print("Done. Thanks for trying the calculator!")
