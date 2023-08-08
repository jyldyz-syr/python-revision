# Functions:
# Defining Functions
# Variable Scope
# Documentation
# Lambda Expressions
# Iterators and Generators
# example

def cylinder_volume(height, radius):
    pi = 3.14159
    return height  *pi*  radius ** 2






# TASK: Write a function named readable_timedelta. The function should take one argument, an integer days, and return a string that says how many weeks and days that is. For example, calling the function and printing the result like this:
# write your function here
def readable_timedelta(days):
    if days < 1:
        print('please enter a positive number which is equal or more than 1')
    elif days < 7:
        print("{} week(s) and {} day(s).".format(0, days))
    elif (days == 7):
        print("{} week(s) and {} day(s).".format(1,0))
    elif (days > 7):
        weeks = days // 7
    #I didn't knpw about Floor Division
        remainder = days % 7
        print("{} week(s) and {} day(s).".format(weeks,remainder))
    else:
        return('need input')

print(readable_timedelta(15))


# SOLUTION SHOWN BY THE PROGRAM
def readable_timedelta(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

# test your function
print(readable_timedelta(15))






# LOCAL SCOPE
def some_function():
    word = "hello"
    print(word)

some_function()


#  Documentation: example
def readable_timedelta(days):
    """Return a string of the number of weeks and days included in days."""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)



#LAMBDA. EXAMPLE OF A NORMAL FUNCTION:
def multiply(x, y):
    return x * y

print(multiply(4, 7))

# ANALOG IN LAMBDA
multiply = lambda x: x * 2
print(multiply(4))

multiply = lambda x, y: x * y
print(multiply(4, 7))
