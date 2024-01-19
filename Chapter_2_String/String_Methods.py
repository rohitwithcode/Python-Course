a="Rohit @!@# #@#"
print(len(a))
print(a.upper()) # String are Immutable
print(a.lower())
print(a)
print(a.rstrip("!@#"))
print(a.replace("Rohit","Mohit"))
print(a.split(" "))

Heading="tHIs is an hEAdIng of parAgRapH."
print(Heading.capitalize())

str="Welcome to my coding."
print(str.center(50))
print(len(str))
print(len(str.center(50)))
print(str.count("o"))
print(str.endswith("."))
print(str.endswith("to",2,10))
print(str.startswith("w"))
print(str.startswith("W"))
print(str.find("o"))
print(str.find("Z"))
print(str.index("my"))
string="WelcomeToDelhi"
print(string.isalnum())
s="Coding000"
print(s.isalpha())
print(s.islower())
print(s.isupper())
print(s.isprintable())
s1="      This is not a space"
print(s1.isspace())
print(s1.istitle())
print(s1.swapcase())
print(s1.title())