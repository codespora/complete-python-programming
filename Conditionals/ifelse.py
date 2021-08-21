'''
Hello students. Welcome to this class. In today's lesson, we are going to learn about the concept of conditionals of the Python 
Programming Language. In more simplistic terms, this is known as the if else statements. The use of conditionals is of paramount
importance in programming for the following reason: it provides the programmer with the ability to check conditions and modify
the program's behavior as deemed fit. The most basic unit of conditionals is the if statement, whose general form is as follows:
an if followed by a Boolean expression to be evaluated. If the Boolean expression is not evaluated, then the statements under the 
"else" are evaluated instead. Notice that the else is optional in programming but it is useful to use in certain scenarios.

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
#In this example, we will elaborate on a case in which the if part of the ifelse control flow is ignored. Instead, the else part will be executed

students = ["Mohamed", "Suleiman", "Abdullahi", "Farah", "Amina", "Farhia", "Ubah"]
if "Sahra" in students:               #this checks if Sahra is one of the students in the above list. 
	print("Sahra is a hardworking student") #since Sahra is not in the list, this print statement will be ignored. The else part will be evaluated

else:
	print("Sahra is not one of the students enrolled here") #this one is printed out.

'''Finally, we will study the elif statement. Just like the else statement, the elif statement is not mandatory i.e it is optional in usage.
The main difference between else and elif statements is that for else statements, there can be at most one else statement that follows an if
statement. On the contrary, there can be an arbitrary number of elif statements that follow the if statement. The following is a programming
syntax that includes the elif statement:

if expression 1:
   statement(s)
elif expression 2:
   statement(s)
elif expression 3:
   statement(s)
elif expression 4:
   statement(s)
else:
   statement(s)

Notice that when we have elif expressions involved, the if expression comes first and the else expression last. It is as if the if and else 
expressions sandwitch the elif statements. We shall illustrate examples that use the elif statements 
'''

'''Let's create a variable that holds the name of Guled, the best student in our Python Programming Language course 
and use an elif statement to print out a statement that evaluates true to the expression that follows the elif keyword'''

best_student = "Guled"

if best_student =="Khalid":
	print("Khalid is the best student in the Python Programming Language course.")
elif best_student =="Hodan":
	print("Hodan is the best student in the Python Programming Language course.")
elif best_student =="Munira":
	print("Munira is the best student in the Python Programming Language course.")
elif best_student =="Hassan":
	print("Hassan is the best student in the Python Programming Language course.")
elif best_student =="Guled":
	print("Guled is the best student in the Python Programming Language course.") #this is the statement that will be printed
else:
	print("Hashim is the best student in the Python Programming Language course.")


'''
This marks the end of our class today. We will meet in the next class. 
'''



