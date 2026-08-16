# Python Decorator Practice

## 📌 About

A beginner-friendly Python project to practice **decorators** and understand how they wrap functions and add extra behavior before and after execution.

## 🎯 Concepts Learned

- What decorators are
- Creating a decorator function
- Creating a wrapper function
- Using `@decorator` syntax
- Passing functions as arguments
- Using `__name__`
- Reusing one decorator with multiple functions

## 🧠 How It Works

The `log_execution` decorator displays a message before and after the decorated function runs.

Example:

```python
@log_execution
def calculation():
    print("Calculating total!!!")
