# Exercise 1: Write a program to read through a file and print the 
# contents of the file (line by line) all in upper case.

file = open('mbox-short.txt')
for line in file:
    line1 = line.rstrip()
    line1 = line.upper()
    print(line1)
