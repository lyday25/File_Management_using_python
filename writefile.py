f = open("demofile2.txt", "a")
f.write("Best of luck!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())