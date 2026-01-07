#создать шаблон в файле template.html c HTML-кодом  для отображения списка пользователей (имя и email каждого пользователя) затем через скрипт создать список пользователей, передать его в шаблон и отобразить результат на экране 
import os
from jinja2 import Environment, FileSystemLoader

# 1. Создаем список пользователей (список словарей)
users_list = [
    {'name': 'Иван Петров', 'email': 'ivan.petrov@example.com'},
    {'name': 'Мария Сидорова', 'email': 'maria.sidorova@example.com'},
    {'name': 'Алексей Иванов', 'email': 'alexey.ivanov@example.com'}
]

folder_name = '/home/egorpc/python/dz27ex4'
os.chdir(folder_name)


env = Environment(loader=FileSystemLoader('.'))    # 2. Настраиваем загрузчик шаблонов,  FileSystemLoader ищет шаблоны в текущей директории
template = env.get_template('template.html')

# 3. Рендерим шаблон, передавая список пользователей
html_output = template.render(users=users_list)

# 4. Выводим результат
print(html_output)
