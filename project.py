#The British College
#Fundamentals of Data Science Level 3

#Assignment 1

'''1. Write a program which will find all such numbers that are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers should be printed on the output screen.
(Bonus point if you can print all the numbers on a single line)


a=[ i for i in range(2000,3201) if i%7==0 and i%5!=0]
print(*a, sep=',')
'''
'''2. Write a program that can compute the factorial of a given number. The number whose factorial is to be computed is input from the keyboard.
(Hint: Factorial of 3, also written as 3! = 3 X 2 X 1. Similarly, 5! = 5 X 4 X 3 X 2 X 1 )

num = int(input("Enter a number whose factorial is to be found: "))    
factorial = 1    
if num < 0:    
   print(" Factorial does not exist for negative numbers")    
elif num == 0:    
   print("The factorial of 0 is 1")    
else:    
   for i in range(1,num + 1):    
       factorial = factorial*i    
   print("The factorial of",num,"is",factorial)   
'''
'''3. With a program to take as an input an integer number n, and generate a dictionary that contains (i, i*i) where “i” lies between 1 and n (both included). The program should then print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

number = int(input("Type a number: "))
numberDict = {}
for i in range(1, number+1):
    numberDict[i] = i*i

print(numberDict)
'''
'''4. Write a program that can accept two strings as input and print the string with maximum length as an output. If two strings have the same length, then the program should print both the strings.

a=input('Enter first string :')
b=input('Enter second string :')
if len(a)>len(b):
    print(a)
elif len(b)>len(a):
    print(b)
else:
print(a,b)
'''
'''5.Write a program which can produce a dictionary where the keys are numbers between 1 and 20 (both included) and the values are the square of keys. The program should print the values only.

l=int(input("Enter the Limit : "))
d = dict()
for x in range(1,l+1):
    d[x]=x**2
print(d)
'''
'''6.Write a program which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

def printValues():
    l = list()
    for i in range(1, 21):
        l.append(i**2)
    print(l)

printValues() 
'''
'''7.Write a program which can generate a list where the values are square of numbers between 1 and 20 (inclusive). The program should only print the last 5 elements of the list.

def square():
    l = list()
    for i in range(1, 21):
        l.append(i**2)
    print(l[:5])

square()
'''
'''8. Write a program to convert Celsius (C) values into Fahrenheit (F). The program should ask for Celsius value from the user and print the Fahrenheit value as an output.
Formula to Convert Celsius o Fahrenheit: [ F = C * ( 9 / 5 ) + 32 ]

C=float(input('Enter value in Celsius:'))
F=C*(9/5)+32
print('The value in Fahrenheit is', F)
'''
'''9. Write a program which accepts a string as input from the keyboard. If the input string is "even" or "EVEN" or "Even", print the even numbers from the list (my_numbers) given below. If the string is "odd" or "ODD" or "Odd", print the odd numbers from the list. Otherwise simply print “Unknown Input!”

my_numbers = [7, 2, 4, 11, 19, 24, 66, 1, 42, 22, 37, 5, 3, 92, 73]

my_numbers=[7,2,4,11,19,24,66,1,42,22,37,5,3,92,73]

input_str=input("Enter 'even' or 'odd':").lower()

if input_str=='even':
    print("even numbers:")
    for num in my_numbers:
        if num % 2==0:
            print(num)
            
elif input_str=='odd':
    print("odd numbers")
    for num in my_numbers:
        if num % 2 !=0:
            print(num)
else:
    print('unknown input')
'''
'''10. Write a program that prints the numbers from 1 to 20. But for multiples of three print “Fizz” instead of
the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and
five print “Fizz Buzz”.

x=1
for i in range(1,21):
    if i%3==0 and i%5!=0:
        print("Buzz")
    elif i%5==0 and i%3!=0:
        print("Fizz")
    elif i%3==0 and i%5==0:
        print("Buzz Fizz")
    else:
        print(i)
'''
