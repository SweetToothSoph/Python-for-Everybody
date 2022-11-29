# Exercise 3: Sometimes when programmers get bored or want to have a bit of fun, they add a harmless 
# Easter Egg to their program. Modify the program that prompts the user for the file name so that it prints a
# funny message when the user types in the exact file name “na na boo boo”. The program should behave 
# normally for all other files which exist and don’t exist.

fname = input('Enter the file name: ')

try:
    fhand = open(fname)
    # this line of code is the danger code
    count = 0
    for line in fhand:
        if line.startswith('Subject: ') :
            count = count + 1

except:
    if fname == 'NA NA BOO BOO' :
        print('NA NA BOO BOO TO YOU - Use a proper file name!')
        quit()
    # At fist I put this line of code above in try but it also printed the
    # except section so this needed to be in this section to print properly
    print('File cannot be opened:',fname)
    quit()

print('There were', count, 'subject lines in', fname)
