# Comparison Operators
# >, >=, <, <=, ==, !=


# in operator - used to check if a value is in sequence

# Logical Operators
# and, or , not

#e.g. if "a" not in "BCIT":

age = 16
stole_a_car = True
class_5 = True

if age >= 16:
    print("In the if block")

    print("drive")
elif stole_a_car: 
    print("You cn drive")
elif class_5:
    print("Class 5")
else:
    print("give up an cry")


print("After the conditional statment")

# Only one block an run (the first one whose condiion evaluates to true)

# Rules of Conditional Statments
# starts with a single mandatory if
# can be followed by multiple (optional) elifs
# can be followed by a single (optional) else

age = 16 
# message = ""

# if age >= 16:
#     message = "Drive"
# else:
#     message = "No drive"

#variable = valueIfTrue if condition else valueIfFalse
message = 'You can drive' if age >= 16 else "You cannont drive"
print("message")



# conbining conditin using and/or

if age >= 16 or stole_a_car or class_5:
    print("You can drive")

if age >= 16 and age <= 100:
    print("You can drive")



# Truth table:

# and
# Chris teaches ACIT 1515 and it is Friday # True
# Chris teaches ACIT 1515 and it is Tuesday # False
# It it Tuesday and Chris teaches ACIT 1515 # False
# Chris is 10 feet tal and it is Tuesday # False

# True and True = True, otherwise F

# Short-Ciruiting - the first condition that evaluates to false in any complex condition using 'and' causes evaluation to stop

# or
# Chris teaches ACIT 1515 and it is Friday # True
# Chris teaches ACIT 1515 and it is Tuesday # True
# It it Tuesday and Chris teaches ACIT 1515 # True
# Chris is 10 feet tal and it is Tuesday # False

# F or F = F, otherwise T

# True and False values
# generally speaking, everything is True in python with the following exceptions:
    # 0 is False
    # None is Flase
    # empty sequence is False


if 2:
    print("The number 2 is True")

if "bcit":
    print("the string bcit is True")

print(bool(2))
print(bool("bcit"))

if (2) == True:
# if 2 == 1:
    print("yes, 2 == True")
else:
    print("no, 2 does not equal True")