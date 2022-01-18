from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

num1 = int(input("What is the first number?: "))
for symbols in operations:
  print(symbols)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What is the second number?: "))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
# if operation_symbol == "+":
#   return add
# elif operation_symbol == "-":
#   return subtract
# elif operation_symbol == "*":
#   return multiply
# elif operation_symbol == "/":
#   return divide

print(f"{num1} {operation_symbol} {num2} = {answer}") 