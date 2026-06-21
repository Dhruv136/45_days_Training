"""
PYTHON OPERATORS

Operators are special symbols used to perform operations on variables and values.

1. ARITHMETIC OPERATORS
   +   Addition
   -   Subtraction
   *   Multiplication
   /   Division
   //  Floor Division
   %   Modulus (Remainder)
   **  Exponentiation (Power)

Example:
"""
a = 10
b = 3

print("Arithmetic Operators")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a // b =", a // b)
print("a % b =", a % b)
print("a ** b =", a ** b)

"""
2. ASSIGNMENT OPERATORS
   =    Assign
   +=   Add and Assign
   -=   Subtract and Assign
   *=   Multiply and Assign
   /=   Divide and Assign
   //=  Floor Divide and Assign
   %=   Modulus and Assign
   **=  Power and Assign
"""

x = 10

x += 5
print("\nAssignment Operators")
print("x += 5 :", x)

x -= 3
print("x -= 3 :", x)

"""
3. COMPARISON (RELATIONAL) OPERATORS
   ==  Equal to
   !=  Not Equal to
   >   Greater than
   <   Less than
   >=  Greater than or Equal to
   <=  Less than or Equal to
"""

print("\nComparison Operators")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

"""
4. LOGICAL OPERATORS
   and  Returns True if both conditions are True
   or   Returns True if at least one condition is True
   not  Reverses the result
"""

p = True
q = False

print("\nLogical Operators")
print("p and q :", p and q)
print("p or q  :", p or q)
print("not p   :", not p)

"""
5. BITWISE OPERATORS
   &   AND
   |   OR
   ^   XOR
   ~   NOT
   <<  Left Shift
   >>  Right Shift
"""

print("\nBitwise Operators")
print("a & b  :", a & b)
print("a | b  :", a | b)
print("a ^ b  :", a ^ b)
print("~a     :", ~a)
print("a << 1 :", a << 1)
print("a >> 1 :", a >> 1)

"""
6. MEMBERSHIP OPERATORS
   in       Checks if value exists in sequence
   not in   Checks if value does not exist in sequence
"""

numbers = [1, 2, 3, 4, 5]

print("\nMembership Operators")
print("3 in numbers     :", 3 in numbers)
print("10 in numbers    :", 10 in numbers)
print("10 not in numbers:", 10 not in numbers)

"""
7. IDENTITY OPERATORS
   is       Returns True if both variables refer to same object
   is not   Returns True if variables refer to different objects
"""

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("\nIdentity Operators")
print("list1 is list2     :", list1 is list2)
print("list1 is list3     :", list1 is list3)
print("list1 is not list3 :", list1 is not list3)

"""
SUMMARY

1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Bitwise Operators
6. Membership Operators
7. Identity Operators

These are the 7 major types of operators in Python.
"""