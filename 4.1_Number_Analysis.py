'''
NUMBER ANALYSIS PROGRAM
-----------------------
Create a program that asks the user for a number and then analyzes it to determine if it is:
1.) odd or even
2.) positive, negative or zero
3.) inclusively between -100 and +100

A small report will then be printed. Use the following to test your program:

In: 32  
Out:  Test 1: Even
      Test 2: Positive
      Test 3: Inclusive

In: -123  
Out:  Test 1: Odd
      Test 2: Negative
      Test 3: Exclusive
'''

hi=int(input("Hey there!! You are here because you know the reason \n so enter some numbers"))

# Determine if odd or even
if (hi % 2) == 0:
    print(hi , "is Even")
else:
    print(hi , "is Odd")

#Positive, Negative or zero
if hi > 0:
    print("It is Positive")
elif hi < 0:
    print("It is Negative")
else:
    print("Your number is a zero")

if hi>=-100 and hi <= 100:
    print("Inclusive")
else:
    print("Exclusive")