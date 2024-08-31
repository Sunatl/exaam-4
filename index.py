# <!-- ### 1 Question
# Кадом методҳои модули datetime ва randome - ро медонед. Бо мисолҳо фаҳмонед.
# datetime baroi ruz va soatro nishon dodan date baroi ruz ro dar terminal nishon dodan va time soatro.va funcsiyaho diga masalan: timedelta,strftime,strptime:va gayraho:
# Random baroi elementhoro randomniy barovardan masalan hast randint az a to be ravadu elementoro randomniy barorad va hast choice va gayraho


# ### 2 Question
# Кадом методхо ва функсияхоро барои кор бо файл медонед.
# write, read,readlines
# modhoi on "r","w","r+","w+" 



# ### 3 Question
# Github чист? Командахои GitHub-ро фахмонед.
# masalan yak darakhte ki hamai pragramistho gam shuda kod hoi khudro roi mekunand,
# va on darakht ro masalan shokhahoyashro ziyod kunand va server vibr meknad 
# git push - baroi pushidan 
# git commit - baroi coment kardan
# git add . - baroi hami failro giriftan
# git init 
# git branch



# ### 1 Question
# Write a Python program to insert an element at a specified position into a given list.
# Напишите программу Python для вставки элемента в указанную позицию в заданный список.
# Барономае нависед дар Python, барои дохил кардани 
# [1, 1, 2, 3, 4, 4, 5, 1]
# # input
#     Enter an element: Sorbon
#     Index: 3
# # output
#     [1, 1, 2, "Sorbon", 3, 4, 4, 5, 1]

# <!-- task 1 -->
# lis = [1, 1, 2, 3, 4, 4, 5, 1]
# a = input("Enter an element: ")
# b = int(input("Index: "))
# lis.insert(b, a)
# print(lis)


# ### 2 Question
# Write program to print 2 days before, today, 2 days after / Напишите программу для печати позавчера, сегодня, послезавтра. / Барномаи нависед, то пареррӯз, имрӯз, фардои дигарро чоп кунад 
# from datetime import datetime, timedelta
# a = datetime.today()
# t = a - timedelta(days=2)
# t1 = a + timedelta(days=2)
# print("2 ruz pesh:", t.strftime('%Y-%m-%d'))
# print("Imruz:", a.strftime('%Y-%m-%d'))
# print("2 ruz bad:", t1.strftime('%Y-%m-%d'))


# ### 3 Question
# Write a program to subtract five days from the current date / Напишите программу, которая вычитает пять дней из текущей даты.
# Input: 17.02.2024           Output: 12.02.2024

# from datetime import datetime, timedelta
# i = "17.02.2024"
# d = datetime.strptime(i, "%d.%m.%Y")
# n = d - timedelta(days=5)
# o = n.strftime("%d.%m.%Y")
# print("Imruz:", i)
# print("5 ruz pesh:", o)


# ### 4 Question
# Create a function that takes a string and returns the sum of vowels, where some vowels are considered numbers (Exactly use dictionary.). Создайте функцию, которая принимает строку и возвращает сумму гласных, где некоторые гласные считаются числами (Обязательно используйте словари).(A=4, E=3, I=1, O=0, U=0) 

# Input                                           Output
# sum_of_vowels("Do I get the correct output?")   10

# def main(s):
#     v = {'A': 4, 'E': 3, 'I': 1, 'O': 0, 'U': 0}
#     t = 0
#     for i in s.upper():
#         if i in v:
#             t += v[i]
#     return t
# a = main("Do I get the correct output?")
# print(a)  


# ### 5 Task
# Create a python program to read line number N from the following file.
# Создайте программу Python для чтения строки номер N из следующего файла.
# my_file.txt -> Hello world
#                TEST
#                Tajikistan
#                An apple
# # input
#     3
# # otput
#     Tajikistan


# def main(filename, n):
#     with open(filename, 'r') as file:
#         s = file.readlines()
#         if 1 <= n <= len(s):
#             return s[n - 1].strip()
#         else:
#             return f"Error: Line {n} does not exist in the file."
# n = int(input())
# res = main('my_file.txt', n)
# print(res)






# ### 6 Question
# Write a program that replaces the content of all odd lines in a given file with a word that we input.
# Напишите программу, которая в заданном файле заменяет содержимое всех нечётных строк на слово, которое мы вводим.
# Барномае нависед, ки дар файли додашуда маълумоти хама сатрхои токро ба калимае, ки мо дохил мекунем, иваз кунад. 




# ### 7 Question
# Create a python program to generate a random password of the specified length.
# Создайте программу Python для создания случайного пароля указанной длины.
# # input
#     Enter the desired password length: 12
# # output
#     Generated password: Xy#7pLm$9oR5


# import random
# def main(a):
#     l = 'abcdefghijklmnopqrstuvwxyz'
#     u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     t = '0123456789'
#     r = '!@#$%^&*()_+-=[]{}|;:,.<>?/'
#     c = l + u + t + r
#     password = ''.join(random.choice(c) for _ in range(a))
#     return password
# s = int(input("Enter the desired password length: "))
# password = main(s)
# print("Generated password:", password)





# ### 8 Question
# Write a Python script to print a dictionary where the keys are numbers between 1 and N (both included) and the values are the square of the keys.
# Напишите сценарий Python для печати словаря, в котором ключами являются числа от 1 до N (оба включены), а значениями являются квадраты ключей.
# # input
#     15
# # output
#     {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
# def main(n):
#     s = {i: i**2 for i in range(1, n + 1)}
#     return s
# n = int(input())
# print(main(n))



# ### 9 Question
# Create a function that returns the number of times a character appears in each word in a sentence. Treat upper and lower case characters of the same letter as being identical. Создайте функцию, которая возвращает количество раз, когда символ встречается в каждом слове предложения. Считать символы верхнего и нижнего регистра одной и той же буквы идентичными.

# Input       
# char_appears("She sells sea shells by the seashore.", "s")

# Output
# [1, 2, 1, 2, 0, 0, 2]
# def main(s, c):
#     s = s.lower()
#     c = c.lower()
#     w = s.split()
#     o = [word.count(c) for word in w]
#     return o
# res = main("She sells sea shells by the seashore.", "s")
# print(res) 






# ### 10 Task
# Given a list of elements of any data types. Create a Python program to separate elements by their types and save them into a new dictionary.
# The keys of a dictionary must be of a data type, and its element must be data belonging to that type.
# Дан список элементов любых типов данных. Создайте программу Python для разделения элементов по их типам и сохранения их в новый словарь.
# Ключи словаря должны иметь тип данных, а его элементом должны быть данные, принадлежащие этому типу.
# # input
#     1 hello True 12 Muhammad
# # output
#     {"int": [1,12], "str": ["hello", "Muhammad"], "bool": [True]} -->
# def main(a):
#     dic = {}
#     for i in a:
#         e = str(type(i).__name__)
#         if e not in dic:
#             dic[e] = []
#         dic[e].append(i)
#     return dic
# a = [1, "hello", True, 12, "Muhammad"]
# res = main(a)
# print(res)