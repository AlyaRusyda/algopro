file = open("L200240290", "w")

file.write("L200240290\n")
file.write("31-07-2006\n")
file.write("Alya Rusyda Maharistya")

file = open("L200240290", "r")
read = file.read()
print(read)
file.close()