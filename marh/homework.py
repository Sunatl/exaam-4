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




# task 8
# def main(n):
#     if n > 50:
# #         return n
# #     print(n)
# #     main(n + 1)
# # res = main(1)
# # print(res)







# # task 1
# def main(a=int(input()), b=int(input()), s=int(input()), d=int(input())):
#     if a <= b and b <= s and s <= d:
#         return(a)
#     elif b <= a and a <= s and s <= d:
#         return(b)
#     elif s <= a and a <= b and b <= d:
#         return(s)
#     else:
#         return(d)
# print(main())


# task 2
# def main(a=input(), b=input()):
#     return(a**b)
# print(main())



# task 3
# def main(a,b):
#     if a == 0 and b == 1 or a == 1 and b == 0:
#         return(1)
#     else:
#         return(0)
# print(main(0,1))



# task 4
# def main(a,b,c):
#     if a == 1 and b == 1:
#         return 1
#     elif b == 1 and c == 1:
#         return 1
#     elif a == 1 and c == 1:
#         return 1
#     elif a == 1 and b==1 and c == 1:
#         return 1
#     else:
#         return 0
# print(main(0,0,1))



# def mai(a):
#     cnt = 0
#     for i in range(1,a+1):
#         if a%i==0:
#             cnt+=1
#     if cnt <= 2 and a != 0:
#         return "prime"
#     else:
#         return "composite"

# a = int(input())
# print(mai(a))
            
            
# a = int(input())
# while a>0:
#     print(a%2,end="")
#     a//=2



