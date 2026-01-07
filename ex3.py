#создать пустую директорию mydir перейти в нее и там создать 3 файла file1-3.txt
import os  # Импортируем модуль os для работы с файловой системой

dir_name = "mydir"
files = ["file1.txt","file2.txt","file3.txt"]
files_path = ["mydir/file1.txt","mydir/file2.txt","mydir/file3.txt"]


# 2. Создаем директорию (если она уже есть, ничего не произойдет)
try:
    os.makedirs(dir_name, exist_ok=True) # exist_ok=True предотвращает ошибку, если папка уже существует
    print(f"Директория '{dir_name}' создана или уже существует.")
except OSError as e:
    print(f"Ошибка при создании директории {dir_name}: {e}")

# 3. Создаем и записываем файлы file1-3.txt
index=0
try:
    for file_name in files:
        with open(files_path[index], 'w', encoding='utf-8') as f: # Открываем файл
           f.write(f"Это содержимое файла {files[index]} .\n") # Записываем текст  
        print(f"Файл '{files_path[index]}' создан в '{dir_name}'.")
        index += 1
        
except IOError as e:
    print(f"Ошибка при записи в файл {file_path}: {e}")

# 4. Читаем директорию  mydir

items = os.listdir(dir_name)  # Получаем список файлов в директории 

print(f"Содержимое папки {dir_name}:")
for item in items:
    print(item)
