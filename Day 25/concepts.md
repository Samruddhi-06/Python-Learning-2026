# Day 25 - Time Module and Command Line Utility

## 1. Time Module

Python provides a built-in module called `time` for working with time-related operations.

We can import it using:

```python
import time
```

The `time` module can be used for:

* Getting the current time
* Getting timestamps
* Pausing program execution
* Formatting time
* Measuring execution time

---

# 2. `time.time()`

The `time.time()` function returns the current time as the number of seconds since the **Unix epoch**.

The Unix epoch is:

```text
January 1, 1970, 00:00:00 UTC
```

### Example

```python
import time

current_time = time.time()

print(current_time)
```

Output will look similar to:

```text
1788770123.456789
```

The exact value will be different every time because it represents the current moment.

The returned value is a **floating-point number**.

---

## Measuring Execution Time with `time.time()`

`time.time()` can also be used to measure approximately how long a piece of code takes to execute.

```python
import time

start = time.time()

for i in range(1000000):
    pass

end = time.time()

print("Execution time:", end - start, "seconds")
```

Output may look like:

```text
Execution time: 0.0352 seconds
```

Here:

```python
start = time.time()
```

records the starting timestamp.

Then:

```python
end = time.time()
```

records the ending timestamp.

The difference:

```python
end - start
```

gives the elapsed time.

---

# 3. `time.strftime()`

The correct function name is **`time.strftime()`**, not `time.strf()`.

`strftime()` means **string format time**.

It converts a time structure into a formatted string.

### Example

```python
import time

current_time = time.localtime()

formatted_time = time.strftime("%H:%M:%S", current_time)

print(formatted_time)
```

Output:

```text
15:42:18
```

The exact output depends on the current time.

---

# 4. Common `strftime()` Format Codes

`strftime()` uses format codes to specify how the date and time should be displayed.

| Code | Meaning              | Example     |
| ---- | -------------------- | ----------- |
| `%Y` | Four-digit year      | `2026`      |
| `%y` | Two-digit year       | `26`        |
| `%m` | Month                | `09`        |
| `%d` | Day                  | `07`        |
| `%H` | Hour, 24-hour format | `15`        |
| `%I` | Hour, 12-hour format | `03`        |
| `%M` | Minute               | `42`        |
| `%S` | Second               | `18`        |
| `%p` | AM/PM                | `PM`        |
| `%A` | Full weekday name    | `Monday`    |
| `%a` | Short weekday name   | `Mon`       |
| `%B` | Full month name      | `September` |
| `%b` | Short month name     | `Sep`       |

---

## Example with Date and Time

```python
import time

current_time = time.localtime()

formatted_time = time.strftime(
    "%d-%m-%Y %H:%M:%S",
    current_time
)

print(formatted_time)
```

Output:

```text
07-09-2026 15:42:18
```

---

## Example with 12-Hour Format

```python
import time

current_time = time.localtime()

formatted_time = time.strftime(
    "%d %B %Y, %I:%M:%S %p",
    current_time
)

print(formatted_time)
```

Output:

```text
07 September 2026, 03:42:18 PM
```

---

# 5. `time.localtime()`

`time.localtime()` converts the current timestamp into local time information.

```python
import time

current_time = time.localtime()

print(current_time)
```

It returns a `struct_time` object containing information such as:

```text
year
month
day
hour
minute
second
weekday
day of year
DST information
```

It is commonly used together with `strftime()`:

```python
import time

current_time = time.localtime()

print(time.strftime("%d-%m-%Y", current_time))
```

---

# 6. `time.sleep()`

The `time.sleep()` function pauses program execution for a specified number of seconds.

### Example

```python
import time

print("Hello")

time.sleep(2)

print("World")
```

Output:

```text
Hello
```

After approximately 2 seconds:

```text
World
```

---

## Countdown Example

```python
import time

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

print("Go!")
```

Output:

```text
5
4
3
2
1
Go!
```

Each number is displayed approximately one second apart.

---

# 7. Creating a Command Line Utility

A **command-line utility** is a program that can be executed from the terminal and controlled using commands and arguments.

For example:

```text
python utility.py --name Sam
```

Instead of opening a program and entering information through a graphical interface, we provide information directly through the terminal.

Command-line utilities are commonly used for:

* File management
* Automation
* Data processing
* Developer tools
* System administration
* Converting files
* Running repetitive tasks

---

# 8. Command Line Arguments

Python provides the `sys` module for accessing command-line arguments.

```python
import sys

print(sys.argv)
```

Suppose we run:

```text
python utility.py Sam 21
```

Then `sys.argv` will contain something similar to:

```python
[
    "utility.py",
    "Sam",
    "21"
]
```

The first element:

```python
sys.argv[0]
```

is the name/path of the script.

The arguments provided by the user start from:

```python
sys.argv[1]
```

---

# 9. Simple Command Line Utility Using `sys.argv`

Create a file:

```text
utility.py
```

Code:

```python
import sys

name = sys.argv[1]

print(f"Hello, {name}!")
```

Run it from the terminal:

```text
python utility.py Sam
```

Output:

```text
Hello, Sam!
```

Here:

```python
sys.argv[1]
```

contains:

```text
Sam
```

---

# 10. Why `argparse` is Better for Command Line Utilities

For small experiments, `sys.argv` can be enough.

However, proper command-line utilities commonly use Python's built-in **`argparse`** module.

`argparse` allows us to create:

* Named arguments
* Optional arguments
* Required arguments
* Help messages
* Default values
* Type checking
* Better error messages

---

# 11. Creating a Utility with `argparse`

Let's create a small command-line utility that displays a greeting.

Create:

```text
greet.py
```

```python
import argparse

parser = argparse.ArgumentParser(
    description="A simple greeting command-line utility."
)

parser.add_argument(
    "--name",
    required=True,
    help="Enter the person's name."
)

args = parser.parse_args()

print(f"Hello, {args.name}!")
```

Run:

```text
python greet.py --name Sam
```

Output:

```text
Hello, Sam!
```

---

# 12. The `--help` Option

One of the advantages of `argparse` is that it automatically provides a help option.

Run:

```text
python greet.py --help
```

You will get information similar to:

```text
usage: greet.py [-h] --name NAME

A simple greeting command-line utility.

options:
  -h, --help   show this help message and exit
  --name NAME  Enter the person's name.
```

This makes the utility easier for other people to understand.

---

# 13. Creating a Time Command Line Utility

Now let's combine today's topics.

We can create a utility that displays the current date and time.

Create:

```text
time_cli.py
```

```python
import argparse
import time


parser = argparse.ArgumentParser(
    description="Display the current date and time."
)

parser.add_argument(
    "--format",
    default="%d-%m-%Y %H:%M:%S",
    help="Specify the time format."
)

args = parser.parse_args()

current_time = time.localtime()

formatted_time = time.strftime(
    args.format,
    current_time
)

print(formatted_time)
```

Run:

```text
python time_cli.py
```

Output:

```text
07-09-2026 15:42:18
```

---

## Using a Custom Format

We can provide a different format from the command line:

```text
python time_cli.py --format "%H:%M:%S"
```

Output:

```text
15:42:18
```

Another example:

```text
python time_cli.py --format "%d %B %Y"
```

Output:

```text
07 September 2026
```

---

# 14. Understanding the Complete Utility

The first part imports the required modules:

```python
import argparse
import time
```

`argparse` handles command-line arguments.

`time` provides time-related functionality.

Then we create an argument parser:

```python
parser = argparse.ArgumentParser(
    description="Display the current date and time."
)
```

The `description` explains what our utility does.

Then we create an optional argument:

```python
parser.add_argument(
    "--format",
    default="%d-%m-%Y %H:%M:%S",
    help="Specify the time format."
)
```

The user can provide:

```text
--format
```

If the user doesn't provide it, the default format is used.

Then:

```python
args = parser.parse_args()
```

reads and processes the command-line arguments.

Finally:

```python
current_time = time.localtime()

formatted_time = time.strftime(
    args.format,
    current_time
)

print(formatted_time)
```

gets the local time, formats it, and displays it.

---

# 15. A Better Command Line Utility Project

For today's practice, create a small utility called:

```text
time-tool
```

The utility can provide different operations:

```text
python time_tool.py
```

Show the current date and time.

```text
python time_tool.py --time
```

Show only the current time.

```text
python time_tool.py --date
```

Show only the current date.

```text
python time_tool.py --help
```

Show instructions.

### Example Code

```python
import argparse
import time


parser = argparse.ArgumentParser(
    description="A simple command-line time utility."
)

parser.add_argument(
    "--time",
    action="store_true",
    help="Display the current time."
)

parser.add_argument(
    "--date",
    action="store_true",
    help="Display the current date."
)

args = parser.parse_args()

current_time = time.localtime()

if args.time:
    print(time.strftime("%H:%M:%S", current_time))

elif args.date:
    print(time.strftime("%d-%m-%Y", current_time))

else:
    print(time.strftime("%d-%m-%Y %H:%M:%S", current_time))
```

### Running the Utility

Current date and time:

```text
python time_tool.py
```

Output:

```text
07-09-2026 15:42:18
```

Only time:

```text
python time_tool.py --time
```

Output:

```text
15:42:18
```

Only date:

```text
python time_tool.py --date
```

Output:

```text
07-09-2026
```

Help:

```text
python time_tool.py --help
```

---

# Summary

## Time Module

Import the module:

```python
import time
```

### `time.time()`

Returns the current Unix timestamp.

```python
time.time()
```

### `time.localtime()`

Returns the current local time as a `struct_time`.

```python
time.localtime()
```

### `time.strftime()`

Formats time information into a string.

```python
time.strftime("%H:%M:%S", time.localtime())
```

### `time.sleep()`

Pauses execution for a specified number of seconds.

```python
time.sleep(2)
```

---

## Command Line Utilities

A command-line utility is a program that can be run and controlled from the terminal.

Basic arguments can be accessed using:

```python
import sys

sys.argv
```

For more structured command-line programs, use:

```python
import argparse
```

The basic workflow is:

```text
Create parser
     ↓
Add arguments
     ↓
Parse arguments
     ↓
Use arguments
     ↓
Display result
```

The main functions/methods to remember are:

| Function/Method             | Purpose                             |
| --------------------------- | ----------------------------------- |
| `time.time()`               | Get Unix timestamp                  |
| `time.localtime()`          | Get local time information          |
| `time.strftime()`           | Format time as a string             |
| `time.sleep()`              | Pause program execution             |
| `sys.argv`                  | Access command-line arguments       |
| `argparse.ArgumentParser()` | Create command-line argument parser |
| `parser.add_argument()`     | Add an argument                     |
| `parser.parse_args()`       | Parse command-line arguments        |

---

