from calculator import add, subtract, multiply, divide

print("===== PYTHON CALCULATOR =====")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))

try:
    print("Division:", divide(a, b))
except ValueError as error:
    print(error)