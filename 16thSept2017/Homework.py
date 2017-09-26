numbers = []

for elem in range(1,100):
    if (elem%2 == 0 or elem%3 == 0):
        numbers.append(elem)

print ("Elements divisible by 2 or 3:")
for elem in numbers:
    print(str(elem) + ", ")