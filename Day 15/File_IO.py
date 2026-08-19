# f = open('Day 15/myfile.txt', 'r')
# text = f.read()
# print(text)
# f.close()

# f = open('Day 15/myfile.txt', 'w')
# f.write("Hello! I am new to the python.")
# f.close()

# f = open('Day 15/myfile.txt', 'a')
# f.write("Moving towards advance python as we completed the basic one.")
# f.close()

# # alternate way of file io

# with open('Day 15/myfile2.txt', 'w') as f :
#     f.write("Understanding IO concepts in python.")


# readlines()

f = open('Day 15/myfile.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)


f = open('Day 15/myfile2.txt', 'r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])

    print(f"Marks of student {i} in Maths is : {m1}")
    print(f"Marks of student {i} in English is : {m2}")
    print(f"Marks of student {i} in SSt is : {m3}")
    print(line)


# writelines()

f = open('Day 15/myfile3.txt', 'w')
lines = ['Maths : 55', 'English : 63', 'Science : 45', 'Hindi : 75', 'SST : 59']
for line in lines:
    f.writelines(line + '\n')
f.close()


# seek()

with open('Day 15/file.txt', 'r') as f:
    f.seek(10)
    data = f.read(3)
    print(data)

# tell

with open('Day 15/file.txt', 'r+') as f:
    data = f.read(10)
    curr_pos = f.tell()
    print(f.seek(curr_pos))


# truncate()

with open('Day 15/sample.txt', 'w') as f:
    f.write("This is an example txt file.")
    f.truncate(10)


with open('Day 15/sample.txt', 'r') as f:
    print(f.read())