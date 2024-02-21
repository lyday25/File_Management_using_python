class Person:
  def __init__(self, name, age, email, phone_number, job_title):
    self.name = name
    self.age = age
    self.email = email
    self.phone_number = phone_number
    self.job_title = job_title
    
p1 = Person("Bola", 26 , "bj@yahoo.com" , "08023145789" , "Data curator")

print(p1.name)
print(p1.age)
print(p1.email)
print(p1.phone_number)
print(p1.job_title)
