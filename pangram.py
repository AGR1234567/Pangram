x = input('Enter a long number: ')
digits = {'1':0, '2':0, '3':0, '4':0, '5':0, '6':0, '7':0, '8':0, '9':0, '0':0, }

for i in x:
    if i in digits:
        digits[i] += 1

pangram = True

for i in digits.values():
    if i == 0:
        pangram = False

if pangram:
    print('The number entered is a pangram')
else:
    print('The number entered is not a pangram')