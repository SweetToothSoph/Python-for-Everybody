# Write a function called chop that takes a list and modifies it, removing the first and last elements, 
# and returns None. Then write a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

def chop(numb) :
    del numb[0]
    del numb[-1]

def middle(new_test2) :
    return new_test2[1:-1]

test1 = [1, 2, 3, 4, 5]
# print(test1)
test2 = [6, 7, 8, 9, 10]
# print(test2)

chop_numb = chop(test1)
print(test1)
print(chop_numb)

middle_new_test2 = middle(test2)
print(middle_new_test2)
print(test2)
