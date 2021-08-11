'''
    Hello guys, welcome back.
    In this lecture, we’re going to learning about loops in Python, especially While-loop.

    At this point, we have learned about for loop and how it can be used to print out a set of code multiple times.
    While Loop in Python also performs the exact same function but the syntax might be a little bit different. 

    Let’s see how Python’s while statement is used to construct loops.
    while <expr>:
        <statement>

    <statement(s)> represents the block to be repeatedly executed, often referred to as the body of the loop.

    Let’s start by defining a variable called points, and we’ll assign that to 10. We’ll start typing “while” points > 0, 
    we want to remove 1 point from our points and print our points.
'''
points = 10
while points > 0:
    points = points - 1
    print(points)

'''
    Here’s what’s happening in this example:
    points is initially 10. The expression in the while statement header is points > 0, which is true, so the loop body executes. 
    Inside the loop body, points is decremented by 1 to 9 and then printed.

    When the body of the loop has finished, program execution returns to the top of the loop, and the expression is evaluated again. 
    It is still true, so the body executes again, and 8 is printed.

    This continues until points becomes 0. At that point, when the expression is tested, it is false, and the loop terminates.
'''

'''
    For our new example, let get user input and ask user if they still coding. First, we’ll define a variable called user_input and 
    assign that to input. We’ll use a while loop to break the loop based on if the user types “yes” or “no”, here we want to break 
    the loop if they type yes. 
    
    Let’s also have a pointer variable that stores our points and assign that to 10. We to add 10 points to our points if the user is still coding, 
    likewise, we want to remove 5 points if the user is not coding. 
'''
user_input = input("Are you still coding? ")
points = 10
while True:
    if user_input == "yes":
        points = points + 10
        break
    else:
        points = points - 5
        break
    
print("Points: ", points)

'''
    For our last example, we are going to use the while loop to print numbers from 1 to 10. In this case, we’ll need to have a variable that 
    keeps track of the number of times the loop executes.

    Let’s define a variable called “count” and initialize it to 0 because we haven’t executed the while loop yet.

    Next, we’ll say while the count is less than 10. If the condition is true it is going to execute the body statement. 
    Let’s define the body statement. For the body statement, we just need to print out the values of the count itself. 
    We also need to make sure that whenever this loop executes for a single time we need to increment the value of the count by 1.
'''
count = 0
while count < 10:
    count = count + 1
    print(count)