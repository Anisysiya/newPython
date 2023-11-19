# Функция — это фрагмент программы, используемый многократно

# def function_name(x):
# body line 1
# ...
# body line n
# optional return

# Задание: Необходимо создать функцию sumNumbers(n), которая будет считать
# сумму всех элементов от 1 до n.
# Решение:
# 1. Необходимо создать функцию:
# def sumNumbers(n):

# 2. Реализовать решение задачи внутри функции
# def sumNumbers(n):
# summa = 0
# for i in range(1, n + 1):
# summa += i
# print(summa)

# 3. Спросим у пользователя число
# def sumNumbers(n):
# summa = 0
# for i in range(1, n + 1):
# summa += i
# print(summa)
# n = int(input()) # 5
# sumNumbers(n) # 15

#  что делает return:
# 1. Завершает работу функции
# 2. Возвращает значение
# def sumNumbers(n):
# summa = 0
# for i in range(1, n + 1):
# summa += i
# return summa
# n = int(input()) # 5
# print(sumNumbers(n)) # 15

# 1. function_file.py (Новый Python файл, в котором находятся функция f(x))
# def f(x):
# if x == 1:
# return 'Целое'
# elif x == 2.3:
# return 23
# return # выход из функции

# 2. working_file.py
# import function_file
# print(function_file.f(1)) # Целое
# print(function_file.f(2.3)) # 23
# print(function_file.f(28)) # None

# В Python можно перемножать строку на число.
# def new_string(symbol, count):
# return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...

# def new_string(symbol, count=3):
# return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12

# Возможность передачи неограниченного количества аргументов
# ● Можно указать любое количество значений аргумента функции.
# ● Перед аргументом надо поставить *.
# def concatenatio(*params):
# res = ""
# for item in params:
# res += item
# return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1')) # a1
# # print(concatenatio(1, 2, 3, 4)) # TypeError: ...

# 💡 Рекурсия — это функция, вызывающая сама себя
# При описании рекурсии важно указать, когда функции надо
# остановиться и перестать вызывать саму себя. По-другому говоря, необходимо
# указать базис рекурсии
# def fib(n):
# if n in [1, 2]:
# return 1
# return fib(n - 1) + fib(n - 2)
# list_1 = []
# for i in range(1, 10):
# list_1.append(fib(i - 2))
# print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

# Алгоритмом называется набор инструкций для выполнения некоторой задачи. В
# принципе, любой фрагмент программного кода можно назвать алгоритмом, но мы с
# Вами рассмотрим 2 самых интересных алгоритмы сортировок:
# ● Быстрая сортировка
# ● Сортировка слиянием

# Быстрая сортировка
# “Программирование это разбиение чего-то большого и невозможного на что-то
# маленькое и вполне реальное

# def quicksort(array):
# if len(array) < 2:
# return array
# else:
# pivot = array[0]
# less = [i for i in array[1:] if i <= pivot]
# greater = [i for i in array[1:] if i > pivot]
# return quicksort(less) + [pivot] + quicksort(greater)
# print(quicksort([10, 5, 2, 3]))

# ● 1-е повторение рекурсии:
# ○ array = [10, 5, 2, 3]
# ○ pivot = 10
# ○ less = [5, 2, 3]
# ○ greater = []
# ○ return quicksort([5, 2, 3]) + [10] + quicksort([])
# ● 2-е повторение рекурсии:
# ○ array = [5, 2, 3]
# ○ pivot = 5
# ○ less = [2, 3]
# ○ greater = []
# ○ return quicksort([2, 3]) + [5] + quicksort([]) # Важно! Не забывайте, что
# здесь помимо вызова рекурсии добавляется список [10]
# ● 3-е повторение рекурсии:
# ○ array = [2, 3]
# ○ return [2, 3] # Сработал базовый случай рекурсии
# На этом работа рекурсии завершилась и итоговый список будет выглядеть таким
# образом: [2, 3] + [5] + [10] = [2, 3, 5, 10]

# Сортировка слиянием

# def merge_sort(nums):
# if len(nums) > 1:
# mid = len(nums) // 2
# left = nums[:mid]
# right = nums[mid:]
# merge_sort(left)
# merge_sort(right)
# i = j = k = 0
# while i < len(left) and j < len(right):
# if left[i] < right[j]:
# nums[k] = left[i]
# i += 1
# else:
# nums[k] = right[j]
# j += 1
# k += 1
# while i < len(left):
# nums[k] = left[i]
# i += 1
# k += 1
# while j < len(right):
# nums[k] = right[j]
# j += 1
# k += 1
# 11
# nums = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(nums)
# print(nums)
