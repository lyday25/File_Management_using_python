
import os
if os.path.exists("emptyfile.txt"):
  os.remove("emptyfile.txt")
  print("File has been deleted")
else:
  print("The file does not exist")