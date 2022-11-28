fruit = 'watermelon'
# At first I forgot to put the quotes so it was not working
letter = fruit[1]
# This line of code is actually not needed but I will leave it for now
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
    # this line of code is very important, it ensures that the line of code
    # goes through all the letters and then stops, if I remove it, it will
    # just do w forever
