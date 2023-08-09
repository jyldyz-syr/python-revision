import math 

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


# initiate empty list to hold user input and sum value of zero
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

# import factorial func from python lib
print(math.factorial(4))