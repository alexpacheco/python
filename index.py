
# coding: utf-8

# # Python Programming
# 
# 
# 
# 
# ### Alex Pacheco
# 
# 
# ### Research Computing


# ### Printing to screen
# 
# - Python has a built-in function, *print* to write output to standard output or screen

# In[1]:


print("Hello World!")


# ### Reading from screen
# 
# - Python has a built-in function, *input* to read input from standard input or screen

# In[2]:


input('What is your name? ')


# ## Your First Python Script
# 
# - Create a file, _myscript.py_, with the following content
# <code>
# print("Hello There!")
# </code>
# - On the command line, type _python myscript.py_ and hit enter

# In[3]:


get_ipython().system('python myscript.py')


# - If you are using Jupyter Notebooks, then bang (!) is used to invoke shell commands
# 

# ## Your First Python Script
# 
# - On Linux and Mac, add _#!/usr/bin/env python_ as the first line
# - Convert _myscript.py_ to an executable and execute it

# In[4]:


get_ipython().system('cat myscript.py')


# In[5]:


get_ipython().run_cell_magic('bash', '', 'chmod +x myscript.py\n./myscript.py')


# - If you are using Jupyter Notebooks, then <code>%%bash</code> is used to enter a series of bash command
#    * If you only need to run one command, then use <code>!</code> followed by the command

# ## Variables and Types
# 
# - A **variable** is a name that refers to a value.
# - An **assignment statement** creates new variables and gives them values:

# In[6]:


message = 'And now for something completely different'
n = 17
pi = 3.1415926535897931


# - The first assigns a string to a new variable named message
# - the second gives the integer 17 to n
# - the third assigns the (approximate) value of $\pi$ to pi
# 
# - To display the value of a variable, you can use a *print* function

# In[7]:


print(message)


# - The type of a variable is the type of the value it refers to.

# In[8]:


type(message)


# In[9]:


type(n)


# In[10]:


type(pi)


# ## Variable names
# 
# - Variable names can be arbitrarily long. They can contain both letters and numbers, but they have to begin with a letter.
# - The underscore character (\_) can appear in a name. 
#    * It is often used in names with multiple words, such as *my_name*
# - If you give a variable an illegal name, you get a syntax error:

# In[11]:


76trombones = 'big parade'


# In[12]:


class = 'Advanced Theoretical Zymurgy'


# ## Reserved Words
# 
# - Python has 31 keywords or reserved words that cannot be used for variable names.



# - Use an editor that has syntax highlighting, wherein python functions have a different color 
#    - See previous slides, variable names are in the normal color i.e. black while reserved keywords, for e.g. *class*, are in green

# ## Statements
# 
# - A statement is a unit of code that the Python interpreter can execute. We have seen two kinds of statements: print and assignment.
# 
# - When you type a statement in interactive mode, the interpreter executes it and displays the result, if there is one.
# 
# - A script usually contains a sequence of statements. If there is more than one statement, the results appear one at a time as the statements execute.

# In[13]:


print(1)
x = 2
print(x)


# ##  Data Types
# 
# 
# Python has 5 Data types
# 


# ### Integers
# 
# - There is effectively no limit to how long an integer value can be
# - You are constrained by the amount of memory your system

# In[14]:


print(123123123123123123123123123123123123123123123123 + 1)


# - Python interprets a sequence of decimal digits without any prefix to be a decimal number:

# In[15]:


print(10)
print(0o10)
print(0b10)


# - Add a prefix to an integer value to indicate a base other than 10:
# 
# | Prefix | Interpretation | Base |
# |:------:|:--------------:|:----:|
# | 0b | Binary | 2 |
# | 0o | Octal  | 8 |
# | 0x | Hexadecimal | 16 |
# 
# - The underlying type of a Python integer, irrespective of the base used to specify it, is called int

# In[16]:


type(10)


# In[17]:


type(0o10)


# In[18]:


type(0x10)


# ### Floating Point Number
# 
# - The *float* type in Python designates a floating-point number. 
# - *float* values are specified with a decimal point. 
# - Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation

# In[19]:


4.2


# In[20]:


type(0.2)


# In[21]:


type(.4e7)


# In[22]:


4.2e-4


# ### Floating-Point Representation
# 
# * For 64-bit systems, the maximum value a floating-point number can have is approximately $1.8 \times 10^{308}$
# * Python will indicate a number greater than that by the string *inf* 

# In[23]:


1.79e308


# In[24]:


1.8e+308


# * The closest a nonzero number can be to zero is approximately $5.0 \times 10^{-324}$
# * Anything closer to zero than that is effectively zero

# In[25]:


5e-324


# In[26]:


2e-324


# - Floating point numbers are represented internally as binary (base-2) fractions
# - Most decimal fractions cannot be represented exactly as binary fractions, so in most cases the internal representation of a floating-point number is an approximation of the actual value
# - In practice, the difference between the actual value and the represented value is very small and should not usually cause significant problems

# In[27]:


0.5 - 0.4 - 0.1


# - You can convert between an *int* and *float* types using built-in functions

# In[28]:


int(4.2)


# In[29]:


float(15)


# ### Complex Numbers
# 
# - Complex numbers are specified as *(real part)+(imaginary part)*j. For example:

# In[30]:


a = 2 + 3j
type(a)


# In[31]:


print(a.real, a.imag)


# In[32]:


a*a


# In[33]:


a*a.conjugate()


# ### Strings
# 
# 
# - Strings are sequences of character data. The string type in Python is called *str*.
# - String literals may be delimited using either single or double quotes. 
#     * All the characters between the opening delimiter and matching closing delimiter are part of the string:

# In[34]:


print("I am a string.")


# In[35]:


type("I am a string.")


# In[36]:


print('I am too.')


# In[37]:


type('I am too.')


# - A string in Python can contain as many characters as you wish. 
#    * The only limit is your machine’s memory resources. 
# - A string can also be empty:

# In[38]:


''


# - If you want to include either type of quote character within the string, the simplest way is to delimit the string with the other type. 
#    * If a string is to contain a single quote, delimit it with double quotes and vice versa

# In[39]:


print("This string contains a single quote (') character.")
print('This string contains a double quote (") character.')


# - Alternatively, escape the quote character using a backslah

# In[40]:


print('This string contains a single quote (\') character.')
print("This string contains a double quote (\") character.")




# #### Interactive Python - User Input
# 
# - To interact with standard input, the *input* function can be assigned to a string variable
# - Modify your *myscript.py* file to ask for your name or anyone's name interactively 

# In[41]:


# To run example within Jupyter Notebook or IPython or Python Shell
name = input ("What is your name? ")
print("Hello ",name)


# - You need to use built-in functions, *int* or *float* to read integer or floating numbers from standard input

# #### Triple Quoted Strings
# 
# - Triple-quoted strings are delimited by matching groups of three single quotes or three double quotes. 
# - Escape sequences still work in triple-quoted strings, but single quotes, double quotes, and newlines can be included without escaping them. 
# - This provides a convenient way to create a string with both single and double quotes in it

# In[42]:


print('''This string has a single (') and a double (") quote.''')


# - Because newlines can be included without escaping them, this also allows for multiline strings:

# In[43]:


print("""This is a
string that spans
across several lines""")


# ### Boolean
# 
# - Objects of Boolean type may have one of two values, *True* or *False*:

# In[44]:


type(True)


# In[45]:


type(False)


# In[46]:


print("Max value for exponent %e" % pow(2,1023))
print("Max number of decimals %e" % pow(2,53))


# ## Operators and Operands
# 
# - Operators are special symbols that represent computations like addition and multiplication. 
# - The values the operator is applied to are called operands.
# 
# 

# ### Arithmetic Operators
# 


# In[47]:


a = 4
b = 3
print(+a)
print(-b)


# In[48]:


print(a + b)
print(a - b)


# In[49]:


print(a * b)
print(a / b)
print(3 * a // b)
print(2 * a % b)
print(a ** b)


# ### String Operations
# 
# - Python strings are immutable i.e. once a string is created it can’t be modified

# In[50]:


str1="Hello"
str2="Hello"
print(id(str1),id(str2))


# - *str1* and *str2* both refer to the same memory location
# - If you modify *str1*, it creates a new object at a different memory location

# In[51]:


str1+=", Welcome to LTS Seminars"
print(str1,id(str1),id(str2))


# - Every element of a string can be referenced by their index (first index is 0)

# In[52]:


str1[0]


# - _+_  operator is used to concatenate string and _*_ operator is a repetition operator for string.

# In[53]:


s = "So, you want to learn Python? " * 4
print(s)


# - You can take subset of string from original string by using [] operator, also known as slicing operator.
# - <code>s[start:end]</code> will return part of the string starting from index <code>start</code>  to index <code>end - 1</code>

# In[54]:


s[3:15]


# - <code>start</code> index and <code>end</code> index are optional. 
# - default value of <code>start</code>  index is 0 
# - default value of <code>end</code> is the last index of the string

# In[55]:


s[:3]


# In[56]:


s[15:]


# In[57]:


s[:]


# #### String functions
# 


# In[58]:


len(s)


# ### Comparison Operators
# 
# - Can be used for both numbers and strings
# - Python compares string lexicographically i.e using ASCII value of the characters


# In[59]:


a = 10
b = 20
print(a == b)


# In[60]:


c = 'Hi'
d = 'hi'
print(c == d)
print( c < d)
print(ord('H'),ord('h'),ord('i'))


# - Consider two strings 'Hi' and 'HI' for comparison. 
# - The first two characters ( H  and H ) are compared. 
# - Since 'i' has a greater ASCII value (105) than 'I' with ASCII value (73), 'Hi' is greater than 'HI'

# In[61]:


'HI' < 'Hi'


# ### Logical Operators



# In[62]:


x = 5
not x < 10


# In[63]:


x < 10 or callable(x)


# In[64]:


x < 10 and callable(len)


# ## Functions

# - A **function** is a named sequence of statements 
#   - functions are specified by name and a sequence of statements. 
#   - You "call" the function by name.

# In[65]:


print(x)


# - The name of the function is *print*. 
# - The expression in parentheses is called the **argument** of the function. 
# - The result, for this function, is the type of the argument.
# 
# - It is common to say that a function "takes" an argument and "returns" a result. 
# - The result is called the **return value**.



# In[66]:


import math


# - This statement creates a **module object** named *math*
# - If you print the module object, you get some information about it

# In[67]:


print(math)


# - The module object contains the functions and variables defined in the module
# - To access one of the functions, you have to specify the name of the module and the name of the function, separated by a dot (also known as a period)
# - This format is called **dot notation**
# 
# 

# In[68]:


degrees = 45
radians = degrees / 360.0 * 2 * math.pi
math.sin(radians)


# ### Iterables and Iterators
# 

# In[69]:


def celcius_to_fahrenheit(tempc):
    tempf = 9.0 / 5.0 * tempc + 32.0
    return tempf


# In[70]:


tempc = float(input('Enter Temperature in Celcius: '))

print("%6.2f C = %6.2f F" % (tempc, celcius_to_fahrenheit(tempc)))


# - When you create a variable inside a function, it is **local**, which means that it only exists inside the function.
#    - e.g. *tempf* is local within the *celcius_to_fahrenheit* function and does not exist outside the scope of the function
# 

# In[71]:


print(tempf)


# ## Conditional Execution

# - **Conditional Statements** gives the programmer an ability to check conditions and change the behavior of the program accordingly.
# - The simplest form is the if statement:

# Syntax:
# <code>
# if condition:
#     statements
# </code>


# In[72]:


if x < 0:
    pass


# - There may be a situation where you want to execute a series of statements if the *condition*
#  is false
# - Python provides an <code>if ... else ...</code> conditional
# - Syntax
# <code>
# if condition:
#     statments_1
# else:
#     statements_2
# </code>

# In[73]:


if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')



# 
# - Sometimes there are more than two possibilities and we need more than two branches.
# - Python provides a <code>if ... elif ... else</code> conditional
# - Syntax
# <code>
# if condition1:
#     statements_1
# elif condition2:
#     statements_2
# else
#     statements_3
# </code>    

# In[74]:


y = 10
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')


# - _elif_ is an abbreviation of “else if.” 
# - Again, exactly one branch will be executed. 
# - There is no limit on the number of _elif_ statements. 
# - If there is an _else_ clause, it has to be at the end, but there doesn’t have to be one.

# In[75]:


choice='d'
if choice == 'a':
    print('choice is a')
elif choice == 'b':
    print('choice is b')
elif choice == 'c':
    print('choice is c')


# - Each condition is checked in order. 
# - If the first is false, the next is checked, and so on. 
# - If one of them is true, the corresponding branch executes, and the statement ends. 
# - Even if more than one condition is true, only the first true branch executes.

# 
# - Conditional can also be nested within another.
# 

# In[76]:


if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')


# - The outer conditional contains two branches. 
# - The first branch contains a simple statement. 
# - The second branch contains another _if_ statement, which has two branches of its own. 
# - Those two branches are both simple statements, although they could have been conditional statements as well.
# 
# 

# - Logical operators often provide a way to simplify nested conditional statements. 

# In[77]:


if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')


# - The _print_ statement is executed only if we make it past both conditionals
# - we can get the same effect with the _and_ operator

# In[78]:


if 0 < x and x < 10:
    print('x is a positive single-digit number.')


# ### Control Statements
# 
# Python provides three control statements that can be used within conditionals and loops
# 
# 
# 1. **break**: Terminates the loop statement and transfers execution to the statement immediately following the loop
# 2. **continue**: Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
# 3. **pass**: The pass statement is used when a statement is required syntactically but you do not want any command or code to execute.

# ### Recursion
# 
# - Python functions can call itself recursively

# In[79]:


def factorial(n):
    if n < 1:
        return 1
    else:
         return n*factorial(n-1)


# In[80]:


factorial(5)


# In[81]:


def double_fact(n):
    if n < 2:
        return 1
    else:
        return n * double_fact(n - 2)


# In[82]:


double_fact(10)


# ## Loops
# 
# - There may be a situation when you need to execute a block of code a number of times.
# 
# - A loop statement allows us to execute a statement or group of statements multiple times.

# ### for loops
# 
# - The *for* statement has the ability to iterate over the items of any sequence, such as a list or a string 
# - If a sequence contains an expression list, it is evaluated first. 
# - Then, the first item in the sequence is assigned to the iterating variable iterating_var. 
# - Next, the statements block is executed. 
# - Each item in the list is assigned to iterating_var, and the statement(s) block is executed until the entire sequence is exhausted.
# 
# <code>
# for iterating_var in sequence:
#    statements(s)
# </code>

# In[83]:


for letter in 'Hola': 
   print('Current Letter :', letter)


# In[84]:


fruits = ['banana', 'apple',  'mango']
for fruit in fruits: 
   print ('Current fruit :', fruit)


# - An alternative way of iterating through each item is by index offset into the sequence itself

# In[85]:


fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('Current fruit :', fruits[index])


# #### range function
# 
# - The built-in function *range()* iterates over a sequence of numbers.

# In[86]:


range(5)


# In[87]:


list(range(5))


# In[88]:


for var in list(range(5)):
    print(var)


# ### while loop
# 
# - A *while* loop statement repeatedly executes a target statement as long as a given condition is true.
# - Here, **statement(s)** may be a single statement or a block of statements with uniform indent. 
# - The **condition** may be any expression, and true is any non-zero value. The loop iterates while the condition is true.
# - When the condition becomes false, program control passes to the line immediately following the loop.
# 
# <code>
# while expression:
#    statement(s)
# </code>

# In[89]:


number = int(input('Enter any integer: '))

fact = count = 1
while (count <= number ):
    fact = count * fact
    count += 1
print('Factorial of %d is %d' % (number, fact))


# #### infinite loop
# 
# - A loop becomes infinite loop if a condition never becomes FALSE
# 
# <code>
# number = int(input('Enter any integer: '))
# fact = count = 1
# while (count <= number ):
#     fact = count * fact
# print('Factorial of %d is %d' % (number, fact))
# </code>    

# #### Using else Statement with Loops
# 
# - Python supports having an *else* statement associated with a loop statement.
# - If the *else* statement is used with a *for* loop, the *else* block is executed only if the *for* loops terminates normally (and not by encountering break statement).
# - If the *else* statement is used with a *while* loop, then the *else* statement is executed when the condition becomes false.

# In[90]:


numbers = [11,33,55,39,55,75,37,21,23,41,13]

for num in numbers:
   if num%2 == 0:
      print ('the list contains an even number')
      break
else:
   print ('the list does not contain even number')


# In[91]:


count = 0
while count < 5:
   print (count, " is  less than 5")
   count = count + 1
else:
   print (count, " is not less than 5")


# ## Lists
# 
# - Like a string, a *list* is a sequence of values. 
# - In a string, the values are characters; in a list, they can be any type. 
# - The values in list are called **elements** or sometimes items.

# In[92]:


a = [10, 20, 30, 40]
print(a)


# - *lists* can be nested.

# In[93]:


b = ['spam', 2.0, 5, [10, 20]]
print(b)


# - An empty list i.e. list with no elements is created with empty brackets [].

# In[94]:


c=[]
print(c)


# - Lists are mutable i.e. they can be modified after creation

# In[95]:


numbers = [17, 123]
print(numbers)


# In[96]:


numbers[0] = 5
print(numbers)


# - A list can be traversed using a *for* loop 

# In[97]:


for i in numbers:
    print(i)


# - The + operator concatenates lists:

# In[98]:


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)


# - You can reference a section of the list using a slice operator

# In[99]:


c[2:5]


# #### list operations
# 
# - *append* adds a new element to the end of the list

# In[100]:


t1 = ['a', 'b', 'c']
t1.append('d')
print(t1)


# - *extend* takes a list as an argument and appends all of the elements

# In[101]:


t2 = ['e', 'f']
t1.extend(t2)
print(t1)


# - *sort* arranges the elements of the list from low to high:

# In[102]:


t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)


# #### deleting list elements
# 
# - *pop* modifies the list and returns the element that was removed. 
# - If you don’t provide an index, it deletes and returns the last element

# In[103]:


t = ['a', 'b', 'c']
x = t.pop(1)
print(t)


# In[104]:


print(x)


# - Use *del* if you do not need the removed value

# In[105]:


t = ['a', 'b', 'c']
del t[1]
print(t)


# - If you know the element you want to remove (but not the index), you can use *remove*

# In[106]:


t = ['a', 'b', 'c', 'd', 'e', 'f']
t.remove('b')
print(t)


# - To remove more than one element, you can use *del* with a slice index

# In[107]:


t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)


# #### lists and strings
# 
# - A string is a sequence of characters and a list is a sequence of values
# - list of characters is not the same as a string. 
# - To convert from a string to a list of characters, you can use *list*

# In[108]:


s = 'spam'
t = list(s)
print(t)


# - The *list* function breaks a string into individual letters. 
# - If you want to break a string into words, you can use the *split* method

# In[109]:


s = 'pining for the fjords'
t = s.split()
print(t)


# - An optional argument called a **delimiter** specifies which characters to use as word boundaries

# In[110]:


s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)


# - *join* is the inverse of *split*. 
# - It takes a list of strings and concatenates the elements. 
# - *join* is a string method, so you have to invoke it on the delimiter and pass the list as a parameter

# In[111]:


t = ['pining', 'for', 'the', 'fjords']
delimiter = ':'
delimiter.join(t)


# ## Dictionaries
# 
# - A *dictionary* is a mapping between a set of indices (which are called **keys**) and a set of **values**. 
# - Each key maps to a value. 
# - The association of a key and a value is called a **key-value pair**
# - The function *dict* creates a new dictionary with no items

# In[112]:


eng2sp = dict()
print(eng2sp)


# - To add items to the dictionary, you can use square brackets

# In[113]:


eng2sp['one'] = 'uno'
print(eng2sp)


# - You can update a dictionary by adding a new entry or a key-value pair

# In[114]:


eng2sp['two'] = 'dos'
print(eng2sp)


# - You can create a dictionary as follows

# In[115]:


eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)


# - the order of items in a dictionary is unpredictable
# - use *keys* to look up the corresponding *value*

# In[116]:


print(eng2sp['three'])


# - To delete entries in a dictionary, use *del*

# In[117]:


del eng2sp['two']
print(eng2sp)


# - The *clear()* function is used to remove all elements of the dictionary

# In[118]:


eng2sp.clear()
print(eng2sp)


# - The *len* function returns the number of key-value pairs

# In[119]:


eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
len(eng2sp)


# - You can loop through keys or values by using the *keys* and *values* functions

# In[120]:


for keys in eng2sp.keys():
    print(keys)


# In[121]:


for vals in eng2sp.values():
    print(vals)


# ## Tuples
# 
# - A *tuple* is a sequence of values
# - The values can be any type, and they are indexed by integers. 
# 

# In[122]:


t = ('a', 'b', 'c', 'd', 'e')


# - To create a tuple with a single element, you have to include the final comma

# In[123]:


t1 = ('a',)
type(t1)


# In[124]:


t2 = ('a')
type(t2)


# - Another way to create a tuple is the built-in function *tuple*. 
# - With no argument, it creates an empty tuple

# In[125]:


t = tuple()
print(t)


# - If the argument is a sequence (string, list or tuple), the result is a tuple with the elements of the sequence

# In[126]:


t = tuple('lupins')
print(t)


# - Most list operators also work on tuples. The bracket operator indexes an element

# In[127]:


t = ('a', 'b', 'c', 'd', 'e')
print(t[1])


# - slice operator selects a range of elements

# In[128]:


print(t[1:],id(t))


# - Unlike *lists*, *tuples* are immutable

# In[129]:


t[0] = 'A'


# - You can’t modify the elements of a tuple, but you can replace one tuple with another

# In[130]:


t = ('A',) + t[1:]
print(t,id(t))


# ### Assignment
# 
# - It is often useful to swap the values of two variables using a cumbersome procedure

# In[131]:


a = 1
b = 2


# In[132]:


temp = a
a = b
b = temp
print(a,b)


# - *tuple assignment* is more elegant

# In[133]:


a,b = b,a
print(a,b)


# - The number of variables on the left and the number of values on the right have to be the same

# In[134]:


a, b = 1,2,3


# - Tuples can be used to return multiple values from a function

# In[135]:


quot, rem = divmod(7, 3)
print(quot)


# In[136]:


print(rem)


# ## File Handling
# 
# 
# - To read/write a file, you have to open it with an appropriate mode as the second parameter
# 
# <code>
# open(filename, mode)    
# </code>
# 
# | mode | description |
# |------|-------------|
# | r | Opens a file for reading only, default mode |
# | w | Opens a file for writing only |
# | a | Opens a file for appending only. File pointer is at end of file |
# | rb | Opens a file for reading only in binary |
# | wb | Opens a file for writing only in binary|
# 

# In[137]:


fout = open('output.txt', 'w')
print(fout)


# - If the file already exists, opening it in write mode clears out the old data.
# - If the file doesn’t exist, a new one is created.
# - The *write* method puts data into the file.

# In[138]:


line1 = "This here's the wattle,\n"
fout.write(line1)


# In[139]:


line2 = "the emblem of our land.\n"
fout.write(line2)


# - When you are done writing, you have to close the file.

# In[140]:


fout.close()
get_ipython().system('cat output.txt')


# - To read data back from the file you need one of these three methods
# 
# | Method | Description |
# |--------|-------------|
# | read([number]) | Return specified number of characters from the file. <br>if omitted it will read the entire contents of the file.|
# | readline() | Return the next line of the file.|
# | readlines() | Read all the lines as a list of strings in the file|

# - Reading all the data at once.

# In[141]:


f = open('myscript.py', 'r')
f.read() 


# In[142]:


f.close()


# - Reading all lines as an array

# In[143]:


f = open('myscript.py', 'r')
f.readlines() 


# In[144]:


f.close()


# - Reading only one line.

# In[145]:


f = open('myscript.py', 'r')
f.readline() 


# In[146]:


f.close()


# - You can iterate through the file using file pointer.

# In[147]:


f = open('myscript.py', 'r')
for line in f:
    print(line)
f.close()    


# ### Formatted output
# 
# - The argument of write has to be a string
# - convert other values to strings using *str*

# In[148]:


f = open('output.txt', 'w')
x = 52
f.write(str(x))
f.close()
get_ipython().system('cat output.txt')


# - An alternative is to use the **format operator**, %
# - The first operand is the **format string**, and the second operand is a **tuple of expressions**.

# In[149]:


tempc = float(input('Enter Temperature in Celcius: '))

print("%6.2f C = %6.2f F" % (tempc, celcius_to_fahrenheit(tempc)))


# - The general syntax for print function is <code>print(format string with placeholder % (variables) )</code>
# 
# - The general syntax for a format placeholder is <code>%[flags][width][.precision]type</code>
# 
# | type | data type |
# |------|-----------|
# | s | strings |
# | f or F | floating point numbers |
# | d or i | integers |
# | e or E | Floating point exponential format |
# | g or G | same as e or E if exponent is greater than -4, f or F otherwise |

# - If you try to open a file that doesn’t exist, you get an IOError:
# 

# In[150]:


fin = open('bad_file')


# - If you don’t have permission to access a file
# 

# In[151]:


fout = open('/etc/passwd', 'w')


# - or if you try to open a directory for reading

# In[152]:


fin = open('/home')


# - Python provides statements, *try* and *except* to allow programmers to gracefully quit the program

# In[153]:


try:    
    fin = open('bad.txt')
    for line in fin:
        print(line)
    fin.close()
except:
    print('Something went wrong.')


# In[154]:


get_ipython().system('cat test1.py')


# In[155]:


get_ipython().system('python test1.py')


# In[156]:


get_ipython().system('cat test2.py')


# In[157]:


get_ipython().system('python test2.py')


# ## Modules
# 
# - Python module is a normal python file which can store function, variable, classes, constants etc
# - Module helps us to organize related codes 
# - Popular modules
#    * math
#    * numpy
#    * scipy
#    * matplotlib
#    * pandas
#    * mpi4py

# ### Creating modules
# 
# - Create a new file called _mymodule.py_ and write the following code.

# In[158]:


get_ipython().system('cat mymodule.py')


# - This module defines a global variable _foo_ and a function _hello_
# - To use this module in a program, you need to **import** the module

# In[159]:


import mymodule


# In[160]:


mymodule.foo


# In[161]:


mymodule.hello()


# - If you only need to import a variable or function, then use **from** with **import**

# In[162]:


from mymodule import hello
hello()


# - You can also abbreviate the module name by adding **as** to the **import**

# In[163]:


import mymodule as my
my.foo


# ## NumPy
# 
# - NumPy is the fundamental package for scientific computing with Python. 
# - It contains among other things
#    - a powerful N-dimensional array object
#    - sophisticated (broadcasting) functions
#    - tools for integrating C/C++ and Fortran code
#    - useful linear algebra, Fourier transform, and random number capabilities
# - NumPy can also be used as an efficient multi-dimensional container of generic data. 
# - Numpy arrays are a great alternative to Python Lists

# - NumPy’s main object is the homogeneous multidimensional array.
# - NumPy’s array class is called *ndarray*. It is also known by the alias *array*
# - The more important attributes of an *ndarray* object are:
#    - ndarray.ndim: the number of axes (dimensions) of the array.
#    - ndarray.shape: the dimensions of the array.
#    - ndarray.size: the total number of elements of the array.
#    - ndarray.dtype: an object describing the type of the elements in the array.
#    - ndarray.itemsize: the size in bytes of each element of the array.
#    - ndarray.data: the buffer containing the actual elements of the array.

# - To use Numpy, you need to import the numpy module
#     * convention: import as np and then use the dot notation

# In[164]:


import numpy as np


# ### Numpy Arrays
# 
# -  create an array from a regular Python _list_ or _tuple_ using the _array_ function

# In[165]:


a = np.array([2,3,4])
print(a, a.dtype)


# - _array_ transforms sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into three-dimensional arrays

# In[166]:


b = np.array([(1.2, 3.5, 5.1),(4.1,6.1,0.5)])
print(b, b.dtype)


# - The type of the array can also be explicitly specified at creation time

# In[167]:


c = np.array( [ [1,2], [3,4] ], dtype=complex )
c


# - The function _zeros_ creates an array full of zeros, 
# - the function _ones_ creates an array full of ones, and 
# - the function _empty_ creates an array whose initial content is random and depends on the state of the memory.

# In[168]:


print('Zeros: ',np.zeros( (3,4) ))
print('Ones', np.ones( (2,4), dtype=np.float64 ))
print('Empty', np.empty( (2,3) ))


# - NumPy provides a function analogous to range that returns arrays instead of lists.

# In[169]:


np.arange( 10, 30, 5 )


# - The _reshape_ function can be used to convert an array into a matrix

# In[170]:


a = np.arange(15).reshape(3, 5)
a


# In[171]:


print("array dimensions: ", a.shape)
print("number of dimensions: ", a.ndim)
print("element types: ", a.dtype.name)
print("size of elements: ", a.itemsize)
print("total number of elements: ",a.size)
print("type of object:",type(a))


#  - Arithmetic operators on arrays apply elementwise

# In[172]:


a = np.array( [20,30,40,50] )
b = np.arange( 4 )
print('a: ', a)
print('b:', b)
print('a-b:', a-b)
print('B**2', b**2)
print('10*sin(a): ', 10*np.sin(a))
print('Which elements of a < 35:', a<35)
print('Elements of a < 35: ',a[a<35])


# In[173]:


A = np.array( [[1,1], [0,1]] )
B = np.array( [[2,0], [3,4]] )
print('A = ', A)
print('B = ', B)
print('A*B = ', A*B)
print('A . B = ', A.dot(B))
print('Numpy A. B = ', np.dot(A, B))


# - Numpy provides *linspace* for generating a sequence of linearly spaced numbers and a random number generator

# In[174]:


np.linspace(0,2*pi,4)


# In[175]:


np.random.random((2,3))


# - NumPy provides mathematical functions such as sin, cos, and exp.

# In[176]:


B = np.arange(3)
print('B: ',B)
print('exp(B): ',np.exp(B))
print('sqrt(B): ',np.sqrt(B))
C = np.array([2., -1., 4.])
print('C: ', C)
print('B + C: ', np.add(B, C))


# ## Visualization
# 
# - Matplotlib is the most popular visualization tool used in Python
# - Other visualization tools commonly used are bokeh, seaborn and plot.ly
# - More details at next weeks seminar

# In[177]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

# Prepare the data
x = np.linspace(0, 10, 100)

# Plot the data
plt.plot(x, x, label='linear')

# Add a legend
plt.legend()

# Show the plot
plt.show()


# In[178]:


plt.plot([1, 2, 3, 4], [1, 4, 9, 16])


# In[179]:


plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()


# - Saving a figure can be done using the *savefig()* command

# In[180]:


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^')
ax.set_xlim(0.5, 4.5)
fig.savefig('my_figure.png')


# In[181]:


from IPython.display import Image
Image('my_figure.png')


# In[182]:


t = np.arange(0., 5., 0.2)

# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()


# In[183]:


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()


# In[184]:


np.random.seed(19680801)

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()


# In[185]:


N = 5
menMeans = (20, 35, 30, 35, 27)
womenMeans = (25, 32, 34, 20, 25)
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width, yerr=menStd)
p2 = plt.bar(ind, womenMeans, width,
             bottom=menMeans, yerr=womenStd)

plt.ylabel('Scores')
plt.title('Scores by group and gender')
plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('Men', 'Women'))

plt.show()


# In[186]:


labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


# In[187]:


x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]

z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
plt.imshow(z, origin='lower', extent=[0, 5, 0, 5],
           cmap='viridis')
plt.colorbar();


# # Further Reading: Python Books
# 
# - **Think Python 2e** - Allen B. Downey
# - **Automate the Boring Stuff with Python** - Al Sweigart
# - **Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython** - Wes McKinney 
# - **Think Stats** - Allen B. Downey
# - **Think Bayes: Bayesian Statistics in Python** - Allen B. Downey
# - **Python Data Science Handbook** - Jake VanderPlas
# 
