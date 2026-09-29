# Assignment #1

# Store the student's code (ID number) in a variable
stdCode = 34551001

# Store the student's midterm exam grade
stdMidterm = 80

# Store the student's final exam grade
stdFinal = 98

# Store the student's first name
stdName = 'Mohammed'

# Store the student's last name
stdLastname = 'Ali'


# 1.
# Print the student's full name and student code.
# str(stdCode) converts the number into text so it can be joined with the string.
print('Student Name: Mohammed Ali - Student Code: ' + str(stdCode))


# 2.
# Print the student's final grade.
# Again, str() converts the number to text.
print('Student Grade Final: ' + str(stdFinal))


# 3.
# Print the student's first and last name.
# Python automatically puts a space between them.
print(stdName, stdLastname)


# 4.
# This line is commented out and does not run.
# If it were executed, it would cause an error because
# stdFinal is a number and stdLastname is text.
# Python cannot add a number and a string together.
# print(stdFinal + ' ' + stdLastname)


# 5.
# Compare the final grade and midterm grade.
# == means "is equal to?"
# 98 == 80 is False.
print(stdFinal == stdMidterm)


# 6.
# != means "not equal to"
# 98 != 80 is True.
print(stdFinal != stdMidterm)


# 7.
# Calculate the average of midterm and final grades.
# (80 + 98) / 2 = 89.0
# str() converts the result into text for printing.
print('Average (Midterm and Final) is: ' + str((stdMidterm + stdFinal) / 2))


# 8.
# Change the student code from 34551001 to 1.
stdCode = 1

# Print the updated student code.
print('New Student Code:', stdCode)


# 10.
# This is a logical expression using NOT, OR, and AND.
#
# stdName == 'Ayesha'
# Mohammed == Ayesha → False
#
# not(False) → True
#
# stdFinal > stdMidterm
# 98 > 80 → True
#
# True or True → True
#
# stdMidterm != stdFinal
# 80 != 98 → True
#
# True and True → True
print((not (stdName == 'Ayesha') or (stdFinal > stdMidterm)) and (stdMidterm != stdFinal))


# 11.
# Convert stdCode to text and check if '345' exists in it.
# stdCode is now 1, so '345' is not found.
# Result = False
print('345' in str(stdCode))


# 12.
# Check if '345' does NOT exist in stdCode.
# Since stdCode is now 1, '345' is not there.
# Result = True
print('345' not in str(stdCode))


# 13.
# Multiplication happens first:
# 5 * 2 = 10
#
# Then modulus (%) finds the remainder:
# 10 % 5 = 0
print(5 * 2 % 5)


# 14.
# Print the final exam grade.
print('Final is : ' + str(stdFinal))


# 15.
# Repeat the string "3" three times.
# Result: 333
print("3" * 3)

# Quick Exam Notes

# ==  Equal to
# !=  Not equal to
# >   Greater than

# Logical Operators
# not -> reverses True/False
# or  -> at least one condition is True
# and -> both conditions must be True

# Membership Operators
# in      -> exists inside
# not in  -> does not exist inside

# Arithmetic
# % -> modulus (remainder)