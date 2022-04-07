demo_str = 'Mama mila ramu.'
author = '(c) cat.'

demo_str += author
# demo_str += author
print(demo_str)
'''
конкатенация плохо
for_str = ''
for i in range(10):
    for_str += str(i)
    print(id(for_str))
    print(for_str)
'''
'''
лучше так
str_list = []
for i in range(10):
    str_list.append(str(i))
print(''.join(str_list))
'''
# print(demo_str.replace('.(c)', '. (c)'))
demo_str = demo_str.replace('.(c)', '. (c)')
demo_str = demo_str.replace('(c) ', '')
demo_str_list = demo_str.split('. ')
demo_str_list[-1] = demo_str_list[-1].upper().replace('A', 'a')
# print(' '.join(demo_str_list))
# print(demo_str_list[-1].isupper())


# print(help(str.replace))

for i in range(20):
    x = 20 - i * 0.1 ** 6
    # print('До конца осталось ', x, "с начала прошло ", i)
    test_f_string = f'До конца осталось {x:.5f},' \
                    f'с начала прошло {i}'
    print(test_f_string.upper())