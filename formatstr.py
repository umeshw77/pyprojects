# Different types of string formatting that python supports

# Python2

s1 = "Welcome to Hogwarts, %s" % "Harry"
print(s1)

# Python2.6

s2 = "{} pill or {} pill?".format("Blue", "Red")
print(s2)

# formatter with positional and keyword arguments
# positional
s3 = "The answer to {0}, the {1}, and Everything".format("Life", "Universe")
# keyword
s4 = "The Hitchhiker's guide to the {space}".format(space="galaxy")

print(s3)
print(s4)

# One can also use ** to do the neat trick with dictionaries
actions = {"action1": "sow", "action2": "reap"}
print("As you {action1}, so you {action2}".format(**actions))

# New style - f-strings (aka formatted string literals)
# Since Python 3.6
# This is simple and less verbose syntax
date = "future"
name = "George"
s = f"Welcome to the {date}, {name}"
print(s)

# Compare with str.format() syntax which is more verbose
s = "Welcome to the {d}, {n}".format(d=date, n=name)
print(s)

# f-strings can take any valid python expressions
print(f"{2 * 10}")


# You can also call functions
def to_lowercase(input):
    return input.lower()


name = "Eric Idle"
print(f"{to_lowercase(name)} is funny")
# Or call method directly
print(f"{name.lower()} is funny")
