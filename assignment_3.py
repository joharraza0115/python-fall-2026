# Assignment #3 has four main parts

# Part A: Numbers

# int, float, complex
# scientific notation like 35e3
# random numbers

# Part B: Casting

# converting between str, int, and float
# understanding why some conversions work and others fail

# Part C: Strings

# indexes
# slicing
# .upper() / .lower()
# .strip()
# .replace()
# .split()
# f-strings
# escape characters
# in

# Part D: Booleans

# True and False
# understanding truthy/falsy values
# bool()
# isinstance()

# And then the bonus:

# Python
# stdName[::-1]

# for reversing the name.


print("\n============================================================")
print("Assignment #3 - Numbers, Casting, Strings & Booleans")
print("Topics: W3Schools > Python Numbers, Python Casting,")
print("                    Python Strings, Python Booleans")
print("============================================================")
print()

stdCode = 34551001
stdName = 'Mohammed'
stdLastname = 'Ali'
stdMidterm = 80
stdFinal = 98.5
stdCity = '  Alexandria  '
stdEmail = 'mohammed.ali@school.edu'
stdPhone = '555-0142'
stdComment = ''


# ---------------- PART A: NUMBERS ----------------


# 1. Create these three variables and print the type of each:
#    a = 12      b = 12.0      c = 12 + 3j

print("\nQuestion 1: Create a = 12, b = 12.0, and c = 12 + 3j and print the type of each.")

a = 12
b = 12.0
c = 12 + 3j

print("a =", a, ", a type =", type(a))
print("b =", b, ", b type =", type(b))
print("c =", c, ", c type =", type(c))
print()

print("Explanation:")
print("12 is a whole number, so its type is int.")
print("12.0 contains a decimal point, so its type is float.")
print("12 + 3j contains an imaginary part using j, so its type is complex.")
print()


# 2. PREDICT: What is the type of x = 35e3 ? What value will print(x) show?
# My guess: The type will be float and the value will be 35000.0.

print("Question 2: PREDICT: What is the type of x = 35e3? What value will print(x) show?")
print("My guess: The type will be float and the value will be 35000.0.")

x = 35e3

print("x =", x)
print("x type =", type(x))
print()

print("Explanation:")
print("35e3 is scientific notation.")
print("The e means multiply by 10 raised to a power.")
print("35e3 means 35 * 1000, which equals 35000.0.")
print("Python represents this scientific notation value as a float.")
print()


# 3. Import the random module and print a random number between 1 and 10.
#    (Hint: random.randrange(1, 11))

print("Question 3: Import the random module and print a random number between 1 and 10.")

import random

randomNumber = random.randrange(1, 11)

print("Random number =", randomNumber)
print()

print("Explanation:")
print("random is a Python module used to generate random values.")
print("randrange(1, 11) starts at 1 and stops before 11.")
print("Therefore, the possible numbers are 1 through 10.")
print()


# ---------------- PART B: CASTING ----------------


# 4. The number "75" below is a STRING. Cast it to an int, add it to stdMidterm,
#    and print the result.

bonusPoints = "75"

print('Question 4: Cast bonusPoints = "75" to an int, add it to stdMidterm, and print the result.')

print("bonusPoints =", bonusPoints, ", type =", type(bonusPoints))
print("stdMidterm =", stdMidterm, ", type =", type(stdMidterm))
print()

bonusPointsInt = int(bonusPoints)

print("After casting bonusPoints to int:")
print("bonusPointsInt =", bonusPointsInt, ", type =", type(bonusPointsInt))
print("Calculation:", stdMidterm, "+", bonusPointsInt, "=", stdMidterm + bonusPointsInt)
print()

print("Explanation:")
print('The value "75" starts as a string because it is inside quotation marks.')
print("int() casts the string '75' to the integer 75.")
print("After casting, Python can add 75 to stdMidterm.")
print()


# 5. PREDICT: What will each line print?
#    print(int(9.99))
#    print(float(7))
#    print(str(3.0))
#
# My guess:
# int(9.99) will print 9.
# float(7) will print 7.0.
# str(3.0) will print 3.0 as a string.

print("Question 5: PREDICT: What will each casting operation print?")

print("My guess: int(9.99) = 9")
print("My guess: float(7) = 7.0")
print('My guess: str(3.0) = "3.0"')
print()

print("int(9.99) =", int(9.99), ", type =", type(int(9.99)))
print("float(7) =", float(7), ", type =", type(float(7)))
print("str(3.0) =", str(3.0), ", type =", type(str(3.0)))
print()

print("Explanation:")
print("int(9.99) removes the decimal portion and gives 9.")
print("float(7) converts the integer 7 to the float 7.0.")
print('str(3.0) converts the float 3.0 into the string "3.0".')
print()


# 6. Fix this line so it runs without an error (use casting):
#    print('Student code: ' + stdCode)

print("Question 6: Fix print('Student code: ' + stdCode) so it runs without an error.")

print("Fixed code: print('Student code: ' + str(stdCode))")
print('Student code: ' + str(stdCode))
print()

print("Explanation:")
print("stdCode is an int, but 'Student code: ' is a string.")
print("str(stdCode) casts the integer into a string.")
print("After both values are strings, they can be joined using +.")
print()


# 7. PREDICT: What happens when you run print(int('12.5'))?
#    Try it, then write a line that correctly turns '12.5' into the int 12.
# My guess: int('12.5') will give an error because '12.5' contains a decimal point.

print("Question 7: PREDICT: What happens with int('12.5')?")
print("My guess: It will give an error because the string contains a decimal point.")
print()

print("Correct conversion:")
print("int(float('12.5')) =", int(float('12.5')))
print()

print("Explanation:")
print("The string '12.5' cannot be converted directly to an int.")
print("First, float('12.5') converts the string to the float 12.5.")
print("Then, int(12.5) converts the float to the integer 12.")
print()


# ---------------- PART C: STRINGS ----------------


# 8. Print the first letter of stdName, and the LAST letter of stdName
#    (use a negative index for the last letter).

print("Question 8: Print the first and last letter of stdName.")

print("stdName =", stdName)
print("First letter stdName[0] =", stdName[0])
print("Last letter stdName[-1] =", stdName[-1])
print()

print("Explanation:")
print("Index 0 represents the first character.")
print("Index -1 represents the last character.")
print()


# 9. Use slicing to print only 'Moh' from stdName.

print("Question 9: Use slicing to print only 'Moh' from stdName.")

print("stdName =", stdName)
print("stdName[0:3] =", stdName[0:3])
print()

print("Explanation:")
print("Slicing uses [start:stop].")
print("The starting index is included, but the stopping index is not included.")
print("stdName[0:3] uses indexes 0, 1, and 2, which gives 'Moh'.")
print()


# 10. Print stdName in all UPPERCASE and stdLastname in all lowercase.

print("Question 10: Print stdName in uppercase and stdLastname in lowercase.")

print("stdName uppercase =", stdName.upper())
print("stdLastname lowercase =", stdLastname.lower())
print()

print("Explanation:")
print("upper() converts letters to uppercase.")
print("lower() converts letters to lowercase.")
print()


# 11. stdCity has extra spaces. Print it with the spaces removed using strip().
#     Then print len() of stdCity before and after strip().

print("Question 11: Remove the extra spaces from stdCity using strip().")

print("Before strip: |" + stdCity + "|")
print("Length before strip =", len(stdCity))
print()

cleanCity = stdCity.strip()

print("After strip:  |" + cleanCity + "|")
print("Length after strip =", len(cleanCity))
print()

print("Explanation:")
print("strip() removes leading and trailing spaces.")
print("The | characters make the spaces easier to see.")
print("strip() does not remove characters from the middle of the string.")
print()


# 12. Use replace() to change the '-' in stdPhone to a space and print it.

print("Question 12: Use replace() to change '-' in stdPhone to a space.")

print("Original phone =", stdPhone)

updatedPhone = stdPhone.replace("-", " ")

print("Updated phone =", updatedPhone)
print()

print("Explanation:")
print("replace() replaces one part of a string with another.")
print("Here, '-' is replaced with a space.")
print()


# 13. Use split() to separate stdEmail at the '@' and print the result.
#     PREDICT: What data type does split() return?
# My guess: split() will return a list.

print("Question 13: Split stdEmail at the '@' delimiter.")
print("My guess: split() will return a list.")
print()

emailParts = stdEmail.split("@")

print("stdEmail =", stdEmail)
print("split('@') =", emailParts)
print("Data type =", type(emailParts))
print()

print("Explanation:")
print("@ is the delimiter, or separator.")
print("split('@') breaks the string wherever it finds @.")
print("split() returns the separated pieces inside a list.")
print()


# 14. Use an f-string to print exactly:
#     Mohammed Ali scored 98.5 on the final.

print("Question 14: Use an f-string to print the student's final score.")

print(f"{stdName} {stdLastname} scored {stdFinal} on the final.")
print()

print("Explanation:")
print("An f-string starts with the letter f before the quotation marks.")
print("Variables inside { } are inserted into the string.")
print()


# 15. Use an f-string with a format specifier to print the average of
#     stdMidterm and stdFinal with exactly 2 decimal places.
#     Expected output: Average: 89.25

print("Question 15: Print the average with exactly 2 decimal places.")

average = (stdMidterm + stdFinal) / 2

print("Calculation:", "(", stdMidterm, "+", stdFinal, ") / 2 =", average)
print(f"Average: {average:.2f}")
print()

print("Explanation:")
print("The average is calculated by adding the two scores and dividing by 2.")
print(":.2f formats the number as a float with exactly 2 decimal places.")
print()


# 16. Print this sentence using an escape character for the quotes:
#     The teacher said "Great job!" to Mohammed.

print('Question 16: Print the sentence using escape characters for the quotes.')

print("The teacher said \"Great job!\" to Mohammed.")
print()

print("Explanation:")
print("The backslash before a quotation mark is an escape character.")
print('It allows quotation marks to appear inside a string that also uses double quotes.')
print()


# 17. Use the in keyword to check if 'school' is in stdEmail. Print the result.

print("Question 17: Check if 'school' is in stdEmail.")

print("stdEmail =", stdEmail)
print("'school' in stdEmail =", 'school' in stdEmail)
print()

print("Explanation:")
print("The in keyword checks whether a value exists inside another value.")
print("Because 'school' appears in the email address, the result is True.")
print()


# ---------------- PART D: BOOLEANS ----------------


# 18. PREDICT True or False for each, then check with bool():
#     bool(0)   bool(15)   bool("")   bool("False")   bool([])   bool(None)
#
# My guesses:
# bool(0) = False
# bool(15) = True
# bool("") = False
# bool("False") = True
# bool([]) = False
# bool(None) = False

print("Question 18: PREDICT True or False for each value.")

print("bool(0) =", bool(0))
print("bool(15) =", bool(15))
print('bool("") =', bool(""))
print('bool("False") =', bool("False"))
print("bool([]) =", bool([]))
print("bool(None) =", bool(None))
print()

print("Explanation:")
print("0 is False.")
print("A non-zero number such as 15 is True.")
print("An empty string is False.")
print('"False" is True because it is a non-empty string; it is text, not the Boolean value False.')
print("An empty list is False.")
print("None is False.")
print()


# 19. Print the result of bool(stdComment). Then explain in a comment
#     why it gives that answer.

# stdComment is an empty string, and empty strings evaluate to False.

print("Question 19: Print the result of bool(stdComment).")

print("stdComment =", repr(stdComment))
print("bool(stdComment) =", bool(stdComment))
print()

print("Explanation:")
print("stdComment is an empty string.")
print("An empty string evaluates to False when passed to bool().")
print()


# 20. Use isinstance() to check if stdFinal is a float. Print the result.

print("Question 20: Use isinstance() to check if stdFinal is a float.")

print("stdFinal =", stdFinal)
print("stdFinal type =", type(stdFinal))
print("isinstance(stdFinal, float) =", isinstance(stdFinal, float))
print()

print("Explanation:")
print("isinstance() checks whether a value belongs to a particular data type.")
print("stdFinal contains 98.5, which is a float, so the result is True.")
print()


# BONUS: Print stdName backwards ('demmahoM') using slicing.
# Hint: [::-1]

print("BONUS: Print stdName backwards using slicing.")

print("stdName =", stdName)
print("stdName[::-1] =", stdName[::-1])
print()

print("Explanation:")
print("[::-1] slices through the entire string with a step of -1.")
print("A step of -1 reads the characters in reverse order.")
print("Therefore, Mohammed becomes demmahoM.")
print()