import pickle

file = open("dump.txt", "rb")
data = pickle.load(file)
print(data)
file.close()