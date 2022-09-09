# when we want to remove duplicates from a list we use set

x = set()
# print(type(x))
# print(x)

x.add(1)
# print(x)

x.add(2)
# print(x)

x.add(3)
# print(x)

x.add(3)
# print(x)

# for i in x:
#     print(i)

given_list = [1, 2, 3, 3, 4, 1, 5]
new_set = set()

for i in given_list:
    new_set.add(i)

print(new_set)
sum_1 = sum(new_set)
print(sum_1)

new_list = list()

for j in new_set:
    new_list.append(j)

print(new_list)
sum_2 = sum(new_list)
print(sum)
