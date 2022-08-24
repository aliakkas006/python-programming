# take user input:
# username = input("name: ")
# print(f"Your name is: {username} ")

# function:
# def add_two_num(num_1, num_2):
#     return num_1 + num_2


# sum_ = add_two_num(1, 2)
# print(sum)

# list:
# grocery_list = ["tomato", "potato", "rice", "apple"]
# grocery_list.sort()
# grocery_list.append("dal")
# grocery_list.pop()
# print(grocery_list)

# li = list()
# li.append("water")
# li.append("salt")
# li.append("vegetables")
# li.pop()
# print(li[-1])

# numbers = [50, 62, 12, 23, 5, 100, 2, 45, 1]
# print(numbers)
# sorted_numbers = sorted(numbers)


# print(sorted_numbers)

# conditional statement:
# def show_grade(grade):
#     print(f"Your grade is: {grade}")


# marks = int(input("Enter your marks: "))
# print(type(marks))
# if marks >= 80:
#     show_grade('A+')
# elif 70 <= marks < 80:
#     show_grade('A')
# elif 60 <= marks < 70:
#     show_grade('A-')
# elif 50 <= marks < 60:
#     show_grade('B')
# elif 40 <= marks < 50:
#     show_grade('C')
# elif 35 <= marks < 40:
#     show_grade('D')
# else:
#     show_grade('F')


# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False


# loop:
# i = 0
# even_num_list = []
# odd_num_list = []
# user_input = int(input("Limit :"))

# while i <= user_input:
#     if is_even(i):
#         even_num_list.append(i)
#     else:
#         odd_num_list.append(i)
#     i = i + 1
#
# print(f"Even numbers = {even_num_list} ")
# print(f"Odd numbers = {odd_num_list} ")

# for value in range(0, user_input):
#     print(value)
#     if is_even(value):
#         even_num_list.append(value)
#     else:
#         odd_num_list.append(value)
#
# print(f"even nums = {even_num_list}")
# print(f"odd nums = {odd_num_list}")

# grocery = ["tomato", "potato", "rice", "water", "milk", "coconut"]
#
# for item in grocery:
#     if item == "water":
#         continue
#     print(item)  # print all the items except water

for i in range(0, 50, 2):   # range(initial_value, stop_value, increment_value)
    print(i)
