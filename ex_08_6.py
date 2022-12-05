numb = []

while True :
    data = input('Enter a number: ')
    if data == 'done' :
        break
    else :
        numb.append(data)

print(numb)
print('Maximum:', max(numb))
print('Minimum:', min(numb))
