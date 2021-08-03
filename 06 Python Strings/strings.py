'''
    Hello guys, welcome back.
    In this video, we’re going to learning about Strings in Python.


    Very often in your programming life, you will deal with text, 
    mainly the user will be giving some text that we want to do something with.

    In Python, we have a datatype called strings, which are used to contain text like characters, symbols, or even numbers. 

    Let’s define a string in Python. Here’s our first string, let’s called it “full_name” and assign a value to it, “Abdi Ali”. 
'''

full_name = "Abdi Ali"


'''
    As you can see we surrounded this string with double quotations marks. You can also use single quotations mark. 
    It’s important that it starts and ends with quotation marks that match, here again, we use double quotes but that’s just me.

    This string here contains the characters A, B, D, I, and A, L, I including space as well.

    NOTE - When we run the program, Python looks at this string, it knows nothing about it because 
    the string doesn’t have any meaning, all it is used for is to carry these characters.
'''

'''
    Let’s define a string with the value of “It’s me, Abdi Ali”
'''

name = "it’s me, Abdi Ali"

'''
    Here, we definitely want to use the double quotation marks on the outside, because we have a single quotation mark on the inside.

    Similarly, we may want to use the single quotation marks on the outside and the double quotation marks on the inside.

    Let’s define a string with the value of ‘He replied, "I left the keys in the car." yesterday.’ 
    Here we are dealing with the correct string type, so we can put whatever we want inside.
'''

single_quotes_outside = 'He replied, "I left the keys in the car." yesterday'

'''
    Let’s switch this into a double quotation mark string. We can put double quotation marks at the beginning and at the end and 
    put a backslash in front of these quotes. When you do this, is called escaping and it’s quite a common thing to do.
'''

double_quotes_outside = "He replied, \"I left the keys in the car.\" yesterday"


'''
    Let’s say we have a longer text we want to assign a variable to it. 
    We’ll define a variable called longer_text and here we are gonna use three quotations marks and put 
    whatever text we want inside. Once we print it out.
'''

longer_text = """Hello,
Abdi Ali

"""

'''
    We’ll see that we got multiple lines printed out.

    Multiline strings are very useful when you have much longer text you working with.
'''

'''
    What if we want to assign each variable to a string and add them together.
    Let’s define the first_name and last_name plus greeting variable and assign values to it.
    We can join them and makeup one final string.
'''

first_name = "Abid"
last_name = "Ali"
greet = "Hello, " + first_name + last_name
print(greet)

'''
    NOTE. We cannot add integers and strings together. We must convert to string first before we can add them together. 
    Converting to string is very easy. We can either add the quotation marks around it or we can use the str function and 
    pass it the value inside, don’t worry str is a function, we’ll go cover more on this later.
'''
# this will give us error
age = 23
name = "Abdi Ali"

final_string = name + "is" + age + "years old"
print(name)

# this will work
final_string = name + "is" + str(age) + "years old"
print(name)

'''
    Let’s use string formatting, to accomplish much faster and more readable.
    We’re going to add F-string to the beginning of our double-quotes. 
    F-string is only something available in Python 3.6 and above. Let’s add some string and then inside a couple of curly braces,
    we’re going to add our variable “age” inside curly braces.
'''
age = 23
final_string = f"Abdi Ali is {age} years old"
print(final_string)

'''
    Let’s assign a new value to age and if that changes something when we print out. 
    Although we change the age, the final_string doesn’t change.
'''
age = 24
print(final_string)

'''
    If we want the new value to affect our final_string, we’ll need to use formatting strings, 
    which do allow for the changing of variables.

    Let’s define a new variable called the “final_string” and then just opening and closing curly braces with the 
    name of the variable inside. We can define another variable called “abdi_string” and add dot format and pass in the age.
'''
age = 23
final_string = "Abdi Ali is {} years old"
print(final_string.format(age))

'''
    Now, if we change the age to a new value and dot format and print out, it’ll have different values than before.
'''
age = 24
print(final_string.format(age))

'''
    Converting data types and string formatting is very common in Python, we’ll learning more about these upcoming lectures. 
    
    But for now, that’s it for this video. Join us in our Facebook community, the link is on the description. I’ll see you next one. 
'''