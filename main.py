
f = open("first.txt", "r")
file = open("reversed.txt", "w")
x = f.read()
file.write(x[::-1])

file.close()
