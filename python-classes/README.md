# Python - Classes and Objects (OOP)

This project introduces Object-Oriented Programming (OOP) in Python.  
You will practice creating classes, instances, attributes (public/protected/private), properties, methods, validation, printing objects, and comparisons.

---

---

## Resources (Read/Watch)

https://python-course.eu/oop/properties-vs-getters-and-setters.php

https://www.youtube.com/watch?v=apACNr7DC_s

https://www.youtube.com/watch?v=-DP1i2ZU9gk
  

---

## Learning Objectives

By the end of this project, you should be able to explain (without Google):

- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- Difference between a class and an object/instance
- What is an attribute
- Public, protected and private attributes (how to use them)
- What is `self`
- What is a method
- What is the special `__init__` method and how to use it
- Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- Difference between an attribute and a property in Python
- The Pythonic way to write getters and setters
- Dynamically creating new attributes for existing instances
- How to bind attributes to objects and classes
- What is `__dict__` (class/instance) and what it contains
- How Python finds attributes
- How to use `getattr`

---

## Requirements

### Documentation (Mandatory)
- Modules, classes, and functions must have docstrings:
  - `python3 -c 'print(__import__("my_module").__doc__)'`
  - `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
  - `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
  - `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
- A docstring must be a real sentence describing the purpose.

---

## Project Structure

Repository: `holbertonschool-higher_level_programming`  
Directory: `python-classes`

---

## Tasks Overview

### 0. My first square
- Create an empty class `Square`.

### 1. Square with size
- Add a private instance attribute `__size`.
- Initialize with `size` (no validation).

### 2. Size validation
- Validate `size`:
  - must be an `int` → `TypeError: size must be an integer`
  - must be `>= 0` → `ValueError: size must be >= 0`

### 3. Area of a square
- Add method `area()` to return `size * size`.

### 4. Access and update private attribute
- Add property `size` with getter/setter validation.

### 5. Printing a square
- Add method `my_print()` to print the square using `#`.

### 6. Coordinates of a square
- Add private attribute `__position` (tuple of 2 positive integers).
- Update printing to respect the position offset.

### 7. Singly linked list (Advanced)
- Implement `Node` and `SinglyLinkedList`.
- Insert nodes with `sorted_insert()` and print list line-by-line.

### 8. Print Square instance (Advanced)
- Implement `__str__` so printing an instance behaves like `my_print()`.

### 9. Compare 2 squares (Advanced)
- Allow comparisons based on area (`==`, `!=`, `<`, `<=`, `>`, `>=`).
- `size` can be `int` or `float`.

---


