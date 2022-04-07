salary_k = (0.5, 1.0, 'vetka', (0, 1))
# print(help(salary_k))
print(salary_k.index('vetka'))
print(salary_k[::-1])

from_tuple = salary_k[1:3]
print(id(from_tuple), id(salary_k))
tuple_from_list = tuple(list_from_tuple)
print(tuple_from_list)
for tuple_element in salary_k:
    print(tuple_element)
