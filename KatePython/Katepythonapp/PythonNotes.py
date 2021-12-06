# Terms

# I. Print- a function instructing the computer to output a "string" or single line of code to the command prompt
    #Example of using the function print:
print("Hello, World")

# II. String- a series of letters and numbers 
"Hello, World"
    #each string is contained within quotation marks and each string must be seperated by a comma
"Kate", "is learning Python"

# III. Script- scripting is a term used to describe a type of coding; scripting is high-level type of coding, meaning its easier. You are doing less of the nitty gritty coding and accessing more libraries.

# IV. Syntax- rules of the language

# V. Syntax Highlighting- multiple colors on the text

# VI. Variables- variables are labeled objects; they are object references
    #there are no spaces in a variable name
    #keep your variable names lower case
    #can contain both letters and number but must begin with either a letter or an underscore
    #camelCase
    #snake_case
    #Example of assigning a variable:
firstName = "Kate"
first_name = "John"
coffeeOfTheDay = "Hazulnut Dream"

# VII. Methods- are owned functions

________________________________________________________________________________

# HOW TO:

# Using variables and strings
firstName = "Kate"
print(firstName, "is learning Python")

# Getting input from a user
favoriteColor = input("What is your favorite color?  ")
print("The color", favoriteColor, "is a great color!")

# Using the input function / Enter
print("Hello")
input('Press Enter to see Step 1.')
print("Step 1:     ")

# Suppressing the print Function's Ending Newline p. 65 book
    # if you dont want a new line to start after the print function is complete you can:
    # the end=' ' arguement specifies that the print function should print a space
    #instead of a newline character at the end of its output.
    
print("One", end=' ')
print("Two", end=' ')
print("Three")
One Two Three

    # if you don't want the print function to print anything at the end of 
    #it's output, not even a space, pass the argument: end=''

print("One", end='')
print("Two", end='')
print("Three")
OneTwoThree

# Specifying an Item Separator p. 66
print("one", "two", "three", sep='')
OneTwoThree

# To specify a character other than the space to separate nultiple items
print("One", "Two", "Three", sep='*')
One*Two*Three

print("One", "Two", "Three", sep='~~~')
One~~~Two~~~Three

# Escape Character: a special character that is preceded with a backslash \, appearing inside a string literal
# the newline escape character: \n causes output to advance to the next line
\n 
\t # causes output to skip over to the next horizontal tab position
print("Mon\tTues\tWed")
Mon    Tues    Wed

# Escape Sequences- adding blank lines inside of your string
"I can't...\n\n even"
print(_)

# Using double quotes (if you have quotes within quotes)

# Concatenation- combining strings together
"chocolate" + "marshmallow"
'chocolatemarshmallow'

"chocolate" + " and marshmallows"
'chocolate and marshmallows'

# Reassignment- changing the variable into a new string
dessert = "chocolate" + " and marshmallows"
dessert = dessert + " and graham crackers"
dessert += ", yum"
'chocolate and marshmallows and graham crackers, yum'
dessert += "!" * 20
'chocolate and marshmallows and graham crackers, yum!!!!!!!!!!!!!!!!!!!!'

_______________________________________________________________________________

# Numeric

#Integers- integers are whole numbers (no decimals), sometimes called Ints

#Floats- Floating Point Numnbers are decimal point numbers
    #you will always get a float when you do division
    #to round a number:
0.1 + 0.1 + 0.1 - 0.3
5.551115123125783e-17

round(_)
0

#round function will round up or down
round(4.6)
5

round(4.2)
4

# Formatting Numbers p. 68 book
# the Format Specifier is a string that contains special characters specifying how the numeric value should be formatted.
    # to round a float to 2 decimal places:
    format(12345.6789, '.2f')

        # .2 specifies the precision; we want to round the number to two decimal places
        #  f specifies that the data type of the number we are formatting is a floating-point number

# Formatting in Scientific Notation
# use the letter e or E instead of f
print(format(12345.6789, 'e'))
1.234568e+04

print(format(12345.6789, '.2e'))
1.23e+04

# Inserting Comma Separators (to specify thousands, millions, etc.)
print(format(12345.6789, ',.2f'))
12,345.68

# Order of Operations (PEMDAS)

# you cannot add a string and ingteger together
# the input function always returns a string, it can not be an integer
# when you want input from a user for a number it must be entered as a string 
int("11")
11
float("11")
11.0
float(11)
11.0
int(11.9)
11
        #note how it didn't round it up to 12. 
        #Coercing this float into an integer this way simply made it ignore everything after the decimal point.

# Floating-Point and Integer Division p. 56 book
# if you only want to work with integers...
# division shortcut:
23 / 3
7.6666666666667
23 // 3
7               # when the result is positive, it is /truncated/, which means that its fractional part is thrown away.
23 % 3
2
        # 3 * 7 = 21 ; 23 - 21 = 2

-5 // 2
-3             # when the result is negative, it is rounded /away from 0/ to the nearest integer.

# The Exponent Operator
** # 2 asterisks written together is the exponent operator and its purpose is to raise a number to a power.
________________________________________________________________________________

# String Methods

#Booleans
bool(1)
True

bool(0)
False

bool(42)
True
                #any non zero number is True
                #0 is always False
bool("burrito")
True

bool("")
False
                #any object that isn't empty is true
                #string literal- a pair of quotes surrounding a character
                #empty string- no characters in the quotes
                #truthy or falsey- the way in which a value coerces to a boolean

True and True
True

True and True and False
False

False or True
True 

False or False
False

(False or False or True) and (True and False)
    # True and False
False 
    #both sides have to be true for it to be true

(False or False or True) and not (True and False)
True

is_smoker = True
has_kids = True
has_kids and not is_smoker
False

_______________________________________________________________________________

# Conditional Branching
# If, Else and Elif
# a single = is used for assignment and a == is used for comparison
fruit = "apples"
fruit == "apples"
True
fruit == "oranges"
False

firstName = input("What is your name?   ")
print("hello,", firstName)
if firstName == "Kate":
	print(firstName, "is learning python")
elif firstName == "Peek":
	print(firstName, "is learning with fellow students in the community!")
else:
	print("You should totally learn Python, {}!".format(firstName))
print("Have a great day {}!".format(firstName))

    # else (otherwise)

_______________________________________________________________________________

# How to Define Even/Odd Numbers and If/Else Algorithm (hackerrank.com)

n = int(input("Give me a number between 1-100:   "))
if ((n % 2 == 0 and n >= 2 and n <= 5) or (n % 2 == 0 and n > 20)):
    print("Not Weird")
elif ((n % 2 != 0) or (n % 2 != 0 and n >= 6 and n <= 20)):
    print("Weird")

________________________________________________________________________________

# Comparisons

"hot dogs" != "sandwiches"
    #this is used to check if 2 items are not equal, also referred to as "bang"

42 >= 42
True

"sunshine" > "rain"
True
    #this is true because the computer is looking at these 2 items in alphabetical order and
    #r comes before #s, so rain is less than sunshine and sunshine is greater than rain.

_______________________________________________________________________________

# FUNCTIONS and LOOPING

praise = "You are doing great"
praise = praise.upper()
number_of_characters = len(praise)
result = praise + "!" * number_of_characters
print(result)

# sidenote: using the .lower function automatically converts whatver the input is to lowercase and then checks the conditions against that. 
# therefore, it doesn't matter whether an uppercase or lowercase answer is entered. It will read it as lowercase.
# it is likewise for the .upper function

_______________________________________________________________________________

# To Create A Function

def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * (number_of_characters // 2)
    print(result)

yell("You are doing great")
yell("Don't forget to ask for help")
yell("Don't Repeat Yourself. Keep things DRY.")

# Returning Values

    #Remember, methods are just owned functions. Our string "You are doing great" owns the method/function .upper
_________________________________________________________________________

# Creating and Calling Functions with Main function

def main():
	number = 5
	show_double(number)

# The show_double function accepts an argument
# and displays double its value.

def show_double(number):
	result = number * 2
	print(result)

# Call the main function.
main()

__________________________________________________________________________

# Check Please

import math

def split_check(total, number_of_people):
    return math.ceil(total / number_of_people)

total_due = float(input("What is the total?   "))
number_of_people = int(input("How many people?  "))

amount_due = split_check(total_due, number_of_people)
print("Each person owes ${}".format(amount_due))

                        # import- is a keyword needed to tell our script that we want to use
                        #the function Math, which is a grouping of new tools (Module)
                        # We can use functions within a module by writing the module name (Math) and using dot notation
                        #to get to the function.
                        # ceil- stands for ceiling and always rounds up to the next closest integer.
help(math)

_____________________________________________________________________________

# Expecting Exceptions
import math

def split_check(total, number_of_people):
    return math.ceil(total / number_of_people)
try:
    total_due = float(input("What is the total?   "))
    number_of_people = int(input("How many people?  "))
except ValueError:
    print("Oh no! That's not a valid value. Try again...")
else:
    amount_due = split_check(total_due, number_of_people)
    print("Each person owes ${}".format(amount_due))

    # adding a string and an integer raises a TypeError.
____________________________________________________________________________

# Raising Exceptions

import math

def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required to split the check")
    return math.ceil(total / number_of_people)
try:
    total_due = float(input("What is the total? $   "))
    number_of_people = int(input("How many people?  "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:    
    print("Oh no! That's not a valid value. Try again...")
    print("({})".format(err))
else:
    print("Each person owes ${}".format(amount_due))

___________________________________________________________________________

# While Loops

# Example: do not use this for actual code!! Example only!


import sys

MASTER_PASSWORD = "opensesame"
password = input("Please enter the super secret password:    ")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password, try again:    ")
    attempt_count += 1
print("Welcome to secret town")

    #Loops are good for when you want code to run until a certain condition is true

_____________________________________________________________________________

# For Loops

    #run through each and every value its given in the iterable 

banner = "Happy Birthday!"
for letter in banner:
    print(letter.upper())

    # letter becomes a variable 
    # the "for" creates a loop that assigns "letter" as a variable to each and every
    #value within the string. 