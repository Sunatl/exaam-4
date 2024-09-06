# def main(m,cnt = 0):
#     d = m %10
#     if m == 0:
#         return cnt
#     cnt+=d
#     return main(m//10,cnt)
# print(main(3))



# task 1
# def main(n, cnt=1):
#     if cnt == n:
#         return "YES"
#     elif cnt > n:
#         return "NO"
#     else:
#         res3 = main(n, cnt + 3)
#         res5 = main(n, cnt + 5)
#         if res3 == "YES" or res5 == "YES":
#             return "YES"
#         else:
#             return "NO"
# n = int(input())
# print(main(n))





# task 5
# def main(s, l=0, r=0):
#     if r == 0:  
#         r = len(s) - 1
#     if l > r:
#         return ""
#     if l == r:
#         return s[l]
#     if l + 1 == r:
#         return s[l:r+1]
#     return s[l] + "(" + main(s, l + 1, r - 1) + ")" + s[r]
# s = input()
# print(main(s))


# task 2
# def main(s, i=0, t=0):
#     if i == len(s):
#         return t
#     c = int(s[i])
#     t = max(t, c)
#     return main(s, i + 1, t)
# s = input()
# print(main(s))



# task 3
# def main(s):
#     if not s:
#         return 0
#     if s[0].isdigit():
#         return 1 + main(s[1:])
#     else:
#         return main(s[1:])
# s = input()
# print(main(s))



# task 4
# def main(s):
#     if len(s) <= 1:
#         return s
#     return s[0] + '*' + main(s[1:])
# s = input()
# print(main(s))




# task 7
# def main(s):
#     if len(s) <= 1:
#         return s
#     if s[0] == s[-1]:
#         return main(s[1:-1])
#     else:
#         return s[0] + main(s[1:-1]) + s[-1]
# s = input().strip()
# print(main(s))












