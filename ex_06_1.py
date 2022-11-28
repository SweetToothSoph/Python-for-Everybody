# Exercise 1: Write a while loop that starts at the last character in the string and works its way 
# backwards to the first character in the string, printing each letter on a separate line, except backwards.

fruit = 'watermelon'
# At first I forgot to put the quotes so it was not working
letter = fruit[1]
# This line of code is actually not needed but I will leave it for now
index = -1
# At first I left it at 0 and it added an extra w
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index - 1
    # I had +1 so it was going the correct way I wanted it backwards
    # this line of code is very important, it ensures that the line of code
    # goes through all the letters and then stops, if I remove it, it will
    # just do w forever
