# import math
# while True:
#     s = int(input("\nKonkuliyator:\n1. Jamh va Tarh\n2. Zarb va Taksim\n3. Modul va Kvadrat \n4. Factorial va Resha \n5. Rakami duiro ba dui gardondan\n6. Exit\nRakamro vorid kuned: "))
#     if s == 1:
#         print("Рақамро ворид кунед:")
#         a = int(input("Рақами аввал: "))
#         o = input("Операторро ворид кунед (+ ё -): ")
#         c = int(input("Рақами дуюм: "))
#         if o == "+":
#             print(f"Натиҷа: {a + c}")
#         elif o == "-":
#             print(f"Натиҷа: {a - c}")
#         else:
#             print("Оператор нодуруст! Лутфан + ё - истифода баред.")
#     elif s == 2:
#         print("Рақамҳоро ворид кунед:")
#         a = int(input("Рақами аввал: "))
#         o = input("Операторро ворид кунед (* ё /): ")
#         c = int(input("Рақами дуюм: "))
#         if o == "*":
#             print(f"Натиҷа: {a * c}")
#         elif o == "/":
#             if c != 0:
#                 print(f"Натиҷа: {a / c}")
#             else:
#                 print("Тақсим ба сифр иҷозат нест.")
#         else:
#             print("Оператор нодуруст! Лутфан * ё / истифода баред.")
#     elif s == 3:
#         print("Рақамро ворид кунед:")
#         a = int(input("Рақам: "))
#         o = input("Операторро ворид кунед (% барои модулус ё ** барои квадрат): ")
#         if o == "%":
#             b = int(input("Рақами дуюм: "))
#             print(f"Натиҷа: {a % b}")
#         elif o == "**":
#             print(f"Натиҷа: {a ** 2}")
#         else:
#             print("Оператор нодуруст! Лутфан % ё ** истифода баред.")
#     elif s == 4:
#         print("Интихоб:\n1. Факториал\n2. Реша")
#         r = int(input())
#         if r == 1:
#             cnt = 1
#             print("Рақамро ворид кунед:")
#             a = int(input("Рақам: "))
#             for i in range(1, a + 1):
#                 cnt *= i
#             print(f"Факториал-и {a}: {cnt}")
#         elif r == 2:
#             print("Рақамро ворид кунед:")
#             a = int(input("Рақам: "))
#             if a >= 0:
#                 resha = math.sqrt(a)
#                 print(f"Реша и {a}: {resha}")
#             else:
#                 print("Рақами манфӣ барои ҳисоб кардани реша мувофиқ нест.")
#         else:
#             print("Интихоби нодуруст! Лутфан 1 барои факториал ё 2 барои реша интихоб кунед.")
#     elif s == 5:
#             a = int(input("Rakami duiro vorid kuned: "))
#             while a>0:
#                 print(a%2,end="")
#                 a//=2
#     elif s == 6:
#         print("Барнома қатъ шуд.")
#         break
#     else:
#         print("Интихоби нодуруст. Лутфан аз 1 то 6 интихоб кунед.")