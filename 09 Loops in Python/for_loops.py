'''
    Hello guys, welcome back.
    In this section, we’re going to learning about loops in Python, especially For-loop.

    A for loop is used to repeat a set of the code a number of times.

    Let’s get started, by seeing how we are going to print out elements inside a list.

    The first thing we need to understand is what is the syntax of a for a loop. For loop in Python has a slightly 
    different way of writing compare to other programming languages, if you are coming from a different programming language.

    Python’s for loop looks like this:
    for <var> in <iterable>:
        <statement>

    <var> takes on the value of the next element in <iterable> each time through the loop.
    <iterable> is a collection of objects—for example, a list or tuple. The <statement(s)> in the loop body are denoted by indentation

    As we learned Lists in lecture seven. Let’s start with a names list, and add some names and then we would create our first for loop.
'''

names = ['Abdi', 'Farah', 'Fartun', 'Asha']

'''
    What we want to do is, we want to print the names in the list we defined.
    We’ll start by saying “for”, which is the keyword that signals, we want t to start a for a loop. Then we’ll do “name” in “names”, print “name”.
'''

for name in names:
    print(name)

'''
    Each time through the loop, “name” takes on a successive item in the “names” list, 
    so print() displays the values 'Abdi', Farah', and 'Fartun', 'Asha', respectively.
'''

'''
    Let’s do another example, print out numbers from 1 to 10. Since we want to print out a list of numbers from 1 to 10, 
    what we are going to do here is to use the range function.
'''

for item in range(1, 11):
    print(item)

'''
    The range takes two values, the starting number, and the ending number. Here we need to specify the starting number as 1 and give a coma and 
    specify the ending number as 11. What we want to do inside the loop is print print out “item”, So what this is going to do is that it’s 
    going to take the value of item and it’s going to print it out. As long as this loop continues to execute.
'''

'''
    Let’s say we want to do multiplication in our list and print out values. So what would be the expected outputs, 
    if our list looks like this [1, 2, 3, 4, 5], the output should be [2, 4, 6, 8, 10], we just multiplying by 2. 
    
    How can we do that?

    So we need to find a way to access the items on the list and we know already how to access using indexes from our previous lecture.
'''

number_list = [1, 2, 3, 4, 5]

'''
    So if we want the first one we use zero indexes to access it. So, number_list[0] will print out 1, we just want to multiply that by 2. 
    We keep doing until we access all the items on the list and multiply by 2.
'''
number_list[0] # 1
number_list[1] # 2
number_list[2] # 3
number_list[3] # 4
number_list[4] # 5

'''
    Imagine having 1000 items on the list, we did end up with 1000 lines of code. That would be a lot of repeating, 
    a good programmer always tries to minimize the repetition. How can we do this with just two lines of code instead, well how about for loop.

    Here, we just choose a name for a variable for number_lists, let’s call items in our number_lists. 
    All we have to do now is print out the item by multiplying by 2.
'''

for item in number_list:
    print(item * 2)

'''
    That’s it for this lecture, with this knowledge and more we’re going to be able to create very useful projects soon. 
    So thanks for sticking with me, hope you’ve enjoyed it and I’ll see you in the next lecture.
'''