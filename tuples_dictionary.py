grades = {
    ("John","Math"):5,
    ("Alice","Science"):4,
    ("Bob","History"):3
}

john_math = grades[("John","Math")]
print("John's Math grade is:", john_math)

grades[("Bob","History")] = 4

print("Bob's updates History Grade is:", grades[("Bob","History")])

keys = list(grades.keys())
student, subject = keys[0]
print("First key - Student:",student, ",Subject:",subject)
    