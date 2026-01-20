# Python - Exceptions

This project focuses on **Errors and Exceptions** in Python and how to write safe code using:
- `try / except`
- `try / except / finally`
- raising built-in exceptions
- printing errors to `stderr`

All scripts are compatible with **Ubuntu 20.04 LTS** using **Python 3.8.5** and follow **pycodestyle 2.7.\***.

---

## Learning Objectives

By the end of this project, you should be able to explain:

- Why Python programming is awesome
- The difference between **errors** and **exceptions**
- What exceptions are and how to use them
- When and why we need exceptions
- How to correctly handle an exception
- The purpose of catching exceptions
- How to raise a built-in exception
- When to use `finally` (clean-up / guaranteed actions)

---

## Requirements

- Python 3.8.5
- All files end with a new line
- First line of all files: `#!/usr/bin/python3`
- A `README.md` file is mandatory
- All files must be executable
- File length may be tested using `wc`

---

## Directory

**Repository:** `holbertonschool-higher_level_programming`  
**Directory:** `python-exceptions`

---

## 0) 0-safe_print_list.py — Safe list printing

Goal: Print up to x elements from a list safely and return how many were actually printed.

**Key idea:**
Use a loop + try/except IndexError to stop when list ends.
No len() allowed, so we rely on exceptions to detect out-of-range.

## 1) 1-safe_print_integer.py — Safe integer printing
Goal: Print a value as an integer using "{:d}".format().
**Key idea:**
If formatting succeeds → it’s an integer → return True.
If it fails (TypeError / ValueError) → return False.

## 2) 2-safe_print_list_integers.py — Print only integers

Goal: Access first x elements and print only integers, return how many integers were printed.
**Key idea:**
Loop through indexes 0..x-1
Try printing each with "{:d}".format()
If it’s not an integer → skip silently (catch TypeError/ValueError)
**Important:** Do NOT catch IndexError
If x is bigger than list length, an exception should occur (as in the provided example).

## 3) 3-safe_print_division.py — Division with debug (finally)
Goal: Divide a / b, return result or None, and always print:
Inside result: <result> (even if division fails)
**Key idea:**
Use try to compute division
Catch ZeroDivisionError
Use finally to print the debug line no matter what.

## 4) 4-list_division.py — Divide two lists safely
Goal: Divide element-by-element for list_length and return a new list.
**Key idea:**
For each index i:
Try: my_list_1[i] / my_list_2[i]
If fails:
TypeError → print wrong type and put 0
ZeoDivisionError → print division by 0 and put 0
IndexError → print out of range and put 0
Use finally to always append a result for each index.

## 5) 5-raise_exception.py — Raise TypeError
Goal: Write a function that raises a TypeError.
**Key idea:**
Simply: raise TypeError

## 6) 6-raise_exception_msg.py — Raise NameError with message
Goal: Raise a NameError with a custom message.
**Key idea:**
raise NameError(message)

## Advanced Tasks
## 100) 100-safe_print_integer_err.py — Integer print + stderr

Goal: Same as task 1, but if it fails:
return False
print error to stderr as: Exception: <error>
**Key idea:**
Use try/except with (TypeError, ValueError)
Print to stderr using sys.stderr.write(...)

## 101) 101-safe_function.py — Execute function safely

Goal: Execute fct(*args) safely.
If success → return result
If any exception happens → return None and print to stderr:
Exception: <error>
**key idea:**
Catch Exception (general) because we want to handle any runtime error.
Print to stderr so output can be redirected/hidden.

## 102) 102-magic_calculation.py — Bytecode translation

Goal: Recreate a function that matches the given bytecode exactly.
What it does (logic):
result = 0
Loop i in range(1, 3) (i = 1, 2)
**Try:**
if i > a: raise Exception("Too far")
else: result += (a ** b) / i


