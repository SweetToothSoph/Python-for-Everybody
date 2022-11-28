# Exercise 2: Rewrite your pay program using try and except so that your program handles 
# non-numeric input gracefully by printing a message and exiting the program. 

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
# line 4 & 5 are the dangerous line of code
# by added them in try if incorrect input it will run except, if correct
# it will go to the if block
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter numeric input")
# the quit was added b/c the first time we ran the code the except ran
# and then it tried to continue but it got confused on line 15
# the quit stops everything there if except is used b/c data given is not good
    quit()
print(fh, fr)
if fh > 40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:", xp)
