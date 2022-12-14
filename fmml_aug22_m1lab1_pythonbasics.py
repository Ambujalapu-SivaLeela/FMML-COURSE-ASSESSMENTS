# -*- coding: utf-8 -*-
"""FMML_Aug22_M1Lab1_PythonBasics.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/viswanadhavarma/FMML-Course-Assignments/blob/main/FMML_Aug22_M1Lab1_PythonBasics.ipynb

# Getting Started

FMML Module 1, Lab 1 <br>
 Module Coordinator: Amit Pandey ( amit.pandey@research.iiit.ac.in ) <br>
 Release date: Aug 2022 <br>

### In this notebook we will be covering the very basics of Python and some basic libraries such as Numpy, Matplotlib and Nltk.
#### It is suggested that you go through each line and try some examples.

#### Section 1 - Python : Basic data types and indexing.
"""

## Strings
'''
A string is a collection of one or more characters put in a single quote,
 double-quote or triple quote. In python there is no character data type,
 a character is a string of length one. It is represented by str class.

String can have special characters. String can be indexed

'''


name = 'First Lab'
name_extended = name + 'Module 1'
last_element_string = name[-1] # -1 in python is index of the last element. 
## indexing is important for preprocessing of the raw data.

print(name ,"\n", name_extended, "\n", last_element_string)

## List

'''
Lists are ordered collection of data, and are very similar to arrays, 
It is very flexible as the items in a list do not need to be of the same type.
'''

name_list = ['First Lab', 3 , '1.1' , 'Lab 1'] ## notice elements are of different data type.
name_list.extend(['Module 1']) ## adding elements to list (Read about append method as well).
element_2 = name_list[1] ## Just like other languages, the index starts from 0.
two_dimesional_list = [[1,2],[3,4]] ## practice with multi-dimensional lists and arrays
## you would soon be required to handle 4 dimensional data :p :)
name_list[2] = '1.111' ##list elements can be changed

print(name_list)
print(element_2)
print(two_dimesional_list)
## list can have list, dictionary, string etc.

## Tuples

name_tuple = ('First Lab', 1, (2,3),[1,1,'list having string']) ## A tuple can have a tuple.
 
print(name_tuple[2])
print("first indexing the last element of the tuple, which is a list and \n then last element of the list (a string) and then second last element of the string:")
print(name_tuple[-1][-1][-2])

## tuples are immutable, read the error !
 #usued when passing parameters etc. and dont want them to be changed
name_tuple=list(name_tuple)
name_tuple[1] = 2
name_tuple

## Sets
'''a Set is an unordered collection of data types that is iterable, mutable and has no duplicate elements. 
The order of elements in a set is undefined though it may consist of various elements.
The major advantage of using a set, as opposed to a list,
 is that it has a highly optimized method for checking whether a specific element is contained in the set.
'''
set_unique = set([1,1,2,3,5,6,'Lab1'])
print(set_unique) ##notice it is unordered
last_el = set_unique.pop()
set_unique.add((1,2))


print(last_el)
print(set_unique)

set_unique=list(set_unique)
set_unique[1] ##it is not indexable

## Dictionary
'''
Dictionary in Python is an unordered collection of data values, used to store data values like a map,
 which, unlike other data types which hold only a single value as an element.
'''

dic = {'1': 'A','2':'B', 'C':3 } ##Observe how key and values can be anything
dic['4'] ='New'
print(dic)

"""#### Question 0:
###### write down 3-5 methods applicable to each data type. (Hint: extend, reverse, etc.

# **String Methods**

---
"""

#string method upper() used to convert string to uppercase
s1="Viswanadha Varma".upper()
s1

#string method lower() used to convert string to lowercase
s2="ViswAnadHa Varma".lower()
s2

#string method swapcase() used to convert lowercase to uppercase and uppercase to lowercase
s3="ViswAnaDha Varma".swapcase()
s3

#string method strip() used to remove either end elements
s4='jsbjjabhellouq'.strip('jsbauiq')
s4

#string method count() used to return the count specific character
s5="Viswanadha Varma".count('a')
s5

"""# List Methods

---


"""

#list method reverse() used to reverse
name_list.reverse()
name_list

#list method extend() used to add elements
name_list.extend([5,7])
name_list

#list method append() used to add single element
name_list.append([1,2,3])
name_list

#list method pop() to delete an element
name_list.pop(1)
name_list

#list method copy() used to make copy of a list
name_list1=name_list.copy()
name_list1

#list method insert() used to insert element at particular position by index number
name_list.insert(2,'hi')
name_list

#list method sort() used to sort a list of numbers from ascending to descending
num_list=[8,7,9,0.5,5,8,4]
num_list.sort()
num_list

"""# Tuple Methods

---

**As tuples are  immutable we have basic methods like index(),count()etc**
"""

#index() used to give index of particular element
elem_index=(3,4,1,5,6,8,6,8,9,8)
elem_index.index(1)

#count() used to return the count of specific element
elem_index.count(8)

"""# Set Methods"""

set1={1,2,3,4,5}
set2={4,5,6,7,8}

#add() method in set used to a elements
set1.add(6)
set1

#difference() method in set used to see difference between two sets
set3=set1.difference(set2)
set3

#intersection() method in set used to see same elememts in two or more sets
set4=set1.intersection(set2)
set4

#pop() removes random element from a set
set4.pop()
set4

#union() combines two sets
set5=set1.union(set2)
set5

"""# Dictionary Methods"""

dictionary={1:'a',2:'b',3:'c'}

#keys() method returns all the keys in the dictionary
dictionary.keys()

#values() method returns all the values in the dictionary
dictionary.values()

#items() method returns a list of each item in a tuple
dictionary.items()

#pop() method deletes a element by using key
dictionary.pop(1)
dictionary

"""## Section 2 - Functions
### a group of related statements that performs a specific task.
"""

def add_new(a:str, b): ## a and b are the arguments that are passed. to provide data type hint
                              # def add_new(x: float, y: float) -> float: 
  sum = a + b
  return sum

ans = add_new(1,2) ## intentionally written str, and passed int, to show it doesn't matter. It is just hint
print(ans)

asn = add_new(3,5)

def check_even_list(num_list):
    
    even_numbers = []
    
    # Go through each number
    for number in num_list:
        # Once we get a "hit" on an even number, we append the even number
        if number % 2 == 0:
            even_numbers.append(number)
        # Don't do anything if its not even
        else:
            pass
    # Notice the indentation! This ensures we run through the entire for loop    
    return even_numbers

"""#### Question 1 :

##### Define a function, which takes in two strings A and B. Reverses the first string A, adds it to B, and returns the final string.


#### Question 2 : 
##### Given a list having Names, work_hours, and gender, Write a function to print name of the female worker that worked the most hours. Also how much do should she be paid if the pay is $ 20 per hour.

##### work_hours = [('Abby',100 , 'F'),('Billy',400, 'M'),('Cassie',800,'F'), ('Maggi',600,'F'),('Alex',500,'M'),('Raj',225,'M'),('Penny',920,'F'),('Ben',300,'M')]

##### Answer : the female worker that worked the most hours is Penny and she should be paid 18400

# Answer for Question no 1
"""

#ANSWER1
def combined_string(A,B):
  A=A[::-1]
  return B+A
c=combined_string("ih",'hello')
c

"""# Answer for Question no2"""

#ANSWER2
def more_work(data):
  high=0
  for i in range(len(data)):
    if data[i][1]>high and data[i][2]=='F':
      high=data[i][1]
  high_paid=high*20
  worker=''
  for i in range(len(data)):
    if data[i][1]==high and data[i][2]=='F':
      worker+=data[i][0]
      break
  print(f"the female worker that worked the most hours is {worker} and she should be paid {high_paid}")
more_work([('Abby',100 , 'F'),('Billy',400, 'M'),('Cassie',800,'F'), ('Maggi',600,'F'),('Alex',500,'M'),('Raj',225,'M'),('Penny',920,'F'),('Ben',300,'M')])

"""#### Section 3 - Libraries and Reading data.

##### Numpy - One of the most used libraries - supports for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
"""

import numpy as np

a = np.array([1,1,2,3,4,5,5,6,1]) ## np.array converts given list to array

b = a>1 ## important comparison operation, where frequently used in manipulation and image processing.

print(b)
print(a[b]) ## [printing only those values in a which are greater than 1]

a_range = np.arange(10,19).reshape(3,3) ## create a 3x3 array with values in range 10-19
a_range

## Indexing in arrays works same as that of list

a_range[0] # printing all the columns of first row

a_range[:,2] #printing all the rows of second column

iden = np.eye(3) #idnetity matrix of given size
iden

## adding two matrices
summed = a_range + iden
summed

### arrays support normal matrix multiplication that you are used to, point-wise multiplication
### and dot product as well.

mul = a_range@iden ## normal multiplication
mul

## point wise multiplication
p_mul = a_range * iden
p_mul

## Transpose of a matrix.

mtx_t = mul.T
mtx_t

### Here we are changing the values of last row of the transposed matrix.
### basically point wise multiplying the values of last row with 1,2 and 3

mtx_t[2] = mtx_t[2]*[1,2,3] ## indexing, point wise multiplication and mutation of values
mtx_t

## Just like the greater than 1 (a>1) example we saw earlier.
## here we are checking if the elements are divisible by 2 (%), and if they are, then replace by 0.

mtx_t[(mtx_t % 2 == 0)] = 0 ## convert even elements of the matrix to zero.
mtx_t

"""#### Question 3 : 

##### a)Create a 5x5 matrix of the following form, 

##### [[1,1]
#####  [2,2]]

#####  i.e. each row is increasing and has repetive elements.

######  Hint : you can use hstack, vstack  etc.

##### b) find dot product of the matrix with any matrix. (Figure out the size/ shape of the matrix)

# Answer for Question no3a
"""

#ANSWER3a
m=np.zeros((5,5))
m+=np.arange(1,6)
n=m.T
n

"""# Answer for Question no3b"""

j=np.arange(1,26).reshape(5,5)
h=np.dot(n,j)
h
h.size

"""#### Reading Files"""

## loading from the google drive
from google.colab import drive 
drive.mount('/content/gdrive')

with open ('/content/sample_data/README.md', 'r') as f:
  a = f.readlines()

a ## here a is list of elements/strings each splitted at \n, \n is also part of the list element.

import pandas as pd

df = pd.read_csv('/content/sample_data/california_housing_test.csv','r')
df.head(10) ## pass as argument number of top elements you wish to print. Head is used to have a quick glance and understand the data.

len(df.columns), df.columns

df.columns[0]

df['longitude,"latitude","housing_median_age","total_'][:5]

df = df.rename(columns = {'longitude,"latitude","housing_median_age","total_':'Detail1'}) ##rename column names as at times it makes it easier for us

df.head(3)

df.iloc[:5, 0]  ##iloc - index - 0 to 4 rows and first column only.

import matplotlib
from matplotlib import pyplot as plt

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

"""## Creating a dataframe.
#### Task: Study about other methods of creating dataframe (for example: using Pandas Series, Lists etc.)
"""

import pandas as pd
import numpy as np

values = np.arange(16).reshape(4,4)
values

dataframe_from_array = pd.DataFrame(values, index = ['a','b','c','d'], columns=['w','x','y','z'] )
dataframe_from_array

dataframe_from_array.loc[['a','b'],['w','x']]

dataframe_from_array.iloc[:2,:2] ## it needs position as integer

dataframe_from_array.iloc[1,3] #second row and last column

dataframe_from_array.iloc[::2,::2]

import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 200), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()

## Question 3 : Upload an image to your google drive, Use plt.imread to read image from the google drive and then print that image using plt.imshow


## Answer 3 : 

## 1) make sure drive is loaded and then upload a test image onto your drive
#reading image
plt.imread('/content/gdrive/MyDrive/19092022.jpg')

#printing image using plt.imshow()
plt.imshow(plt.imread('/content/gdrive/MyDrive/19092022.jpg'))