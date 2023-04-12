# Chapter 3: Control Flow Statements

In this chapter, we will cover control flow statements, which allow you to control the execution of your program. Specifically, we will cover if statements, loops, and break and continue statements.

## 3.1 If Statements
If statements allow you to execute a block of code only if a certain condition is true. Here's the basic syntax:

```py
if condition:
    # code to be executed if the condition is true
```

For example, let's say we want to write a program that tells the user if a number is positive, negative, or zero:

```py
num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")
```

In this example, we use the if statement to check if the number is greater than zero. If it is, we print "The number is positive". If it's not, we use the elif statement to check if the number is less than zero. If it is, we print "The number is negative". If neither of these conditions is true, we use the else statement to print "The number is zero".

### Mini-project 1: 

Write a program that prompts the user to enter their age and tells them if they're old enough to vote or not.

### Mini-project 2: 

Write a program that prompts the user to enter a year and tells them if it's a leap year or not.

## 3.2 Loops

Loops allow you to repeat a block of code multiple times. There are two types of loops in Python: for loops and while loops.

### 3.2.1 For Loops

For loops allow you to iterate over a sequence of items, such as a list or a string. Here's the basic syntax:

```py
for item in sequence:
    # code to be executed for each item in the sequence
```

For example, let's say we want to write a program that prints the numbers from 1 to 10:

```py
for i in range(1, 11):
    print(i)
```

In this example, we use the range function to generate a sequence of numbers from 1 to 10, and then use the for loop to print each number.

### 3.2.2 While Loops

While loops allow you to repeat a block of code as long as a certain condition is true. Here's the basic syntax:

```py
while condition:
    # code to be executed as long as the condition is true
```

For example, let's say we want to write a program that keeps prompting the user to enter a number until they enter a negative number:

```py
num = 0

while num >= 0:
    num = int(input("Enter a number: "))
    print("You entered", num)

print("You entered a negative number")
```

In this example, we use the while loop to keep prompting the user to enter a number until they enter a negative number.

### Mini-project 3: 

Write a program that generates a multiplication table up to 10 x 10.

## 3.3 Break and Continue Statements

Break and continue statements allow you to control the flow of your program within a loop.

### 3.3.1 Break Statements

Break statements allow you to exit a loop prematurely. Here's an example:

```py
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

In this example, we use the break statement to exit the loop when i is equal to 5.

### 3.3.2 Continue Statements

Continue statements allow you to skip over certain iterations of a loop.

Here's an example of a continue statement:

```py
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
```

In this example, we use the continue statement to skip over the iteration where i is equal to 5, and continue with the next iteration.

### Mini-project 1: 

Write a program that prompts the user to enter 10 numbers and calculates their sum, but skips over any negative numbers using the continue statement.

### Mini-project 2: 

Write a program that prompts the user to enter a string and prints out each character of the string one by one, but skips over any vowels using the continue statement.

### Mini-project 3: 

Write a program that prompts the user to enter a number and prints out all the prime numbers up to that number using a while loop and the break statement.