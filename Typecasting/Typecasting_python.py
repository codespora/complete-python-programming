'''
Hello and welcome back to this tutorial.In this lesson, we will learn about the important typecasting concept in Python Programming Language.
Typecasting refers to a technique used to modify the values (or variables) declared in a given datatype into a different datatype. In the Python Programming
Language, this is attained by using what is known as inbuilt constructor functions.Inbuilt means that you do not need to program. It is already programmed for you.
The functions are int(), string(), float(). There are several functions. However, in this lesson we will only stick to these 3 important methods.
There is implicit and explicit typecasting. We will focus on the latter as implicit typecasting happens by default when you program.
'''

'''we will begin by concurrently learning both the the int() and float typecasting method
Let's begin by defining a float datatype variable and convert that into an int type.
'''

x = 1.5
#print x to ascertain that x variable was assigned to 1.5
print(x)
#Now, let's check the datatype of x, using a combination of the str() and type() function. The str() as shall be described later, changes our value to a string value.
print("The datatype of x is " + str(type(x)))
#Now, let's change x (which as can be evinced from the print function) above is float to int type. In order to do this, we have to invoke the int() method

y = int(x)
print(y)
#By printing you notice that the initial 1.5 stored as x variable is now 1. This is because 1.5 is float while 1 is int.
print("The datatype of y is " + str(type(y)))

'''Utilizing the float() method, you can change a defined value into float. In this scenario, we define a value as an integer and then change that to a float type '''
a = 20

print(a)
print("The datatype of a is " + str(type(a)))
#as shown in the above print function, a is of the int class. Now we will convert that to float type and store that in a new variable
b = float(a)
print(b)
print("The datatype of b is " + str(type(b)))

'''utilizing the float b value that is defined above, we hereby indicate that this value type can be changed to string type using the str() and store that in a variable called c
and later on print c to check for its type'''
c = str(b)
print(c)
print("The datatype of c is " + str(type(c)))

'''The same holds true for any other inter-method conversion. This means that using these functions, you can change from string type to integer type to float type & vice versa. 
That is the end for today's class on typecasting. We will meet in the next class'''

