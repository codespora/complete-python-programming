'''
Hello and welcome to this class. In this lesson, we're going to learn about functions in the Python Programming Language. A natural question that is worthy of asking from the onset
goes as follows: What is a function? Simply put, a function refers to a block of related programming statements that are grouped together. This makes it easier for the code to be
used. Rather than repeat related statements, we write a function to take care of related statements that perform a specific task. Anytime that we need that function, we can call it.
In Python Programming Language, the def keyword is used to create/define a function.

'''
#Let's create the first skeleton of a function using the above-mentioned def keyword
def myFirst_function():
  print("Hello Amina and welcome to your first function.")
myFirst_function() 
'''first_function() as shown above is how our function is called/invoked to print the statement. Hence, you are able to see the statement being printed out.
 If you do not call it this way, you will not be able to run the function 
'''

#The second functional concept that we would learn today is the argument/paramaters. 
'''As we have seen from the definition of the function, the name of the function is followed by parentheses. Information can be passed into these parentheses as arguments/parameters
 for the function.From the functional standpoint, a parameter refers to the variable listed inside the parentheses of the function whereas the argument is the value that is sent
 to the function when it is called. The number of arguments that a function can take can be more than 1. For the sake of simplicity, this lesson will stick to the 1-paramater function

'''
''' Let's define a function that takes the temperature of a city (in degree celsius) and change that into Fahrenheit. We will use the regular temperature of Hargeisa, Somaliland, 
and Jijiga (Somali Region, Ethiopia) as examples. Usually, Hargeisa's temperature is around 32 °C (degree celsius) while Jijiga's is around 28 °C.We will change these temperatures 
into degree Fahrenheit (°F).
'''
def celsius_to_fahrenheit(temp_celsius):
  return (temp_celsius) * (9/5)+32 #This converts the temperature in celsius to Fahrenheit
print("Hargeisa's temperature in degree Fahrenheit is", celsius_to_fahrenheit(32), "°F.")
print("Jijiga's temperature in degree Fahrenheit is ", celsius_to_fahrenheit(28), "°F.")

'''
Let's work on another example. In this example, we will write a function that simulates the work done by a money exchanger (sarifle in Somali language)
Assume that you have some money in the form of U.S dollars ($) and you would like to know how much you are worth in Somali Shillings. We can 
write a function that can convert our U.S. dollars into Somali Shillings. We will use today's rate to convert. The date today is 17th of August
2021 and 1 U.S dollar is equivalent to 585.00 Somali Shillings. 

'''
def usdollars_to_somaliShillings(usd):
  amount_in_SomaliShillings = (usd*585.00)
  return amount #this gives us the result









'''
In this lesson's last example, we focus on defining a function that accepts a list of cities. Then, we will use that function to print the names of the cities
in the Horn of Africa. 
'''
def my_cities(cities):
  for city in cities:
    print(city)
magaalooyin = ["Mogadishu", "Addis Ababa", "Asmara", "Hargeisa", "Jijiga", "Djibouti", "Dire Dawa", "Harar"]
print ("The below mentioned are some of the cities in the region: ")
my_cities(magaalooyin)

'''That is the end of our class today. See you in the next class'''


