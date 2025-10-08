import os
import csv
import sys
from datetime import datetime

def wait():
    input("\nPress Enter to continue...\n")

#! Section 1: Lists
#* Lists are mutable (changeable) and ordered. Great for dynamic collections.
print("=== Lists ===")
fruits = ['apple', 'banana', 'cherry']
print("Original list:", fruits)
wait()

fruits.append('date')  #* O(1) - Appending is constant time
fruits[0] = 'orange'   #* O(1) - Direct memory index update
print("Updated list:", fruits)
wait()

print("Iterating over list:")
for fruit in fruits:
    print(fruit)
wait()

print("Slicing lists:")
print(fruits)
print("fruits[1:3]:", fruits[1:3])   # ['banana', 'cherry'] #* non inclusive 3 index
print("fruits[2:]:", fruits[2:])     # ['cherry', 'date'] #* inclusive start index
print("fruits[:2]:", fruits[:2])     # ['orange', 'banana']
print("fruits[-2:]:", fruits[-2:])   # ['cherry', 'date']
wait()

#! Section 1.5: Lambdas vs Traditional Functions
#* map() applies a function to each item in a list.
#* lambdas are one-line anonymous functions.
print("=== Lambdas vs Traditional Functions ===")
wait()
list_one = [3, 4, 5]
print("Original list:", list_one)
wait()

def incrementor(x):  #* Traditional named function
    return x + 1

list_two = list(map(incrementor, list_one))  #* Uses named function
list_three = list(map(lambda x: x + 1, list_one))  #* Uses lambda keyword
print("Using function:", list_two)
print("Using lambda:", list_three)
wait()

#! Section 2: Tuples (continued)
#* Tuples are immutable and memory-efficient. Used when data shouldn't change.
#* They're faster and require less memory than lists due to fixed size and no method overhead.
#* "No method overhead" means tuples don’t carry the extra functionality/methods that lists do (like .append(), .pop(), etc.), 
#* which makes them lighter in memory and faster for iteration or fixed data storage.
#* Tuples in math are ordered groups of elements — just like coordinates (x, y, z).
#* Common use cases: coordinates, RGB values, database rows, fixed configs.
#* I use them with grid traversal IE: BFS.

print("=== Tuples ===")
wait()
dimensions = (1920, 1080)
print("Tuple length:", len(dimensions))  #* Can still use len()
wait()

print("Check if 1920 is in dimensions:", 1920 in dimensions)  #* O(n) membership check
wait()

#* Example: 3x3 coordinate grid using tuples
print("3x3 coordinate grid using tuples:")
grid = [(i, j) for i in range(3) for j in range(3)]
for coord in grid:
    print(coord)
wait()

#! Section 3: Dictionaries
#* Dictionaries are fast key-value stores. Keys must be unique. Lookup time is O(1).
#* Backed by a hash table under the hood. Ideal for fast lookups, configs, counting.
print("=== Dictionaries ===")
wait()
person = {"name": "Jazmine", "age": 30}
print("Initial dict:", person)
wait()

person["email"] = "jazmine@example.com"  #* Adding new key-value pair
print("After adding email:", person)
print("Dictionary length:", len(person))
wait()

print("Keys:", list(person.keys()))      #* Get all keys
print("Values:", list(person.values()))  #* Get all values
print("Items:", list(person.items()))    #* Get key-value pairs as tuples
wait()

print("Access value by key:", person["name"])
print("Using .get():", person.get("age", "Not found"))  #* Safer access with default
print("Using .get():", person.get("bicycle", "Not found"))
print("Check if 'email' exists:", "email" in person)    #* O(1) key membership
wait()

del person["age"]              #* O(1) delete by key
print("After deleting age:", person)
print("Dictionary length:", len(person))  #* Number of key-value pairs
wait()

#! Section 4: Sets
#* Sets hold unique values. Fast for membership tests, deduplication, and set math.
#* Underlying structure is a hash table. Average-case O(1) add, delete, lookup.
print("=== Sets ===")
wait()
unique = {1, 2, 2, 3, 4}
print("Initial set (duplicates removed):", unique)
wait()

unique.add(5)
print("After adding 5:", unique)
wait()

print("Union with {4, 6}:", unique.union({4, 6}))             #* All elements from both sets
print("Intersection with {2, 3}:", unique.intersection({2, 3})) #* Elements in both sets
print("Difference from {1, 5}:", unique.difference({1, 5}))     #* Elements only in 'unique'
#* Symmetric difference returns all elements that are in either of the sets, but not in both.
print("Symmetric difference with {2, 6}:", unique.symmetric_difference({2, 6}))  #* XOR logic -> removes anything existing in both
wait()

print("Check if 3 in unique:", 3 in unique)
wait()
unique.discard(100)  #* Safe remove (no error if not found)
print("Set length:", len(unique))
wait()
unique.discard(3)  #* Safe remove (no error if not found)
print("Set length:", len(unique))
wait()

#! Section 5: File Handling – Text Files
#* `with open(...) as f:` ensures files are properly closed.
#* Text files are great for logs, configs, and human-readable data.
print("=== File Handling: Text Files ===")
wait()
try:
    with open("example.txt", "w") as file:
        file.write("Hello\nSecond line")
    print("Wrote to example.txt")
    wait()

    with open("example.txt", "r") as file:
        print("Contents of example.txt:")
        print(file.read())
except Exception as e:
    print("File error:", e)
wait()

#! Section 6: File Handling – CSV Files
#* Use csv.writer() to write rows, csv.reader() to read rows.
#* CSVs are common for spreadsheets, reports, and structured tabular data.
print("=== File Handling: CSV Files ===")
wait()
with open("sample.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Jazmine", 30, "New York"])
print("Wrote sample.csv")
wait()

with open("sample.csv", "r") as file:
    reader = csv.reader(file)
    print("CSV contents:")
    for row in reader:
        print(row)
wait()

#! Section 7: Keyboard Input
#* input() always returns a string. Convert it if you need numbers.
#* Great for interactive programs and CLI tools.
print("=== Keyboard Input ===")
wait()
try:
    name = input("Enter your name: ")
    print(f"Hello, {name}!")
except Exception:
    print("Input error")
wait()

#! Section 8: Simple Calculator
#* Demonstrates input, type conversion, branching, and error handling.
#* Covers common runtime exceptions and branching logic patterns.
print("=== Simple Calculator ===")
try:
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")
    if op == "+":
        print("Result:", n1 + n2)
    elif op == "-":
        print("Result:", n1 - n2)
    elif op == "*":
        print("Result:", n1 * n2)
    elif op == "/":
        print("Result:", n1 / n2)
    else:
        print("Invalid operation")
except ValueError:
    print("Invalid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
wait()

#! Section 9: os Module
#* Lets you interact with the operating system: paths, dirs, env vars.
#* Common for scripting, automation, deployment, and file management.
print("=== os Module ===")
wait()
print("Current directory:", os.getcwd())
print("Files in current dir:", os.listdir())
wait()

os.environ["THISVALUE"] = "ABC"
print("Environment variable THISVALUE:", os.getenv("THISVALUE"))
wait()

#! Section 10: sys.argv
#* sys.argv shows command-line args. Useful for CLI tools.
#* sys.argv[0] is always the script name.
print("=== sys.argv Example ===")
wait()

for i, arg in enumerate(sys.argv):
    print(f"Argument {i}:", arg)
wait()

#* Demonstrating appending a simulated arg
sys.argv.append("demo_arg")  #* This does not simulate real CLI use but shows mutation
print("After appending a simulated argument:")
for i, arg in enumerate(sys.argv):
    print(f"Argument {i}:", arg)
wait()