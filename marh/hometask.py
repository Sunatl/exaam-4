# # task 1
# def main(s):
#         return ''.join([c*2 for c in s])
# print(main("String"))      
# print(main("Hello World!")) 
# print(main("1234!_ "))      




# task 2
# def main(file):
#         with open(file, 'r') as file:
#             c = file.read()
#         t = c.lower().split().count("the")
#         return t
# file = "my_file.txt"
# s = main(file)
# print(f"The word 'the' occurs {s} times.")





# task 3
# def main(file):
#         with open(file, 'r') as file:
#             c = file.read()
#         s = c.split()
#         t = sum(1 for word in s if word.endswith('e'))
#         return t
# file = "my_file.txt"
# e = main(file)
# print(f"The number of words ending with 'e' is {e}.")




# task 4
# def main(file):
#         with open(file, 'r') as file:
#             c = file.read()
#         w = c.split()
#         s1 = w.count("this")
#         s = w.count("these")
#         return s1, s
# file = "my_file.txt"
# s1, s = main(file)
# print(f"The word 'this' occurs {s1} times.")
# print(f"The word 'these' occurs {s} times.")





# task 5
# def main(n):
#         if n < 0:
#             return "invalid"
#         elif n == 1:
#             return "Google"
#         else:
#             return f"G{'o' * n}gle"
# print(main(10))
# print(main(2)) 
# print(main(-2))



# task 6
# def c(s, t):
#     return any(s in i for i in t)
# lis = ['red', 'black', 'white', 'green', 'orange']
# print(c("abs", lis)) 
# print(c("ack", lis))



# task 7
# def main(n):
#     s = n // 6
#     t = n + s
#     return t
# print(main(6))   
# print(main(12))  
# print(main(213))  




# task 8
# def main(s):
#     if len(s) == 0:
#         return ""
#     return s[0] + s[-1]
# print(main("ganesh")) 
# print(main("kali"))   
# print(main("shiva"))  


# task 9
# def main(a):
#     return a.endswith('s')
# print(main("changes")) 
# print(main("change"))  
# print(main("dudes"))   
# print(main("magic"))   




