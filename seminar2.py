# name = "Ivan"
# #       0123
# print(name[0])
# foreach - C#
# for element in "Hello", 123, 34.125, True, 'a':
#     print(element * 2)
# 0: element = "Hello"
# 1: element = 123
# 2: element = 34.125
# ...
# range и for между собой НИКАК НЕ СВЯЗАНЫ!!!
# range(begin=необязательный(0), end=обязательный, step=необязательный(+1))
print(*range(5))
# # 0 1 2 3 4
# print(*range(5, 0, -1))
# print(*range(5, 13, 2))
# print(*range(2, 10))
# print(*range(0, 8, 2))


# for i in range(5):
#     # print(i, end=' ')
#     print(i, end='!\n')


# print(1, end=', ')
# print(2, end='. ')
# print(3, end='!\n')
# # print()
# print("Hello")


# print("Ivan")


# from numpy import arange


# for i in arange(0.0, 1.23, 0.01):
#     print(i)
# _______________________________________


# Задача №9. По данному целому неотрицательному n вычислите значение n!. 
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу
# используя цикл while
# Input:       5
# Output:    120

# n = int(input())
# f = 1
# while n > 0:
#     f = f * n       
#     n = n - 1       
# print(f)
# # ___________________________---


# number = int(input())
# multi = 1
# while number > 0:
#     multi = multi * number
#     number = number - 1
# print(multi)
# # _______________________________


# n = int(input("Введите целое неотрицательное число: "))
# factorial = 1
# i = 1
# # Умножаем числа от 1 до n на текущее значение факториала
# while i <= n:
#     factorial *= i
#     i += 1
# print("Факториал числа", n, "равен", factorial)
# # _______________________________________


# n = int(input("Input number: "))
# result = 1
# while n > 1:
#     result *= n # result = result * n
#     n -= 1
# print(result)
# #________________________



# Задача №11.
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи,
# выведите число -1.
# Input:     5
# Output:  6

# n = int(input('Введите длину ряда: '))
# f1 = f2 = 1
# print(f1, f2, end=' ')
# for i in range(1, n):
#     f1, f2 = f2, f1 + f2 
#     print(f2, end=' ')
##________________________


# A = int(input("Введите число: "))
# f1 = 0
# f2 = 1
# i = 2
# while f2 < A:
#     f1, f2 = f2, f1 + f2
#     i +=1
# if A != f2:
#     i = -1
# print(i)
##__________________________


# n = int(input('Введите число n: '))
# count = 3
# s = 1
# k =2
# next=0
# while next < n:
#     next = s+k
#     count += 1
#     s=k
#     k=next
# if next == n:
#     print(count+1)

# if next != n:
#     print(-1)
# if n == 2:
#     print(3)
##___________________________


# n = int(input("Введите число: "))
# first_fib = 0
# second_fib = 1
# i = 2 # Первые два числа уже известны
# while second_fib < n:
#     next_fib = first_fib + second_fib
#     # 0 + 1 = 1
#     # 1 + 1 = 2
#     first_fib = second_fib
#     second_fib = next_fib
#     i += 1
#     if second_fib > n:
#         i = -1
# print(i)
# __________________________



# Задача №15.
# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче.
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый
# арбуз? Помогите ему! Пользователь вводит одно число N – количество арбузов. 
# Вторая строка содержит N чисел, записанных на новой строчке каждое. 
# Здесь каждое число – это масса соответствующего арбуза
# Input:	5 -> 5 1 6 5 9
# Output:	1 9


# n = int(input())
# max = int(input())
# min = max
# for i in range(n-1):
#     i = int(input())
#     if i < min:
#         min = i
#     elif i > max:
#         max = i
# print(max, min)
##_____________________________


# n = int(input('Введите количество арбузов: '))
# minimum = 100000000
# maximum = 0
# for i in range(n):
#     weight = int(input('Введите массу арбуза: '))
#     if weight > maximum:
#         maximum = weight
#     if weight < minimum:
#         minimum = weight
# print(minimum, maximum)
##_______________________


# mass = []
# arb = int(input())
# for i in range(arb):
#     mass.append(int(input()))
# for i in range(arb):
#     max = min = mass[0]
#     if max < mass[i]:
#         max = mass[i]
#     if min > mass[i]:
#         min = mass[i]
# print(max, min)
##____________________________


# n = int(input("Введите кол-во арбузов: "))
# x = int(input("Введите массу арбуза: "))
# max_massa, min_massa =  x, x
# for i in range(n - 1):
#     x = int(input("Введите массу арбуза: "))
#     if max_massa < x:
#         max_massa = x
#     elif min_massa > x:
#         min_massa = x
# print(min_massa, max_massa)