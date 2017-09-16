speed = 10 #mph
print('You encountered a police car')
if speed > 50:
    print('You are going too fast.')
else:
    print('Your speed is fine.')

print('Your speed is ' + str(speed))

userAgeStr = raw_input('Enter your age\n>')
age = int(userAgeStr)
print('You are trying to enter a bar')
if age < 18:
    if age <= 15:
        print('Don\'t even try it.')
    else:
        print('Come back in ' + str(18 - age) + ' years')
elif age == 18:
    print('Just old enough')
else:
    print('Come in')
    

some_list = ['apples', 'pizza', 'banana']
if 'pizza' in some_list:
    print('Yay')

first_10_ns = [1,2,3,4,5,6,7,8,9,10]

for entry in first_10_ns:
    print(entry)