largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        fnum = int(num)
        if smallest is None or fnum < smallest:
            smallest = fnum
        if largest is None or fnum > largest:
            largest = fnum
    except:
        print('Invalid input')
        continue

print("Maximum is", largest)
print("Minimum is", smallest)

# I am not very proud of myself, I did not actually figure this out
# I found another girls code online and copy-pasted it, her's did run though so
# I did have to fix it some stuff and remove some stuff but still
