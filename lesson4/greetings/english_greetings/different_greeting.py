def create_greating(name):
    greeting = f'Hello, dear {name.capitalize()}'
    return greeting


def create_another_greating(name):
    greeting = f'Hello again, dear {name.capitalize()}'
    return greeting


if __name__ == '__main__': #проверка что апускается как скрипт, а не дли импорта модулей
    print(create_another_greating('Basil'))
    print(create_greating('Anna'))