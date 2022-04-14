#лямбда функция - безымянная функция
'''
def create_greating(name):
    greeting = f'Hello, dear {name.capitalize()}'
    return greeting


list_of_names = ['basil', 'marina', 'natasha', 'ivan']

print(*map(create_greating, list_of_names))
print(*map(lambda x: f'Hello, dear {x.capitalize()}', list_of_names))

sorted_list_of_names = sorted(list_of_names)
print('Sorted', sorted_list_of_names)

sorted_list_of_names = sorted(list_of_names, key=lambda x: x[-1])
print('Sorted by last char', sorted_list_of_names)

print('Filtred by second char', *filter(lambda x: x[1] == 'a', list_of_names))

y = lambda x: x[1] == 'a'
print(y('cat'))
print(y('dog'))
'''

salaries = [1000, 500, 700, 72, 4200, 130, 6]

def get_reward(salary):
    additional_reward = ((salary * 0.3) / 12 + 365) / 16
    return additional_reward

for salary in salaries:
    print(get_reward(salary))

print(*map(get_reward, salaries))
print(*map(lambda salary: ((salary * 0.3) / 12 + 365) / 16, salaries))
