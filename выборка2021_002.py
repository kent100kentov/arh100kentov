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
r1 = input ("введите формат: CR2, CR3, JPG, jpg или другой: ")
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
try:
    os.makedirs( a + "Print/10")
except FileExistsError:
#    print()
    try:
        os.makedirs( a + "print/13")
    except FileExistsError:
#    print()
        try:
            os.makedirs( a + "print/20")
        except FileExistsError:
            print("директория существует")
#folder = "'a' + 'Print'"
os.chdir(a + "Print")
print("Текущая директория:", os.getcwd())
print('скопируйте или проверьте файлы\nв директории ' + a + 'Print')
while True:
    n1 = input ("Введите номер по списку(или stop для остановки): ")
# удалим случайные лишние пробелы
    n1 = n1.strip()
    if n1 == 'stop':
        break
    n = "n"
    print ( a + n1 + n + ' выбор фото ' + '10x15' )
    f10 = input('запишите номера фото через пробел : ').split()
    print ( a + n1 + n + ' выбор фото ' + '13x20' )
    f13 = input('запишите номера фото через пробел : ').split()
    print ( a + n1 + n + ' выбор фото ' + '20x30' )
    f20 = input('запишите номера фото через пробел : ').split()
# вывод результата списков для контроля
    print(a + n1 + n + ' конец выбора ' )
    f10.sort()
    f13.sort()
    f20.sort()
    print(f10)
    print(f13)
    print(f20)
    print("Ждите, идет копирование файлов!")

#формирование словарей типа {112: 3, 222: 2} слово:ключ
    data = {}
    for e in f10:
        data[e] = data.get(e, 0) + 1

    data10 = data
#    print(data10)

    data = {}
    for e in f13:
        data[e] = data.get(e, 0) + 1

    data13 = data
#    print(data13)


    data = {}
    for e in f20:
        data[e] = data.get(e, 0) + 1

    data20 = data
#    print(data20)

    for x in data10:
        y = (data10.get(x))
        y = int(y)
        while y > 1:
            y -= 1
            try:
                shutil.copy(x + '.' + r1, '10\\' + n1 + '=' + x + '_'*y + '.' + r1)
            except FileNotFoundError:
                print('файла 10х15 нет, проверьте номер:', x)
        try:
            shutil.copy(x + '.' + r1, '10\\' + n1 + '=' + x + '.' +r1)
        except FileNotFoundError:
            print('файла 10х15 нет, проверьте номер:', x)

    for x in data13:
        y = (data13.get(x))
        y = int(y)
        while y > 1:
            y -= 1
            try:
                shutil.copy(x + '.' + r1, '13\\' + n1 + '=' + x + '_'*y + '.' + r1)
            except FileNotFoundError:
                print('файла 13х20 нет, проверьте номер:', x)
        try:
            shutil.copy(x + '.' + r1, '13\\' + n1 + '=' + x + '.' + r1)
        except FileNotFoundError:
            print('файла 13х20 нет, проверьте номер:', x)

    for x in data20:
        y = (data20.get(x))
        y = int(y)
        while y > 1:
            y -= 1
            try:
                shutil.copy(x + '.' + r1, '20\\' + n1 + '=' + x + '_'*y + '.' + r1)
            except FileNotFoundError:
                print('файла 20х30 нет, проверьте номер:', x)
        try:
            shutil.copy(x + '.' + r1, '20\\' + n1 + '=' + x + '.' + r1)
        except FileNotFoundError:
            print('файла 20х30 нет, проверьте номер:', x)

#    print("Ждите, идет копирование файлов!")
