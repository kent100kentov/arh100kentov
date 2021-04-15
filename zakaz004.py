#https://pythontutor.ru/lessons/lists/
#Методы split и join
#https://pythonru.com/osnovy/rabota-s-fajlami-v-python-s-pomoshhju-modulja-os
#смена директорий

import os
import shutil

# вывести текущую директорию
print("Текущая директория:", os.getcwd())
# изменить текущую директорию
z = input ("введите букву рабочего диска: ")
#удалим случайные лишние пробелы
os.chdir( 'C:')
z = z.strip()
os.chdir( z + ":")
print("Текущая директория:", os.getcwd())
s1 = input ("введите номер сада: ")
#удалим случайные лишние пробелы
s1 = s1.strip()
s = "s"
g1 = input ("введите номер группы: ")
#удалим случайные лишние пробелы
g1 = g1.strip()
g = "g"
a = (s1 + s + g1 + g)
print ( 'создаю каталог ' + a + 'Print')
# создаём каталог и несколько вложенных папок
# если директория уже есть будет ошибка
os.makedirs( a + "Print/10")
os.makedirs( a + "print/13")
os.makedirs( a + "print/20")
#folder = "'a' + 'Print'"
os.chdir(a + "Print")
print("Текущая директория:", os.getcwd())
print('скопируйте файлы в директорию ' + a + 'Print')
while True:
    n1 = input ("Введите номер по списку(или stop для остановки): ")
# удалим случайные лишние пробелы
    n1 = n1.strip()
    if n1 == 'stop':
        break
    n = "n"
    print ( a + n1 + n + ' выбор фото ' + '10x15' )
    f10 = input('запишите номера фото через - : ').split('-')
    print ( a + n1 + n + ' выбор фото ' + '13x20' )
    f13 = input('запишите номера фото через - : ').split('-')
    print ( a + n1 + n + ' выбор фото ' + '20x30' )
    f20 = input('запишите номера фото через - : ').split('-')
# вывод результата списков для контроля
    print(a + n1 + n + ' конец выбора ' )
    f10.sort()
    f13.sort()
    f20.sort()
    print(f10)
    print(f13)
    print(f20)
    print("Ждите, идет копирование файлов!")
# запись файлов по списку в поддиректории с переименовнием
    y = 0
    for x in f10:
        y = int(y)
        y += 1
        y = str(y)
        shutil.copy(x + '.CR3', '10\\'+ n1 +'='+ x + '--2021-' + y + '.CR3')
    y = 0
    for x in f13:
        y = int(y)
        y += 1
        y = str(y)
        shutil.copy(x + '.CR3', '13\\'+ n1 +'='+ x + '--2021-' + y + '.CR3')
    y = 0
    for x in f20:
        y = int(y)
        y += 1
        y = str(y)
        shutil.copy(x + '.CR3', '20\\'+ n1 +'='+ x + '--2021-' + y + '.CR3')
