# Задача 5. Вариант 0.
# Напишите программу, которая бы при запуске случайным образом отображала название
# одношо из четырех животных, встреченных Колобком в лесу.

# Krasnikov A. S.
# 02.03.2016

import random

print("Программа случайным образом отображает название одного из четырех животных, встреченных Колобком в лесу.")

animal = random.randint(1,4)

print('\nКоловок встретил', end=' ')

if animal == 1 :
    print('зайца')
elif animal == 2 :
    print('волка') 
elif animal == 3 :
    print('медведя') 
else :
    print('лису')


input("\n\nНажмите Enter для выхода.")