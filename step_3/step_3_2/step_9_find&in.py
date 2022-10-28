#s = 'My Name is Julia'

# if 'Name' in s:
#   print('Мы смотрим есть ли переменная Name в под')

index = s.find('Name')
print(index, '- Индекс переменной')
if index != -1:
    print(f'Substring found at index {index}')
