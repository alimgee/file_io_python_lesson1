f = open("text.txt", 'r')
#lines = f.readlines()
lines = f.read()
f.close()

print(lines)