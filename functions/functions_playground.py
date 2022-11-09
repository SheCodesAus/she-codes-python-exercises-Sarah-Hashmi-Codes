#function syntax
# def name_of_function():
#     '''
#     docstring explains function
#     this is a function that says "hello!"
    
#     '''
#     print("hello!")


# name_of_function()

# def create_greeting(name):
#     greeting = f"hello,{name}"
#     print(greeting)

# create_greeting("Sarah")
# create_greeting("Alyan")
# create_greeting("Adeel")


# def add_function(num1, num2):
#     sum = num1 + num2
#     print(sum)
#     return sum

# result_of_function = add_function(1,2)    (storing result)
# print(result_of_function)



# def multi_function(num):
#     multi_3 = 3*(num)

#     #print(multi_3)
#     return multi_3

# result_of_function = multi_function(2)
# print(result_of_function)


# def convert_cm_to_in(length_cm):
#     length_in_inches = length_cm/2.54
#     print(length_in_inches)
#     return length_in_inches
    

# length_of_closet_in_inches = convert_cm_to_in(50)



# def convert_in_to_cm(length_in):
#     length_in_cm = length_in * 2.54
#     print(length_in_cm)
#     return length_in_cm

# def convert_f_in_c(temp):
#     temp_in_c=(temp-32)/2
#     print(temp_in_c)
#     return(temp_in_c)

# temp = int(input("Enter Temp in F: "))
# print(temp)

# length_of_closet_in_inches = convert_in_to_cm(50)


# def calculate_mean(a,b):
#     total = a + b
#     mean = total/2
#     return mean

# def print_mean(a,b):
#     total = a + b
#     mean = total/2
#     print(mean)

# result_return = calculate_mean(3,4)
# result_print = print_mean(3,4)
# print('=========')
# print(result_return)
# print(result_print)

# print(calculate_mean)



# def temp_in_f(Temperature):
#     temp=(Temperature-30)/2
#     print(temp)
  
# Temperature = int(input("Temp in f is: "))
# temp_in_f(Temperature)


# def number(num):
#     if (num %2) == 0:
#         print("True")
#     else:
#         print("False")

# num = int(input("Enter a number: "))
# number(num)

# def cost(price_per_unit,num_unit):
#     cost=price_per_unit * num_unit
#     print('${:,.2f}'.format(cost))

# price_per_unit = float(input("Enter price: "))
# num_unit = int(input("Enter number per units: "))
# cost(price_per_unit,num_unit)

# number = 10
# if number > 11: 
#   print(0)
# elif number != 10:
#   print(1)
# elif number >= 20 or number < 12:
#   print(2)
# else:
#   print(3)


def color_translator(color):
	if color == red:
		print(#ff0000)
	elif color == green:
		print(#00ff00)
	elif color == blue:
		print(#0000ff)
	else:
		color != ("red", "green", "blue")
	return unknown
