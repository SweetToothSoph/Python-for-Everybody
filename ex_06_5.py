str = 'X-DSPAM-Confidence: 0.8475'

str1 = str.find(':')
print(str1)

str2 = str[str1+2: ]
# print(str2)

value = float(str2)
print(value)

# Above is my first code that I pretty much did on my own
# I modified it (below) according to the teachers but I originally did
# it on my own which I am pretty proud of, but I had forgotten to add float

str = 'X-DSPAM-Confidence: 0.8475'

str1 = str.find(':')
print(str1)

str2 = str[str1+2: ]
print(str2)

value = float(str2)
print(value)
