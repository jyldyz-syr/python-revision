# python ch1: Data Structures and Algorithms Nanodegree Program

# Arithmetic Operators=================================================
print(3 + 5) # 8
print(1 + 2 + 3 * 3) # 12
print(3 ** 2) # 9
print(9 % 2) # 1


# My electricity bills for the last three months have been $23, $32 and $64. What is the average monthly electricity bill over the three month period? Write an expression to calculate the mean, and use print() to view the result.
# Write an expression that calculates the average of 23, 32 and 64
a=23+32+64
b=a/3
# Place the expression in this print statement
print(b)



# In this quiz you're going to do some calculations for a tiler. Two parts of a floor need tiling. One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 tiles long. Tiles come in packages of 6.
# How many tiles are needed?
# You buy 17 packages of tiles containing 6 tiles each. How many tiles will be left over?
# Fill this in with an expression that calculates how many tiles are needed.
print((9*7)+(5*7))

# Fill this in with an expression that calculates how many tiles will be left over.
print((17*6)-((9*7)+(5*7)))




# Integers and Floats=================================================
# Write code to compare these densities. Is the population of San Francisco more dense than that of Rio de Janeiro? Print True if it is and False if not.
# Write code that prints True if San Francisco is denser than Rio, and False otherwise
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

compare = san_francisco_pop_density > rio_de_janeiro_pop_density
print(compare)


# String Methods=================================================
# Write two lines of code below, each assigning a value to a variable

one = "new"
two = "old"

# Now write a print statement using .format() to print out a sentence and the 
#   values of both of the variables
print( "we need {} and {}".format(one, two))



# print statements and get the same output.

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

message = "Verse has a length of {} characters.\nThe first occurence of the \
word 'and' occurs at the {}th index.\nThe last occurence of the word 'you' \
occurs at the {}th index.\nThe word 'you' occurs {} times in the verse."

length = len(verse)
first_idx = verse.find('and')
last_idx = verse.rfind('you')
count = verse.count('you')

print(message.format(length, first_idx, last_idx, count))


# Debugging Code============================================




# Python ch2:Data Structues
#summary: 
# Types of Data Structures: Lists, Tuples, Sets, Dictionaries, Compound Data Structures
# Operators: Membership, Identity
# Built-In Functions or Methods



# Lists and Membership Operators
list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[0])
print(list_of_random_things[len(list_of_random_things)])


#Use list indexing to determine how many days are in a particular month based on the integer variable month, and store that value in the integer variable num_days. For example, if month is 8, num_days should be set to 31, since the eighth month, August, has 31 days.
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
# use list indexing to determine the number of days in month
num_days = days_in_month[:-3]

print(num_days)

# slice
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
eclipse_dates = eclipse_dates[-3:]
print(eclipse_dates)



