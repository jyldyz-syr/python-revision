import math 



#TASK: use try amd except (finally) to receive a number and catch errors 
while True:
    try:
        x=int(input('Enter a num: '))
        # print('success')
        break
    except ValueError:
        print("not a valid num")
    except KeyboardInterrupt:
        print("not a valid num")
        break
    finally:
        #finally will run no matter what (used to clean up)
        print('done')






#TASK: Add a try-except block to make sure no ZeroDivisionError occurs.

def party_planner(cookies, people):
    leftovers = None
    num_each = None
    # TODO: Add a try-except block here to
    #       make sure no ZeroDivisionError occurs.
    try:
        num_each = cookies // people
        leftovers = cookies % people
        return(num_each, leftovers)
    
    except ZeroDivisionError:
        print('please enter a number >0')

party_planner(5,6)





# # TASK: initiate empty list to hold user input and sum value of zero
user_list = []
list_sum = 0

# seek user input for ten numbers 
for i in range(10):
    userInput = input("Enter any 2-digit number: ")
    try:
       number = userInput
       user_list.append(number)
       if (number % 2 == 0):
           list_sum += number
    except ValueError:
        print('enter correct value as a number')

print("user_list: {}".format(user_list))
print("The sum of the even numbers in user_list is: {}.".format(list_sum))



# import factorial func from python lib to test how it works
print(math.factorial(4))



# EXAMPLE function for ITERATORS & GENERATORS help you work with sequences of data efficiently, either by allowing you to loop through items one by one (iterators) or by generating values on-the-fly, conserving memory (generators).
def squares(n):
    for i in range(n):
        yield i ** 2

squared_numbers = squares(5)

for num in squared_numbers:
    print(num)




#TASK: Implement my_enumerate
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    count = start
#Inside the loop, you use the yield keyword to generate a pair of values:
    for element in iterable:
        yield count, element
#count: The current enumeration count.
#element: The current element from the iterable.
        count += 1
#After yielding, you increment the count by 1, effectively updating it for the next iteration.

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

#TASK: Implement a generator function, chunker, that takes in an iterable and yields a chunk of a specified size at a time.

def chunker(iterable, size):
    # Implement function here
    for i in range(0, len(iterable), size):
       yield iterable[i:i+size]


for chunk in chunker(range(25), 4):
    print(list(chunk))



