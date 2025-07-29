num1=int(input('Enter a Number: '))
found = False
for i in range (num1):
    if i**2 == num1:
        print(f'{i} is the square of {num1}.')
        found=True
        break
if found == False:
    print(f'{num1} is not square of any number.')