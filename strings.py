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
# s[0] = "J"
s = "J" + s[1:]
print(s)

# Membership Operators
print("py" in "python")
print("Java" in "Python")

# Useful Built-in Functions
print(len("python"))
print(max("abc"))
print(min("abc"))

# Coding Problems

# Reverse a String
def reverse(c):
    return c[::-1]
print(reverse("Rohit"))

def reverse(s):
    ans = ""
    for ch in s:
        ans = ch + ans
    return ans
print(reverse("Rohit"))

# palindrome Check
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("madam"))

# Count Vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    
    for ch in s:
        if ch in vowels:
            count += 1
    return count

print(count_vowels("Rohit"))

# ⭐ Assignment
# Theory
# What is the difference between indexing and slicing?
# Why are strings immutable?
# What does find() return if the substring is not present?
# Coding

# Write programs for:

# Reverse a string.
# Check whether a string is a palindrome.
# Count vowels in a string.
# Count the frequency of each character.
# Remove all spaces from a string.
