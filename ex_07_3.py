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
