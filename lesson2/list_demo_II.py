x = 10.0
y = 100
z = -10
test_str_value = 'hello'

our_first_list = [x, [y, z]]

number_list = []
for i in range(20):
    number_list.append(i)
    if i % 10 == 0:
        # number_list[i] = 'cat'
        # number_list[i] = -i
        number_list.insert(i, 'cat')
        # print(number_list)
        # number_list.clear() #  про весь список

print(len(number_list))
print(number_list)
print(number_list.index('cat'))
number_list.insert(number_list.index('cat') + 1, 'dog')
# number_list.remove('cat')
print(number_list)
# print(number_list.count('cat'))
# number_list.append(our_first_list)
number_list.extend(our_first_list)

print(number_list)
# sorted_list = sorted(number_list, reverse=True)
# print(number_list)
# print(sorted_list)
# number_list.sort()  # если хотим изменить наш список
# print(number_list)



# print(help(number_list))