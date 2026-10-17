print("\n============================================================")
print("Assignment #2 - Python Data Types")
print("Topic: W3Schools > Python Data Types")
print("============================================================")
print()

stdCode = 34551001
stdName = 'Mohammed'
stdLastname = 'Ali'
stdMidterm = 80
stdFinal = 98.5
stdGPA = 3.7
stdActive = True
stdCourses = ['Python', 'Math', 'English']
stdBirthDate = (2001, 5, 14)
stdProfile = {'name': 'Mohammed', 'city': 'Alexandria'}
stdSkills = {'typing', 'Excel', 'typing'}
stdAdvisor = None


# 1. Use type() to print the data type of stdCode, stdName and stdFinal.
print("\nQuestion 1: Use type() to print the data type of stdCode, stdName and stdFinal.")
print("stdCode =", stdCode, ", stdCode type =", type(stdCode))
print("stdName =", stdName, ", stdName type =", type(stdName))
print("stdFinal =", stdFinal, ", stdFinal type =", type(stdFinal))
print()


# 2. Print the data type of stdActive and stdAdvisor.
print("Question 2: Print the data type of stdActive and stdAdvisor.")
print("stdActive =", stdActive, ", stdActive type =", type(stdActive))
print("stdAdvisor =", stdAdvisor, ", stdAdvisor type =", type(stdAdvisor))
print()


# 3. Print the data type of stdCourses, stdBirthDate, stdProfile and stdSkills.
print("Question 3: Print the data type of stdCourses, stdBirthDate, stdProfile and stdSkills.")

print("stdCourses =", stdCourses, ", stdCourses type =", type(stdCourses),
      "- List is mutable, meaning items can be changed, added, or removed.")

print("stdBirthDate =", stdBirthDate, ", stdBirthDate type =", type(stdBirthDate),
      "- Tuple is immutable, meaning items cannot be changed after it is created.")

print("stdProfile =", stdProfile, ", stdProfile type =", type(stdProfile),
      "- Dictionary is mutable and stores key-value pairs; items can be changed, added, or removed.")

print("stdSkills =", stdSkills, ", stdSkills type =", type(stdSkills),
      "- Set is mutable and stores unique values; items can be added or removed, and duplicates are not kept.")

print()


# 4. PREDICT: How many items will print(stdSkills) show? Why?
# My guess: It will show 2 items because sets do not allow duplicate values.

print("Question 4: PREDICT: How many items will print(stdSkills) show? Why?")
print("My guess: It will show 2 items because sets do not allow duplicate values; only unique values are kept.")
print("stdSkills =", stdSkills)
print()


# 5. Create a variable x = 5j and print its data type.
print("Question 5: Create a variable x = 5j and print its data type.")
x = 5j
print("x =", x, ", x type =", type(x))
print()

print("Complex number explanation with example:")
complexExample = 3 + 5j
print("Example:", complexExample)
print("3 is the real part.")
print("5j is the imaginary part.")
print("j tells Python that the number contains an imaginary part.")
print()

print("Why do we use complex numbers?")
print("Complex numbers help solve mathematical problems that cannot be solved using only real numbers.")
print("For example: x squared = -1")
print("No real number multiplied by itself equals -1.")
print("Mathematics defines the square root of -1 as an imaginary number.")
print("Python uses j to represent the imaginary unit, so 1j * 1j = -1.")
print("Complex numbers are useful in engineering, signal processing, telecommunications, physics, and advanced mathematics.")
print()


# 6. Create a variable r = range(5). Print its data type,
# then print list(r) to see the numbers inside it.

print("Question 6: Create a variable r = range(5). Print its data type, then print list(r) to see the numbers inside it.")

r = range(5)

print("r type =", type(r))
print("list(r) =", list(r))
print()

print("Range explanation:")
print("range() creates a sequence of numbers.")
print("range(5) starts at 0 and stops before 5.")
print("Therefore, range(5) represents the numbers 0, 1, 2, 3, and 4.")
print("list(r) converts the range into a list so we can clearly see the numbers.")
print()


# 7. Convert stdMidterm to a float using float(). Print the new value and its type.
print("Question 7: Convert stdMidterm to a float using float(). Print the new value and its type.")
midtermFloat = float(stdMidterm)
print("midtermFloat =", midtermFloat, ", midtermFloat type =", type(midtermFloat))
print()


# 8. PREDICT: What will print(int(stdFinal)) show? Does it round up?
# My guess: It will show 98. It does not round up.
print("Question 8: PREDICT: What will print(int(stdFinal)) show? Does it round up?")
print("My guess: It will show 98. It does not round up.")
print("int(stdFinal) =", int(stdFinal))
print()


# 9. Convert stdCode to a string and print how many characters it has using len().
print("Question 9: Convert stdCode to a string and print how many characters it has using len().")
codeString = str(stdCode)
print("codeString =", codeString)
print("Number of characters =", len(codeString))
print()


# 10. Create a frozenset from stdCourses and print its data type.
print("Question 10: Create a frozenset from stdCourses and print its data type.")

frozenCourses = frozenset(stdCourses)

print("stdCourses =", stdCourses)
print("frozenCourses =", frozenCourses)
print("frozenCourses type =", type(frozenCourses))
print()

print("Frozenset explanation:")
print("A frozenset is similar to a set, but it is immutable.")
print("Immutable means the values cannot be added, removed, or changed after the frozenset is created.")
print("Like a regular set, a frozenset stores unique values and does not keep duplicates.")
print()

print("In this example:")
print("stdCourses is a list:", stdCourses)
print("frozenset(stdCourses) converts the list into an immutable set of courses.")
print()

print("Why use a frozenset?")
print("Use a frozenset when you want a collection of unique values that should not be changed.")
print()


# 11. Create a variable msg = b"Hello" and print its data type.
print('Question 11: Create a variable msg = b"Hello" and print its data type.')

msg = b"Hello"

print("msg =", msg, ", msg type =", type(msg))
print()

print("String vs. Bytes Explanation:")
print()

print("1. String means readable text for people:")
normalMsg = "Hello"
print('Example: normalMsg = "Hello"')
print("Value =", normalMsg)
print("Type =", type(normalMsg))
print("String = readable text.")
print()

print("Examples of strings:")
print('name = "Mohammed"')
print('city = "Alexandria"')
print('message = "Hello"')
print()

print("2. Bytes means data represented as bytes:")
print('Example: msg = b"Hello"')
print("The b before the text tells Python to treat the value as bytes instead of a regular string.")
print("Type =", type(msg))
print()

print("At the computer level, the characters in this simple example have numeric byte values:")
print("H = 72")
print("e = 101")
print("l = 108")
print("l = 108")
print("o = 111")
print()

print('We can see the byte values by using list(b"Hello"):')
print(list(msg))
print()

print("Why would we use bytes?")
print("Bytes are commonly used when programs work with:")
print("- Files")
print("- Images")
print("- Audio")
print("- Network communications")
print("- Other binary data")
print()

print("Easy way to remember:")
print('String: "Hello" = readable text')
print('Bytes:  b"Hello" = byte data')
print("The b before the quotation marks changes the data type from str to bytes.")
print()


# 12. PREDICT the data type of each value below, then check with type():
#     10    10.0    "10"    [10]    (10,)    {10}    {'a': 10}    True
#
# My guesses:
# 10 = int
# 10.0 = float
# "10" = str
# [10] = list
# (10,) = tuple
# {10} = set
# {'a': 10} = dict
# True = bool

print("Question 12: PREDICT the data type of each value below, then check with type():")
print("10 =", type(10))
print("10.0 =", type(10.0))
print('"10" =', type("10"))
print("[10] =", type([10]))
print("(10,) =", type((10,)))
print("{10} =", type({10}))
print("{'a': 10} =", type({'a': 10}))
print("True =", type(True))
print()


# 13. PREDICT: What is the data type of stdMidterm + stdFinal?
# My guess: float

print("Question 13: PREDICT: What is the data type of stdMidterm + stdFinal?")
print("My guess: float")
print()

print("stdMidterm =", stdMidterm, ", type =", type(stdMidterm))
print("stdFinal =", stdFinal, ", type =", type(stdFinal))
print()

print("Calculation:", stdMidterm, "+", stdFinal, "=", stdMidterm + stdFinal)
print("Result type =", type(stdMidterm + stdFinal))
print()

print("Explanation:")
print("stdMidterm is an integer (int) with a value of 80.")
print("stdFinal is a floating-point number (float) with a value of 98.5.")
print("When Python adds an int and a float, the result is a float.")
print("Therefore, 80 + 98.5 = 178.5, and 178.5 is a float.")
print()


# 14. PREDICT: What is the data type of stdMidterm / 2?
# My guess: float because division using / returns a float.

print("Question 14: PREDICT: What is the data type of stdMidterm / 2?")
print("My guess: float because division using / returns a float.")
print()

print("stdMidterm =", stdMidterm, ", type =", type(stdMidterm))
print("Calculation:", stdMidterm, "/", 2, "=", stdMidterm / 2)
print("Result type =", type(stdMidterm / 2))
print()

print("Explanation:")
print("/ is called the division operator in Python.")
print("The / operator divides one number by another and returns a float.")
print("Even though 80 and 2 are both integers, int / int using / returns a float.")
print("Therefore, 80 / 2 = 40.0, and the result type is float.")
print()


# 15. Fill in the blank so the output is <class 'tuple'>
# print(type(_))

print("Question 15: Fill in the blank so the output is <class 'tuple'>.")
print("Completed code: print(type((1,)))")
print(type((1,)))
print()

print("Explanation:")
print("The blank _ is replaced with (1,).")
print("(1,) is a tuple containing one item.")
print("The comma is what makes a single item a tuple.")
print("(1) is an integer, but (1,) is a tuple.")
print()


# BONUS: Why does print(type((1))) show <class 'int'> and not <class 'tuple'>?
# Answer: Parentheses by themselves do not create a tuple.
# A one-item tuple needs a comma, for example: (1,)

print("BONUS: Why does print(type((1))) show <class 'int'> and not <class 'tuple'>?")
print()

print("Without comma: print(type((1)))")
print("Output:", type((1)))
print()

print("With comma: print(type((1,)))")
print("Output:", type((1,)))
print()

print("Explanation:")
print("(1) is the integer 1 placed inside parentheses, so its data type is int.")
print("(1,) contains a comma, which makes it a one-item tuple.")
print("For a tuple with only one item, the comma is required.")
print()

print("Easy way to remember:")
print("(1)  = int")
print("(1,) = tuple")
print()