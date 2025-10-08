import logging
import csv
import time 

def wait():
    input("\nPress Enter to continue...\n")

#! Section 1: Custom Classes and Inheritance
print("=== Classes and Inheritance ===")

class Dog:
    count = 0  # This is a class variable shared across all Dog objects

    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age
        Dog.count += 1        # Add to the class-level counter

    def call_dog(self):
        print(f"Come here, {self.name}!")

    def speak(self):
        print("bark bark bark")

    @classmethod
    def get_dog_count(cls):
        return cls.count

d1 = Dog("Rex", 3)
d1.call_dog()
d1.speak()
print("Total dogs created:", Dog.get_dog_count())
wait()
d2 = Dog("Barkie", 4)
print("Total dogs created:", Dog.get_dog_count())
print("Access count in instance, falls back to class:", d2.count)
wait()

class BigDog(Dog):
    def __init__(self, name, age): 
        super().__init__(name, age)

    def fetch(self):
        print("Got it.")

    def speak(self):
        print("Woof Woof Woof")

    def speak_verbose(self):
        super().speak()
        self.speak()

dog3 = BigDog("Butch", 3)
dog3.call_dog()
dog3.speak()
dog3.speak_verbose()
wait()

#! Section 2: Decorators
print("=== Decorators ===")

# Logger decorator for writing info to a file
logger = logging.getLogger("lesson3_logger")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f"function: {func.__name__}, args: {args}, kwargs: {kwargs}, return: {result}")
        return result
    return wrapper

@logger_decorator
def greet(name):
    return f"Hello, {name}!"

print(greet("Amanda"))
wait()

# Timer decorator from lesson to measure run time
def timer(func):
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def wait_half_second():
    time.sleep(0.5)
    return "Done"

print(wait_half_second())
wait()

#! Section 3: Decorator with Arguments
print("=== Decorator with Arguments ===")

def type_converter(output_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return output_type(func(*args, **kwargs))
        return wrapper
    return decorator

@type_converter(str)
def get_number():
    return 5

print("Converted to str:", type(get_number()).__name__)
wait()

#! Section 4: List Comprehensions
print("=== List Comprehensions ===")
nums = list(range(10))
even_squares = [x**2 for x in nums if x % 2 == 0]
print("Even squares:", even_squares)
wait()

#! Section 5: List Comprehension with CSV
print("=== List Comprehension and CSV ===")

with open("../csv/employees.csv", newline="") as file:
    rows = list(csv.reader(file))
    names = [f"{row[0]} {row[1]}" for row in rows[1:]]
    print("All Names:", names)

    names_with_e = [name for name in names if 'e' in name]
    print("Names with 'e':", names_with_e)
wait()

#! Section 6: Closures
print("=== Closures ===")

def make_secret(secret):
    attempts = 0
    def guess(word):
        nonlocal attempts
        if word == secret:
            print("Correct!")
            return True
        else:
            attempts += 1
            print(f"Wrong. Attempts: {attempts}")
            return False
    return guess

game = make_secret("python")
game("java")
game("python")
wait()
