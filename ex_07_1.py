file = open('mbox-short.txt')
for line in file:
    line1 = line.rstrip()
    line1 = line.upper()
    print(line1)
