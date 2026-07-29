# Day 07 - Loops in Python

Loops are used to execute a block of code repeatedly.

## 1. for Loop

The `for` loop is used to iterate over a sequence such as a string, list, tuple, or range.

### Syntax

```python
for variable in sequence:
    # Code
```

### Example

```python
fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(fruit)
```

---

## range() Function

The `range()` function generates a sequence of numbers.

### Syntax

```python
range(start, stop, step)
```

Examples:

```python
# 0 to 4
for i in range(5):
    print(i)

# 1 to 5
for i in range(1, 6):
    print(i)

# Even numbers
for i in range(2, 11, 2):
    print(i)
```

---

## 2. while Loop

The `while` loop executes as long as the given condition is `True`.

### Syntax

```python
while condition:
    # Code
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## else with while Loop

The `else` block executes when the `while` loop finishes normally (i.e., not terminated using `break`).

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
else:
    print("Loop completed successfully.")
```

---

## Do-While Loop in Python

Python does **not** have a built-in `do-while` loop.

However, we can simulate it using a `while True` loop with a `break` statement.

Example:

```python
while True:
    num = int(input("Enter a positive number: "))

    if num > 0:
        print("Valid Input")
    else:
        print("Invalid Input")

    choice = input("Continue? (yes/no): ").lower()

    if choice != "yes":
        break
```

In this example, the loop body executes **at least once**, which is the behavior of a do-while loop.

## 3. break Statement

The `break` statement is used to terminate the loop immediately, even if the loop condition is still `True`.

### Example

```python
for i in range(1, 11):
    if i == 6:
        break
    print(i)
```

**Output**

```
1
2
3
4
5
```

The loop stops as soon as `i` becomes `6`.

---

## 4. continue Statement

The `continue` statement skips the current iteration and moves to the next iteration of the loop.

### Example

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Output**

```
1
2
4
5
```

The number `3` is skipped.

---

## Difference Between break and continue

| break | continue |
|--------|----------|
| Terminates the loop completely. | Skips the current iteration and continues with the next iteration. |
| Control moves outside the loop. | Control returns to the beginning of the loop for the next iteration. |

### Example Using while Loop

```python
count = 1

while count <= 10:
    if count == 5:
        break
    print(count)
    count += 1
```

Output:

```
1
2
3
4
```

### continue with while Loop

```python
count = 0

while count < 5:
    count += 1

    if count == 3:
        continue

    print(count)
```

Output:

```
1
2
4
5
```