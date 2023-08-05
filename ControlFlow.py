# CONTROL FLOW==================================================================
# Conditional Statements
# Boolean Expressions
# For and While Loops
# Break and Continue
# Zip and Enumerate
# List Comprehensions



#Create a new list with capitalized names for cities
cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
capitalized_cities = []

for city in cities:
    capitalized_cities.append(city.title())

print(cities[0].title())
print(cities[0].capitalize())
print(capitalized_cities)



# Write a for loop using range() to print out multiples of 5 up to 30 inclusive
list1 = list(range(5,34,5))
for index in list1:
    print(index)



# Write a for loop using range() to print out numbers that multiple of 5 up to 30 inclusive
list1 = list(range(30))
list2 = []
for index in list1:
    if index %5 == 0:
        list2.append(index)
    else:
        continue
print(list2)


#Replacing instances of a character in a string and make names appear in lower case
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    name = name.lower()
    name = name.replace(' ', '_')
    usernames.append(name)
    
print(usernames)


#count how many str with XML 
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for i in tokens:
    if i[0] == '<':
        count+=1

print(count)



#string's first line should be the opening tag <ul>. Following that is one line per element in the source list, surrounded by <li> and </li> tags. The final line of the string should be the closing tag </ul>.
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line,
                     # it does the characters that are after it in html_str
                     # are on the next line

for item in items:
    html_str = html_str + "<li>" + str(item) + "</li>" "\n"
    html_str = html_str + "</ul>"

print(html_str)



# Method 1: Using a for loop to create a set of counters

book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}

for word in book_title:
    if word not in word_counter:
            word_counter[word] = 1
else:
            word_counter[word] += 1
    
print(word_counter)







# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for key, value in basket_items.items():
    if key in fruits:
        result+=value
    
print("There are {} fruits in the basket.".format(result))





# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

#Iterate through the dictionary
fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']


for key , value in basket_items.items():
    if key in fruits:
        fruit_count += value
    else:
        not_fruit_count += value
        
print(not_fruit_count)
print(fruit_count)

# print('Fruits count {} and non Fruits count is {}'.format(fruit_count, not_fruit_count))) - idk 
print("There are {} fruits in the basket and non fruit count is {}.".format(fruit_count, not_fruit_count))







#Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.
#For example, if limit is 40, your code should set the nearest_square to 36.

# OPTION1
limit = 195
i = 1 
while i**2 < limit:
    i+=1
print((i-1)**2)


# OPTION2
limit = 196
num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)








# Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0 
list_sum = 0 
i = 0 
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list):
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1
              
print (count_odd)
print (list_sum)






# NEW TOPIC: Break, Continue: COLLECT ALL ITEMS UNDER 100 
manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]
weight = 0 
items = []

for item, weights in manifest:
     if weight >= 100:
          break
     elif weight + weights > 100:
          continue
     else:
          items.append(item)
          weight += weights

print(weight)
print(items)





#Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
for headline in headlines:
   news_ticker += headline +" "
   if len(news_ticker) > 140:
        news_ticker = news_ticker[:140]
        break
print(news_ticker)





# Prime numbers are whole numbers that have only two factors: 1 and the number itself. The first few prime numbers are 2, 3, 5, 7.

# For instance, 6 has four factors: 1, 2, 3, 6.
# 1 X 6 = 6
# 2 X 3 = 6
# So we know 6 is not a prime number.

# In the following coding environment, write code to check if the numbers provided in the list check_prime are prime numbers.

# If the numbers are prime, the code should print "[number] is a prime number."
# If the number is NOT a prime number, it should print "[number] is not a prime number", and a factor of that number, other than 1 and the number itself: "[factor] is a factor of [number]".


# Your code should check if each number in the list is a prime number

# MY CODE
# check_prime = [26, 39, 51, 53, 57, 79, 85]
# not_prime=[]
# prime=[]
# for num in check_prime:
#     for i in range (2, num):
#         if (num % i) == 0:
#             not_prime = not_prime.append(num)
#             # print("{} is not a prime cuz {} is a factor for {}".format(num, i, num))
#             break
#         if (num % i) != 0:
#             prime = prime.append(num)
#             # print("{} is Prime Number".format(num))
            
# print(not_prime, prime)
    
    
# # ##CORRECT CODE
## iterate through the check_prime list
check_prime = [26, 39, 51, 53, 57, 79, 85]
for num in check_prime:

## search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):

## number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break

## otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num -1:    
            print("{} IS a prime number".format(num))



# ZIP AND ENUMARATE: zip and enumerate are useful built-in functions that can come in handy when dealing with loops.
# For example: 
# letters = ['a', 'b', 'c']
# nums = [1, 2, 3]

# for letter, num in zip(letters, nums):
#     print("{}: {}".format(letter, num))

# letters = ['a', 'b', 'c', 'd', 'e']
# for i, letter in enumerate(letters):
#     print(i, letter)



#TASK1: Each string should be formatted as label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4.
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
points = []


for point in zip(labels, x_coord, y_coord, z_coord):
   points.append("{}: {}, {}, {}".format(*point))
 
print(points)

for point in points:
    print(point)



# CAST NAMES TURN INTO LIST AND DICT

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

# list
cast = zip(cast_names, cast_heights)
finalCast = list(cast)
print(finalCast)

# dictionary
cast = zip(cast_names, cast_heights)
finalCast = dict(cast)
print(finalCast)



# Quiz: Enumerate (HARD FOR ME)
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# iterate using for loop and adding (i) index, (ii) value in enumerate(your_list):
for num, character in enumerate(cast):
    cast[num] = character +" " + str(heights[num])
print(cast)


# LIST COMPREHENSION
# new_list = [expression for item in iterable] 
# for example:
capitalized_cities = [city.title() for city in cities]
print(capitalized_cities)

# CONDITIONALS
squares = [x**2 for x in range(9) if x % 2 == 0]
print(squares)

squares= [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares)
