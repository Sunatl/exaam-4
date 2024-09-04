# def main(sum1):
#     if not sum1:
#         return 0
#     return sum1[0] + main(sum1[1:])
# sum1 = [1, 2, 3, 4, 5]  
# print(main(sum1)) 






# # task 3
# def main(n):
#     if n < 10:
#         return n
#     else:
#         return n % 10 + main(n // 10)
# n = 345  
# print(main(n)) 



# task 4
# def main(n):
#     if n <= 0:
#         return 0
#     else:
#         return n + main(n - 2)
# print(main(6))    
# print(main(10))  


# task 5
# def main(a, b):
#     if b == 0:
#         return 1
#     return a * main(a, b - 1)
# print(main(3,4)) 


# task 6
# def main(a, b):
#     if b == 0:
#         return a
#     return main(b, a % b)
# print(main(48,18)) 




# task 7
# def main(s):
#     if len(s) <= 1:
#         return s
#     return main(s[1:]) + s[0]
# print(main("odina"))






