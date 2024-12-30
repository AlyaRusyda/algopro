import shelve

file = open("L200240290", "r")
data = shelve.open('Alya.data')
data['nim'] = file.readline()
data['ttl'] = file.readline()
data['nama'] = file.readline()

print(data['nim'])
print(data['ttl'])
print(data['nama'])
file.close()