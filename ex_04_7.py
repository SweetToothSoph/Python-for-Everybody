# Exercise 7: Rewrite the grade program from the previous chapter using a function called 
# computegrade that takes a score as its parameter and returns a grade as a string.

def computegrade(sf):
    if sf > 1.0:
        print("Bad score")
    elif sf >= 0.9:
        print("A")
    elif sf >= 0.8:
        print("B")
    elif sf >= 0.7:
        print("C")
    elif sf >= 0.6:
        print("D")
    elif sf < 0.6:
        print("F")

sc = input("Enter Score: ")

try:
    sf = float(sc)
except:
    print("Bad score")
    quit()
    
computegrade(sf)
