import os

# Получаем список файлов
file_list = os.listdir()
# Инициализируем список кортежей (file, text)
data = []
# Инициализируем строку вывода для записи в файл
output = ''

# Получаем все файлы .txt из директории
for file in file_list:
    if '.txt' in file and file != 'recipes.txt':
        with open(file, 'r', encoding='utf-8') as f:
            file_text = f.readlines()
            # получим и отсортируем позже список кортежей вида [(file, [lines])]
            data.append((file, file_text))
data = sorted(data, key=lambda content: len(content[1]))  # получим и отсортируем список кортежей по длине текста

# Формируем строку вывода из сортированного списка кортежей
for file, text in data:
    output += f'{file}\n{len(text)}\n'
    for string in text:
        output += f'{string}'
    output += '\n'
print(output)

