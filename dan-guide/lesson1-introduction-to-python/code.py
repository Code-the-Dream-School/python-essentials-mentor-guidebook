#run 
# python --version
# pip --version
#! Students run
# pip install virtualenv (or perhaps pip3 install virtualenv).
# Windows:
# python -m venv .venv
# source .venv/Scripts/activate
# code .

#* Interpreter setup.
# ctrl + shift + p

def wait():
    input("\nPress Enter to continue...\n")

#! Section 1: Variables
print("Variables in Python")
name = "Jazmine" # A variable storing a string
age = 28 # A variable storing an integer
height = 5.8 # A variable storing a float (decimal)
print("Name:", name)
print("Age:", age)
print("Height:", height)
wait()

#! Section 2: Data Types
print("Data Types")
is_student = True
balance = 1000.75
first_name = "Charlie"
number_of_days = 7
print("is_student:", is_student, type(is_student))
print("balance:", balance, type(balance))
print("first_name:", first_name, type(first_name))
print("number_of_days:", number_of_days, type(number_of_days))
wait()

#! Section 3: Type Conversion
print("Type Conversion")
num_str = "42"
num_int = int(num_str)
num_float = float(num_int)
num_str_again = str(num_int)
is_empty = not bool("")
is_non_zero = bool(5)

#* String literals: 
print(f"Converted {num_str} (type: {type(num_str)}) to {num_int} (type: {type(num_int)})")
print(f"Converted {num_int} (type: {type(num_int)}) to {num_float} (type: {type(num_float)})")
print(f"Converted {num_int} back to {num_str_again} (type: {type(num_str_again)})")
print(f"Is empty string falsey? {is_empty}")
print(f"Is 5 truthy? {is_non_zero}")
wait()

#! Section 4: Implicit vs Explicit Conversion
print("Implicit vs. Explicit Conversion")
result_implicit = 3 + 2.5
result_explicit = int(2.8) + 3 #* truncates the decimal(which causes rounding down)
print("Implicit result (3 + 2.5):", result_implicit)
print("Explicit result (int(2.8) + 3):", result_explicit)
wait()

#! Section 5: Operators
print("Operators")

# Arithmetic
print("Addition: 3 + 2 =", 3 + 2, ", type:", type(3 + 2))
print("Subtraction: 5 - 3 =", 5 - 3, ", type:", type(5 - 3))
print("Multiplication: 4 * 2 =", 4 * 2, ", type:", type(4 * 2))
print("Division: 9 / 3 =", 9 / 3, ", type:", type(9 / 3))  # float result
print("Integer Division: 9 // 3 =", 9 // 3, ", type:", type(9 // 3))  # truncates to int
print("Integer Division: 10 // 3 =", 10 // 3, ", type:", type(10 // 3))
print("Modulus: 9 % 4 =", 9 % 4, ", type:", type(9 % 4))  # remainder
print("Modulus: 11 % 4 =", 11 % 4, ", type:", type(11 % 4))
print("Exponentiation: 2 ** 3 =", 2 ** 3, ", type:", type(2 ** 3))
wait()

# Comparison
print("Comparison Operators")
print("Equal: 5 == 5:", 5 == 5, ", type:", type(5 == 5))
print("Not Equal: 5 != 4:", 5 != 4, ", type:", type(5 != 4))
print("Less Than: 3 < 4:", 3 < 4, ", type:", type(3 < 4))
print("Greater Than: 10 > 5:", 10 > 5, ", type:", type(10 > 5))
print("Less Than or Equal: 5 <= 5:", 5 <= 5, ", type:", type(5 <= 5))
print("Greater Than or Equal: 7 >= 3:", 7 >= 3, ", type:", type(7 >= 3))
wait()

# Logical
print("Logical Operators")
print("and: True and False =", True and False, ", type:", type(True and False))
print("or: True or False =", True or False, ", type:", type(True or False))
print("not: not True =", not True, ", type:", type(not True))
wait()

#! Section 6: Indentation
print("Indentation Example")
def check_number(num):
    if num > 0:
        print("Positive number")
    elif num < 0:
        print("Negative number")
    else:
        print("Zero")
check_number(0)
wait()

print("Incorrect indentation (this will raise an error):")
bad_code = '''
def check_number(num):if num > 0:
    print("Positive number")
'''

try:
    exec(bad_code)
except SyntaxError as e:
    print("Caught SyntaxError:", e)
wait()

#! Section 7: Control Flow - Conditionals
print("Control Flow - Conditionals")
age = 16
if age >= 18:
    print("You're an adult!")
elif age >= 13:
    print("You're a teenager.")
else:
    print("You're a child.")
wait()

#! Section 7: Control Flow - Loops
print("Control Flow - Loops")
for i in range(3):
    print("Loop iteration:", i)
wait()

count = 0
while count < 3:
    print("Count is:", count)
    count += 1
wait()

#! Break and Continue
print("Using break in loop:")
for num in range(10):
    if num == 5:
        break
    print(num)
wait()

print("Using continue in loop:")
for num in range(5):
    if num == 2:
        continue
    print(num)
wait()

#! Section 8: Functions
print("Functions")
def greet(name="stranger"):
    print("Hello,", name + "!")
greet()
greet("Luis")
wait()

def add(a, b):
    print("Sum:", a + b)
add(3, 5)
add("Hello ", "World!")
wait()

def square(number):
    return number * number
print("Square of 4:", square(4))
wait()

def add_numbers(*args): #* args lets you pass in any number of arguments as a tuple
    print("Sum with *args:", sum(args))
add_numbers(1, 2, 3, 4)
add_numbers(1,7) 
wait()

def print_info(**kwargs): #* keyword arguments, any number like args but a key=value pair
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Janet", role="Developer", age=25)
print_info(name="Bob", favorite_color="Blue", likes="[dogs, cats]")
wait()

# Scope
name = "Hima"
def set_name():
    name = "James"
set_name()
print("Name:", name)
wait()
def set_name_global():
    global name
    name = "James"  

set_name_global()
print("Name:", name) 
wait()

#! Section 9: Debugging
print("Debugging with print")
def multiply(a, b):
    result = a * b
    print("Result is:", result)
    return result
multiply(3, 5)
wait()

#! Section 10: Logging
import logging
logging.basicConfig(level=logging.DEBUG)
print("Logging Levels Example:")

def log_multiply(a, b):
    if a is None or b is None:
        logging.critical("CRITICAL: One of the inputs is None")
        return None
    
    if b == 0:
        logging.error("ERROR: Cannot multiply by zero")
        return 0

    logging.debug(f"DEBUG: Starting multiplication of {a} and {b}")
    result = a * b
    logging.info(f"INFO: Result is {result}")

    if result > 20:
        logging.warning("WARNING: Result is unusually large")

    return result

log_multiply(3, 5)
log_multiply(10, 3)
log_multiply(0, 5)
log_multiply(None, 5)
wait()

#! Section 11: Error Handling
print("Error Handling")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
wait()

try:
    num = int("abc")
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Success: {num}")
finally:
    print("Try block finished.")
wait()

def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older.")
try:
    check_age(16)
except ValueError as e:
    print(e)
wait()

#! Section 12: String Operations
print("String Operations")
name = "Ed"
count = 6
kind_of_object = "apples"
print(f"{name} has {count} {kind_of_object}.")
cost = 22 / 7
print(f"The pie cost ${cost:.2f}.")