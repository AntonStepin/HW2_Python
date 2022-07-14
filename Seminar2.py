
import datetime
from timeit import default_timer as timer

# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def sum_of_numbers_in_number(number): 
    numbers = []
    sum = 0
    count_in_numbers = 0
    minus = False
    for char in str(number):
        if char.isdigit() and minus == False:
            numbers+=char
            sum += int(numbers[count_in_numbers])
            count_in_numbers+=1
        elif char.isdigit() and minus == True:
            numbers+= char
            sum += -abs(int (numbers[count_in_numbers]))
            minus = False
            count_in_numbers+=1    
        elif char == '-':
            minus = True
    print(sum)

# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def product_of_number(number):
    print(type(number))
    if type(number) != int:
        print("You enter not a digit")
        exit
    else:    
        result = []
        for i in range(1,number+1):
            temp = 1
            for j in range (1,i+1):
                temp *=j
            result.append(temp)
        print(result)

# 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

def numerical_sequence (number):
    if type(number) == int:
        lst_of_number = {}
        for i in range(1,number+1):
            lst_of_number[i] = (1+1/i)**i
        print(lst_of_number)
    else:
        print('You enter not a integer')

# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

#Без использования библиотеки Random у меня получилось прийти только к выводу, что мы можем реализовать выдачу случайного числа 
# с помощью, например, библиотеки datetime, но использовать данное число мы можем только как ID в базах и т.д. 
# (или если сложить элементы или использовать различные операции %10 и другие, то будет случайное число, но с узким разбросом), так как 
# если нам потребуется вывод случайных чисел в ряд циклом for, то из-за скорости работы цикла произойдет выдача одинаковых чисел. 
# Пример решение с datetime: 

def occasional_number():
    moment_date = datetime.datetime.today()
    random = int (f"{moment_date.year}" + f"{moment_date.month}" + f'{moment_date.day}' + f'{moment_date.hour}' + f'{moment_date.microsecond}')
    print(random)

# Еще пример с timer и XOR
def sporadic_number():
    oper_moment = timer()
    textp = str(oper_moment).split(".")
    randomnum = (int(textp[0])^int(textp[1]))%10
    print(randomnum)

# А так "серьезным" и одним из лучших вариантов является метод реализованный изначально в Python по методу вихря Мерсенна, 
# на GitHub есть варианты его реализации на языке Python (переписывать я его не стал))).
#последний вариант можно доработать под выдачу чисел двузначных и далее и использовать далее для перемешивания списка






