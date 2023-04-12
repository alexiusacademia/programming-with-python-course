# Chapter 4: Functions and Modules

In this chapter, we will cover functions and modules, which allow you to write reusable code and organize your program into smaller, more manageable pieces.

## 4.1 Functions

Functions allow you to encapsulate a block of code into a single unit that can be called from anywhere in your program. Here's the basic syntax for defining a function:

```py
def function_name(arguments):
    # code to be executed
    return value
```

For example, let's say we want to write a program that calculates the area of a circle. We can encapsulate the formula for calculating the area into a function:

```py
import math

def area_of_circle(radius):
    area = math.pi * radius ** 2
    return area
```

In this example, we use the math module to access the value of pi, and then define a function that takes a radius as an argument, calculates the area of the circle using the formula pi * r^2, and returns the result.

To call the function, we simply pass a value for the radius:

```py
radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
print("The area of the circle is", area)
```

### Mini-project 1: 

Write a program that takes two numbers as input and calculates their average using a function.

### Mini-project 2: 

Write a program that takes a list of numbers as input and calculates their sum using a function.

## 4.2 Modules

Modules allow you to organize your code into separate files that can be imported and used in other programs. Here's an example:

```py
# file: my_module.py

def greeting(name):
    print("Hello,", name)
```

In this example, we define a simple function that takes a name as an argument and prints out a greeting. To use this function in another program, we can import the module like this:

```py
import my_module

my_module.greeting("Alice")
```

This will print out `"Hello, Alice"`.

### Mini-project 3: 

Write a program that prompts the user to enter a number and checks if it's a prime number using a function defined in a separate module.

## 4.3 Function Arguments

Functions can take one or more arguments, which are values that are passed to the function when it's called. There are two types of arguments: positional arguments and keyword arguments.

### 4.3.1 Positional Arguments

Positional arguments are arguments that are passed to the function based on their position in the argument list. Here's an example:

```py
def greet(first_name, last_name):
    print("Hello,", first_name, last_name)
```

In this example, we define a function that takes two positional arguments: first_name and last_name. To call this function, we simply pass values for these arguments in the correct order:

```py
greet("Alice", "Smith")
```

This will print out `"Hello, Alice Smith"`.

### 4.3.2 Keyword Arguments

Keyword arguments are arguments that are passed to the function using their names. Here's an example:

```py
def greet(first_name, last_name):
    print("Hello,", first_name, last_name)
```

In this example, we define a function that takes two keyword arguments: first_name and last_name. To call this function, we pass values for these arguments using their names:

```py
greet(last_name="Smith", first_name="Alice")
```

This will print out `"Hello, Alice Smith"`.

### Mini-project 1: 

Write a program that takes a name as input and greets the person using a function that has a default value for the last name argument.

### Mini-project 2: 

Write a program that takes a list of names as input and calculates the length of each name using a function that takes a variable number of arguments.

## 4.4 Function Return Values

Functions can also return one or more values, which are values that are sent back to the caller when the function is finished executing. Here's an example:

```py
def add_numbers(num1, num2):
    result = num1 + num2
    return result
```

In this example, we define a function that takes two numbers as arguments, adds them together, and returns the result. To use this function, we can assign the return value to a variable:

```py
sum = add_numbers(3, 5)
print(sum)
```

This will print out `"8"`.

### Mini-project 3: 

Write a program that takes a list of numbers as input and returns a new list containing only the even numbers using a function that uses a list comprehension.

Congratulations, you have completed the Functions and Modules chapter! With these skills, you can now write reusable code and organize your program into smaller, more manageable pieces.