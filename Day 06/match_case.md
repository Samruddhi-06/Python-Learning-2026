# Day 06 - Match Case Statement

The `match-case` statement was introduced in **Python 3.10**. It is similar to the `switch` statement in languages like Java and C++.

It compares a value against multiple cases and executes the matching block of code.

## Syntax

```python
match expression:
    case value1:
        # Code
    case value2:
        # Code
    case _:
        # Default Code
```

- `match` evaluates the expression.
- `case` specifies possible values.
- `_` acts as the **default case** when no other case matches.

---

## Example 1: Day of the Week

```python
day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid Day")
```

---

## Example 2: Calculator

```python
operator = input("Enter operator (+, -, *, /): ")

a = 10
b = 5

match operator:
    case "+":
        print(a + b)
    case "-":
        print(a - b)
    case "*":
        print(a * b)
    case "/":
        print(a / b)
    case _:
        print("Invalid Operator")
```

---

## Advantages

- Improves code readability.
- Better than writing long `if-elif-else` chains.
- Easy to maintain.
- Similar to the `switch` statement in other programming languages.

---

## Note

The `match-case` statement is available only in **Python 3.10 and later**.