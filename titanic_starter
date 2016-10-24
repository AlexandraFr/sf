# Практическая работа

#### Задание 1: Скачайте файл с данными о погибших на титанике
import requests
import os

def to_str(lines):
    new_to_str = []
    for bytes in lines:
        new_to_str.append(str(line, 'utf-8') + '\n')
    return new_to_str
    # Функция возвращает список преобразованных строк,
    # а принимает список байтовых строк
    
    # Отдельно взятую строку байт можно преобразовать в строку
    # символов следующим образом: str(line, 'utf-8')+'\n'
    # Символ перехода на новую строку добавляется, чтобы при
    # записи в файл каждая запись начиналась с новой строки
    
    # Удалите pass и представьте ваше решение



def download_file(url):
    # Делаем GET-запрос по указанному адресу
    response = requests.get(url)
    # Получаем итератор строк
    text = response.iter_lines()
    # Каждую строку конвертируем из массива байт в массив символов
    text = to_str(text)

    # Если файла не существует, то создаем его и записываем данные
    if not os.path.isfile("titanic.csv"):
        with open("titanic.csv", "w") as f:
            f.writelines(text)
    return text

#data = download_file("https://raw.githubusercontent.com/haven-jeon/introduction_to_most_usable_pkgs_in_project/master/bicdata/data/titanic.csv")

# Если вы успешно выполнили первое задание, то файл можно не скачивать
# каждый раз, а вместо этого данные читать из файла. Расскомментируйте
# следующую строку и закомментируйте предыдущую
data = open('titanic.csv')

#### Задание 2: Получаем список словарей
# Модуль для работы с файлами в формате CSV
import csv

reader = csv.DictReader(data)
reader.fieldnames[0] = 'lineno'
titanic_data = list(reader)

# Модуль для красивого вывода на экран
from pprint import pprint as pp
pp(titanic_data[:2])
pp(titanic_data[-2:])


#### Задание 3: Узнать количество выживших и погибших на Титанике
def survived(tit_data):
    surv = 0
    notsurv = 0
    for dict in tit_data:
        if dict.get('survived') == '1':
            surv += 1
        else:
            notsurv += 1
    tuple = (surv, notsurv)
    return tuple
    # Функция возвращает кортеж из двух элементов: количество
    # выживших и число погибших


pp(survived(titanic_data)) # (500, 809)


#### Задание 4: Узнать количество выживших и погибших на Титанике
#### по отдельности для мужчин и женщин
from operator import itemgetter
from itertools import groupby
def survived_by_sex(tit_data):
    list_male = []
    list_female = []
    for dict in tit_data:
        if dict.get('sex') == 'male':
            list_male.append(dict)
        else:
            list_female.append(dict)
    control_list = [('female', (survived(list_female))), ('male', (survived(list_male)))]
    return control_list
    # Функция возвращает список кортежей из двух элементов вида:
    # (пол, (количество выживших, число погибших))

    # Подумайте над использованием функции survived()


pp(survived_by_sex(titanic_data)) # [('female', (339, 127)), ('male', (161, 682))]

#### Задание 5: Узнать средний возраст пассажиров
def average_age(tit_data):
    count = 0
    sum = 0
    for dict in tit_data:
        if dict['age'] == 'NA':
            pass
        else:
            sum += float(dict.get('age'))
            count += 1
    average_age = sum / count
    return average_age
    # Функция возвращает средний возраст пассажиров


pp(average_age(titanic_data)) # 29.88


#### Задание 6: Узнать средний возраст мужчин и женщин по отдельности
def average_age_by_sex(tit_data):
    list_male = []
    list_female = []
    for dict in tit_data:
        if dict['sex'] == 'male':
            list_male.append(dict)
        else:
            list_female.append(dict)
    control_list = [('female', (average_age(list_female))), ('male', (average_age(list_male)))]
    return control_list
    # Функция возвращает список кортежей из двух элементов вида:
    # (пол, средний возраст)

    # Подумайте над использованием функции average_age()

pp(average_age_by_sex(titanic_data)) # [('female', 28.68), ('male', 30.58)]


#### Задание 7: Сколько детей и взрослых было на борту:
def children_and_adults(tit_data):
    children, teens, adults = 0, 0, 0
    for dict in tit_data:
        if dict['age'] == 'NA':
            pass
        elif float(dict.get('age')) < 14:
            children += 1
        elif float(dict.get('age')) < 18:
            teens += 1
        else:
            adults += 1
    list_age = [children, teens, adults]
    return list_age
#### Получить группы в следующих диапазонах возрастов:
#### [0-14), [14-18), [18-inf]
pp(children_and_adults(titanic_data))

#### Задание 8: Сколько в каждой группе выживших
def survived_by_age(tit_data):
    list_children = []
    list_teens = []
    list_adults = []
    for dict in tit_data:
        if dict['age'] == 'NA':
            pass
        elif float(dict.get('age')) < 14:
            list_children.append(dict)
        elif float(dict.get('age')) < 18:
            list_teens.append(dict)
        else:
            list_adults.append(dict)
    control_list = [('children', (survived(list_children))), ('teens', (survived(list_teens))),
                    ('adults', (survived(list_adults)))]
    return control_list

pp(survived_by_age(titanic_data))
#### Задание 9: Сколько в каждой группе выживших по отдельности для
#### мужчин и женщин
def survived_by_age_and_age(tit_data):
    list_male = []
    list_female = []
    for dict in tit_data:
        if dict.get('sex') == 'male':
            list_male.append(dict)
        else:
            list_female.append(dict)
    control_list = [('male', survived_by_age(list_male)), ('female', survived_by_age(list_female))]
    return control_list
pp(survived_by_age_and_age(titanic_data))
