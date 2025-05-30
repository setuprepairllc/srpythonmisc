f = open("flag.txt", "r")
print(f.read())

f = open("flag.txt", "w")
f.write("added some text to the file")
print(f.read())
f.close()
