# Day 14 - Python Concepts

## 1. Short-Hand if-else Statement

Python provides a short way to write an `if-else` statement in a single line.

### Normal if-else

```python
age = 18

if age >= 18:
    result = "Eligible"
else:
    result = "Not Eligible"

print(result)
```

### Short-hand if-else

```python
age = 18

result = "Eligible" if age >= 18 else "Not Eligible"

print(result)
```

### Syntax

```python
value_if_true if condition else value_if_false
```

### Example

```python
a = 10
b = 20

greater = a if a > b else b

print(greater)
```

---

## 2. enumerate() Function

The `enumerate()` function is used to loop through an iterable while keeping track of the index.

### Example Without enumerate()

```python
fruits = ["Apple", "Mango", "Banana"]

for i in range(len(fruits)):
    print(i, fruits[i])
```

### Using enumerate()

```python
fruits = ["Apple", "Mango", "Banana"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

### Starting Index from a Different Number

The `start` parameter can be used to specify the starting index.

```python
fruits = ["Apple", "Mango", "Banana"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

Output:

```text
1 Apple
2 Mango
3 Banana
```

### Syntax

```python
enumerate(iterable, start=0)
```

---

# 3. Virtual Environment

A virtual environment is an isolated Python environment for a project.

It allows each project to have its own packages and package versions without affecting other Python projects.

### Create a Virtual Environment

Windows:

```bash
python -m venv .venv
```

### Activate the Virtual Environment

Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
.venv\Scripts\activate
```

After activation, you will usually see:

```text
(.venv)
```

at the beginning of the terminal prompt.

### Deactivate

```bash
deactivate
```

---

# 4. requirements.txt

`requirements.txt` contains the Python packages required by a project.

### Create requirements.txt

If packages are installed in the virtual environment:

```bash
pip freeze > requirements.txt
```

This records the installed packages and their versions.

### Install Packages from requirements.txt

```bash
pip install -r requirements.txt
```

This allows another developer to install the project's dependencies.

---

# 5. .gitignore for Virtual Environment

The virtual environment should normally not be uploaded to GitHub.

Create a file named:

```text
.gitignore
```

Add:

```text
.venv/
venv/
__pycache__/
*.pyc
```

This prevents the virtual environment and Python cache files from being tracked by Git.

---

# Summary

- Short-hand if-else allows simple conditional expressions in one line.
- `enumerate()` provides both the index and value while iterating.
- A virtual environment isolates project dependencies.
- `requirements.txt` records project dependencies.
- `.gitignore` prevents unnecessary files such as `.venv` and `__pycache__` from being committed.