# Exercise 3: Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error message. If the score is between 0.0 and 1.0, 
# print a grade using the following table:
# Score Grade:
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F

sc = input("Enter Score: ")

# Needed to put the score in a float to it can give it its proper value
# Putting float in try statement will give correct error message when anything
# other than a valid score is entered
try:
    sf = float(sc)
except:
    print("Bad score")
    quit()

# The following code I found online, I did not figure it out
# elif is used when there are multiple decisions
# you must state a if first, then elif with print

if sf > 1.0:
    print("Bad score")
elif sf >= 0.9:
    print("A")
elif sf  >= 0.8:
    print("B")
elif sf  >= 0.7:
    print("C")
elif sf  >= 0.6:
    print("D")
elif sf  < 0.6:
    print("F")
