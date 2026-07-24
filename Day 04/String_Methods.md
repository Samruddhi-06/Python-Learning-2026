# Day 04 - Python String Methods

Python provides many built-in string methods to manipulate strings.

## 1. upper()

Converts all characters to uppercase.

```python
text = "hello"
print(text.upper())
```

## 2. lower()

Converts all characters to lowercase.

```python
text = "HELLO"
print(text.lower())
```

## 3. strip()

Removes leading and trailing whitespace.

```python
text = "  Python  "
print(text.strip())
```

## 4. rstrip()

Removes trailing whitespace.

```python
text = "Python   "
print(text.rstrip())
```

## 5. replace()

Replaces one substring with another.

```python
text = "Hello World"
print(text.replace("World", "Python"))
```

## 6. split()

Splits a string into a list.

```python
text = "Python Java C"
print(text.split())
```

## 7. capitalize()

Capitalizes the first character.

```python
text = "python"
print(text.capitalize())
```

## 8. center()

Centers the string within a specified width.

```python
text = "Python"
print(text.center(20, "*"))
```

## 9. count()

Returns the number of occurrences of a substring.

```python
text = "banana"
print(text.count("a"))
```

## 10. endswith()

Checks if the string ends with a specified value.

```python
text = "hello.py"
print(text.endswith(".py"))
```

## 11. find()

Returns the first index of a substring or -1 if not found.

```python
text = "Python"
print(text.find("t"))
```

## 12. index()

Returns the first index of a substring.

```python
text = "Python"
print(text.index("t"))
```

## 13. isalnum()

Returns True if all characters are alphanumeric.

```python
text = "Python123"
print(text.isalnum())
```

## 14. isalpha()

Returns True if all characters are alphabets.

```python
text = "Python"
print(text.isalpha())
```

## 15. islower()

Checks whether all characters are lowercase.

```python
text = "python"
print(text.islower())
```

## 16. isprintable()

Returns True if all characters are printable.

```python
text = "Hello"
print(text.isprintable())
```

## 17. isspace()

Returns True if all characters are whitespace.

```python
text = "   "
print(text.isspace())
```

## 18. istitle()

Returns True if each word starts with an uppercase letter.

```python
text = "Hello World"
print(text.istitle())
```

## 19. isupper()

Checks whether all characters are uppercase.

```python
text = "PYTHON"
print(text.isupper())
```

## 20. startswith()

Checks if the string starts with a specified value.

```python
text = "Python"
print(text.startswith("Py"))
```

## 21. swapcase()

Converts uppercase to lowercase and vice versa.

```python
text = "PyThOn"
print(text.swapcase())
```

## 22. title()

Converts the first letter of each word to uppercase.

```python
text = "welcome to python"
print(text.title())
```