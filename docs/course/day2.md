# Collection Types

In this course, we will explore two of the most common collection types, `List` amd `Tuple`.

## List

In Python, a list is a built-in data structure that allows you to store and manipulate a collection of values. 
It is an ordered collection of items, where each item can be of different data types such as integers, floats, 
strings, or even other lists.

Here are some key features of lists in Python:

### Creating a List

Creating a list in python can be done in two ways, by using the angle brackets `[]` or by using the `list()` constructor. 
In this course, we will be commonlu deal with python using square brackets.

Let's say we'll create a list of students:

```py
students = ['Agnes', 'Kristina', 'Alyanna', 'Joshua', 'Ruth']
```

Elements in a list is numbered by indexes. For the above example, we have:

| Element    | Index |
| ---------- | ----- |
| 'Agnes'    | `0`   |
| 'Kristina' | `1`   |
| 'Alyanna'  | `2`   |
| 'Joshua'   | `3`   |
| 'Ruth'     | `4`   |

To access the elements in a list, we use the square bracket like this:

```py title="Accessing element in a list"
print(students[3])

# output: 'Joshua'
```
