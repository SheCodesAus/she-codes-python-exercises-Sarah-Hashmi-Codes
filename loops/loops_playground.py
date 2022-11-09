# for loop
# my_iterable = [1, 2, 3,4,5,6,7,8]

# for item in my_iterable:
#     #some code here
#     print(item)

# for num in range(1, 10):  (start:Stop)
    # print(num)


# for num in range(1,11,2):  (start:Stop:step)
#     print(num)

# for num in range(0,101):
#     print(num)

# for num in range(0,101,5):
#     print(num)

# my_name = "Sarah"

# for letter in my_name:
#     print(letter)

from re import M
from stat import IO_REPARSE_TAG_APPEXECLINK


wishlist = ["igloo", "chicken", "donut toy"]

# for item in range(len(wishlist)):
#     print(wishlist[item])

# for item in wishlist:
#     print(f"Chilli wants: {item}")

# chilli_wishlist = [["igloo"],["donut toy", "tennis ball", "crocodile toy"],["chicken", "peanut butter"],["cardboard box", "kong", "dig mat"]]


# for category in chilli_wishlist:
#     for item in category:print(item)

#While Loops

# some_boolean_condition = True
# while some_boolean_condition:
#     #do somethin

# counter = 10
# while counter <= 10:   
#     print(counter)
#     #counter = counter + 1 
#     counter += 1


# guess = ""
# while guess != "a":
#     guess = input("Guess a letter:")


# num = int(input("Enter a number: "))

# for i in range(1,num+1):
#     print(f"{num} * {i} = {num*i}")


# num = int(input("Enter a number : "))
# total = 0
# for i in range(1,num+1):
#     total += i

# print(total)


# N = int(input("Please input an integer: "))
# i = 1
# x = range(1, N + 1)
# for i in x:
#     nums = range(1, i + 1)
# print(int(sum(nums)))


# num = [3, 5, 9, 1] 
# for i in range(0,1):
#     print(sum(num))

# num = [-3, -5, 9, 1]
# for i in range(0,1):
#     print(sum(num))

# mailing_list = [
# ["Chilli", "chilli@thechihuahua.com"],
# ["Roary", "roary@moth.catchers"],
# ["Remus", "remus@kapers.dog"],
# ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
# ["Ivy", "noreply@goldendreamers.xyz"],
# ]


# for i in mailing_list:
#     print(f"{i[0]}:{i[1]}")
    
#While Loops Excersises

# # Q1

# sum = 0 
# number = ""
# while number > 0:
#     number = int(input('Enter a number: '))
#     if number > 1:
#         sum = sum + number
    
# print(sum)


# number = 0
# sum = 0

# while number != "":
#     sum += int(number)
#     number = input("Enter a number" )


#     sum = 0
#     while True:
#         number = input("Enter a number: ")

#     if number == "":
#         break
#     else:
#         sum += int(number)

# print(sum)



# Q2

# number = int(input("Enter a number: ")) 
# counter = 0
# while counter <= number:
#     if counter % 2 == 1:
#       print(counter)
#     counter += 1


# Q3

# guess = int
# while guess != 25:
#     guess = int(input("Guess the number: "))
#     if guess > 25:
#         print("Too High!")
#     if guess < 25:
#         print("Too Low!")
#     if guess == 25:
#         print("Correct!")


# correct_number = 7
# guessed_number = 0

# while guessed_number != correct_number:
#     guessed_number= int(input("Guess the number: "))

#     if guessed_number < correct_number:
#         print("Too Low")
#     elif guessed_number > correct_number:
#         print("Too high")
#     elif guessed_number == correct_number:
#         print("Correct")

# While Loops Extension

# Q1

# groceries = [
# ["Baby Spinach", 2.78],
# ["Hot Chocolate", 3.70],
# ["Crackers", 2.10],
# ["Bacon", 9.00],
# ["Carrots", 0.56],
# ["Oranges", 3.08]
# ]

# for item in groceries
#     # item = ["Baby spinach", 2.78]
#     name_of_item = item[0]
#     num_items = (f"How many of {name_of_item}?")
#     price_per_unit = item[1]
#     cost_of_item = num_items * price_per_unit
#     item.append(cost_of_item)
    

# print("==Izzy's Food Emporium==")
# for item in groceries:
#     name = item[0]
#     cost = item[2]
#     print(f"{name}\t{cost}")
# print("==========================")
# print(f"\t\t${sum}")


#2

# string_input = input("Please enter a string: ")

# counter = 9
# for letter in string_input:
#     print(f"{counter} {letter}")
#     counter += 1

#3

# number = 5

# for pyramid_row in range(6): 
#         # print(pyramid_row)
#         pyramid_row_output = "*" * (pyramid_row)
#         print(pyramid_row_output)



# size = int(input("Pyramid size: "))

# for i in range(1, size+1):
#     pyramid_row = "*" * (i*2 - 1)
#     padding_row = " " * (size - i)
#     print(f"{padding_row}{pyramid_row}{padding_row}")

# n = 5

# for i in range(n):
#     for j in range (n-i-1):
#         print("", end=" ")
#     for j in range(2*i + 1):
#         print("*", end="")
#     print()



name_list = ["Joy", "bunny", "ash", "kitty"]

# print(f"Hi {name_list[0]})")



# # for loop
# for name in name_list:
#    print(f"Hi {name}")
   
#    input("_____________") 


#while loop
counter = 0
while counter < len(name_list):
    print(f"hi {name}")
    print(counter)
    counter = counter + 1
    name = name_list[counter]
    print(f"hi{name}")
    counter = counter + 1
    input("__________")


# example 2
import random

budget = 100
how_much_spent = 0

def buy_stuff():
    cost_of_item = random.randit(0,20)
    return cost_of_item

how_much_spent += buy_stuff()
print(f"total spent: {how_much_spent}")

if how_much_spent < budget:
    print(f"total spemt: {how_much_spent}")


for i in range(0,100):
    how_much_spent += buy_stuff()
    print(f"total spent:{how_much_spent}")

    input("_____")
    if how_much_spent > budget:
        break


while how_much_spent < budget:
    how_much_spent += buy_stuff()
    print(f"totals spent: {how_much_spent}")

    input("____")