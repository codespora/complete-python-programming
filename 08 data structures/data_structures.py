# -*- coding: utf-8 -*-
"""data_structures.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oNayPtecqFdKmXM6vrbmZvrofb8zIcfK

<img style="float: left;" src="https://avatars.githubusercontent.com/u/88348966?s=400&u=9643fc4455139ef6e232241a949da1d6005499e6&v=4" alt="drawing" />

### Welcome to the Repository for the Complete Python Bootcamp!
## Simple Data Structures
Hello guys, welcome back.

In this section, we’re going to learning about how to store data in composite forms and how to manipulate those forms.

Those forms are called data structures and we focus on arrays(lists), touples, and dictionaries in this case

### Arrays(lists) in Python

A list in python is a collection of data and data structures. Lists can hold any combination of data at onces.

To start, we will create a simple list
"""

mylist = ["Abdi", "mubarik", 'Saleban', 1, 2.5, -1991]

"""#### Accessing elements in a list

To access elements in a list, you need to use their index or place in the list. The index of the first element("Abdi") is 0, the index of the second element is 1 and so on. 

To access an element will use square brackets in the form `mylist[index]` 

Run the following examples to see how it works
"""

print(mylist[0])

print(mylist[2])

print(mylist[4])

print(mylist[12])

"""#### Modifying the a list 

Here, we will show you how to change the elements of a list in two ways

###### Changing an element 
The first is change the value of an element using the index of the element. For examples let's change the first element of `mylist` to from Abdi to Somali.

Here's how to do that:
"""

mylist[0] = "Somali"
print(mylist)

"""When we print the list, we see that the first element is no longer Abdi.

##### Adding an element to the list 

To add a new element to the list we use the `append` operator.

See the example below.
"""

mylist.append("Africa")
print(mylist)

"""# Touples

Touples are a comma separated collection of data similar to lists, but touples are not mutable(changeable). You can't add or change the elements of a touple.

Let's create a touple show that it's not mutable.
"""

mytouple = (2,3,4,"abi",(2,3))
print(mytouple[0])
mytouple[0] = "mubarik"

"""# Dictionaries in Python

Dictionaries are collection of key, value pairs. 

Let's show you how to create a dictionary in Python

"""

mydict = {'age': 23, "name": "abdi"}
print(mydict)

"""#### Accessing values in a dictionary

To access a value in a dictionary, you will use the key the same way you would use the index in a list. Let's show you an example
"""

mydict['name']

mydict['age']

"""#### Modifying dictionaries in Python

Adding a new key value pair and changing the value of a key is the same in dictionaries. Let's demo both
"""

mydict["age"]=100
print(mydict)

mydict["language"]="Somali"
print(mydict)