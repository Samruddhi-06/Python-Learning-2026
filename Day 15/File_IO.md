# Day 15 - File I/O in Python

File I/O (Input/Output) allows Python programs to create, read, write, and modify files.

## 1. Opening a File

The `open()` function is used to open a file.

### Syntax

```python
file = open("filename", "mode")
```

Example:

```python
file = open("sample.txt", "r")
```

After using the file, it should be closed:

```python
file.close()
```

---

# 2. File Modes

The mode determines what operations can be performed on a file.

| Mode | Description |
|------|-------------|
| `r` | Read the file |
| `w` | Write to the file |
| `a` | Append to the file |
| `x` | Create a new file |
| `t` | Text mode |
| `b` | Binary mode |
| `r+` | Read and write |
| `w+` | Write and read |
| `a+` | Append and read |

### `r` - Read

Opens an existing file for reading.

```python
file = open("sample.txt", "r")
```

The file must already exist.

### `w` - Write

Opens a file for writing.

```python
file = open("sample.txt", "w")
```

If the file exists, its previous contents are **overwritten**.

If it does not exist, Python creates it.

### `a` - Append

Opens a file for adding content at the end.

```python
file = open("sample.txt", "a")
```

Existing content is preserved.

### `x` - Create

Creates a new file.

```python
file = open("sample.txt", "x")
```

An error occurs if the file already exists.

---

# 3. Reading a File

The `read()` method reads the contents of a file.

```python
file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()
```

---

# 4. Writing to a File

The `write()` method writes text to a file.

```python
file = open("sample.txt", "w")

file.write("Hello Python!")

file.close()
```

> Opening a file in `w` mode replaces its existing contents.

---

# 5. Closing a File

The `close()` method closes an opened file.

```python
file = open("sample.txt", "r")

print(file.read())

file.close()
```

Closing files is important because it releases system resources.

---

# 6. The `with` Statement

The `with` statement automatically closes the file after the block finishes.

```python
with open("sample.txt", "r") as file:
    print(file.read())
```

You don't need to explicitly call:

```python
file.close()
```

The `with` statement is the recommended approach for most file operations.

---

# 7. `readlines()`

The `readlines()` method reads all lines and returns them as a list.

```python
with open("sample.txt", "r") as file:
    lines = file.readlines()

print(lines)
```

Example file:

```text
Python
Java
C++
```

Output:

```python
['Python\n', 'Java\n', 'C++\n']
```

---

# 8. `writelines()`

The `writelines()` method writes multiple strings to a file.

```python
lines = ["Python\n", "Java\n", "C++\n"]

with open("sample.txt", "w") as file:
    file.writelines(lines)
```

`writelines()` does **not** automatically add newline characters, so `\n` must be included when required.

---

# 9. `tell()`

The `tell()` method returns the current position of the file pointer.

```python
with open("sample.txt", "r") as file:
    print(file.tell())

    print(file.read(6))

    print(file.tell())
```

---

# 10. `seek()`

The `seek()` method moves the file pointer to a specified position.

```python
with open("sample.txt", "r") as file:
    print(file.read(5))

    file.seek(0)

    print(file.read(5))
```

Here, `seek(0)` moves the file pointer back to the beginning of the file.

---

# 11. `truncate()`

The `truncate()` method changes the size of a file.

If a size is provided, the file is truncated to that number of bytes.

```python
with open("sample.txt", "w") as file:
    file.write("Hello Python")

    file.truncate(5)
```

The file will contain:

```text
Hello
```

If `truncate()` is called without a size, the file is truncated at the current file position.

```python
with open("sample.txt", "r+") as file:
    file.seek(5)
    file.truncate()
```

---

# Summary

- `open()` opens a file.
- `r` is used for reading.
- `w` is used for writing and can overwrite existing content.
- `a` adds content to the end of a file.
- `x` creates a new file.
- `read()` reads file content.
- `write()` writes a string.
- `readlines()` returns lines as a list.
- `writelines()` writes multiple strings.
- `tell()` returns the current file-pointer position.
- `seek()` changes the file-pointer position.
- `truncate()` reduces or changes the file size.
- `close()` closes a file.
- `with` automatically handles closing the file.