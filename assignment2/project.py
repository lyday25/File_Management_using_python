f = open("leader.txt", "a")
f.write("Great leader!")
f.write("visionary manager!")
f.close()

#open and read the file after the appending:
f = open("leader.txt", "r")
print(f.read())

#f = open("leader.txt", "r")
#print(f.read())