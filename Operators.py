#Arithmatic Calculation (+,-,*,**,/,//)
num1=10
num2=3
sum=num1+num2 #same applies for *,-,/
print("the sum is ",sum)
pow=num1**num2 # It powers the given variable
print(f"The power is {pow}")
num3=num1//num2 # It shows only finite number
print("The Answer is",num3)

# Comparision operator (<,>,<=,>=,==,!=,)
print(num1>num2)
print(num1<=num2)
print(num1!=num2)
print(num1==10)

#Assignment Operator (=,+=,-=,*=,/=)
i=1
i+=2  #Replacement for i=i+2
print(i)

# Logical Operator (and,or,not)
print(num1>num2 and num1==num2)
print(num1>=10 and num2<=5)
print(num1>num2 or num2>num1)
print(num1>20 or num2>20)
print(not num1>num2)