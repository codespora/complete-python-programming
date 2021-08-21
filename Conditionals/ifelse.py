'''
Hello students. Welcome to this class. In today's lesson, we are going to learn about the concept of conditionals of the Python 
Programming Language. In more simplistic terms, this is known as the if else statements. The use of conditionals is of paramount
importance in programming for the following reason: it provides the programmer with the ability to check conditions and modify
the program's behavior as deemed fit. The most basic unit of conditionals is the if statement, whose general form is as follows:
an if followed by a Boolean expression to be evaluated. If the Boolean expression is not evaluated, then the statements under the 
"else" are evaluated instead. 

if BOOLEAN EXPRESSION:  
	STATEMENTS 1
else:
	STATEMENTS 2

''' 

#Let's start with a simple example of an if else statement

name = "Ali" #here we define a name of a student called
if name == "Ali":
	print("My name is Ali and I am a student of Codespora")
else:
	print("My name is Halimo and I would like to be a classmate of Ali") 

'''
As you can see from the above code, since the Boolean expression that follows the if statement evaluates to true, the block statement i.e 
"My name is Ali and I am a student of Codespora" is executed and hence printed out. The else section of the code is ignored as the if part 
of the code block evaluates to true. Note that == and = convey a different meaning in programming logic. Whereas == implies an evaluation of 
equality, the latter, =, is used to assign values to a variable. For instance, 1==1 (means 1 is equal to 1 and thus is true), 1==2 (indicates
that 1 is equal to 2 and hence false). On the other hand, a=1 (does not mean that a is equal to 1. Rather, the variable a is assigned to the value
of 1).

''' 
#In this example, 

