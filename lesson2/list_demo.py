'''
Изменения!

'''

x = 10.0 + 2
y = 100
z = -10
test_str_value = 'hello'

our_first_list = [x, y, z]
# print(type(our_first_list))
# print(type(our_first_list[0]))
# print(help(our_first_list))

x = x + 1  # x += 1

our_first_list.append(test_str_value)
print(our_first_list)
####изъятие элементов#####
'''
# our_string_back = our_first_list.pop()
# print(our_string_back)
our_first_list.pop()  # последний элемент по умолчанию
print(our_first_list)
our_first_list.pop(0)
print(our_first_list)
'''
number_list = []
for i in range(10):
    number_list.append(i)

print(number_list)
print(number_list[1])
'''
length_of_list = len(number_list)
print(length_of_list)
print(number_list[length_of_list-1])
print(number_list[-4])
'''

print(number_list[1:5:1])  # первый (старт) включается в список, конец - нет
print(number_list[5:1:-1])
'''
random_list[start_point:end_point:step]
range(start, end, step)
'''
print(number_list[::-2])

# number_list.append(our_first_list)
print(number_list)

for element in number_list[2::2]:
    print(element)

long_long_list = [1, 2, 3, 4,
                  5, 6, 7, 8,
                  9, 9, 10, 11]

tuple_long_long_list = tuple(long_long_list)
long_long_list = list(tuple_long_long_list)
