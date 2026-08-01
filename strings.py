# String

s = "Python"
# print(s[0])
# print(s[2])
# print(s[-1])

# String Slicing

# syntax = string[start:end:step]
# start => is include 
# end => is excluded

print(s[1:4])
print(s[0:4:2])
print(s[:4])
print(s[2:])
print(s[::-1])

# string methods
print(s.upper())
print(s.lower())

a = "  Python  "
print(a)
print(a.strip())

b = "I Love Java"
print(b.replace("Java","Python"))

text = "apple banana mango"
print(text.split())

print(s.find("t"))
print(s.find("z"))

# Strings are Immutable

