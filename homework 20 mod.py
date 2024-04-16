# def kalkulator(misol):
#     try:
#         natija = eval(misol)
#         return natija
#     except (SyntaxError, ZeroDivisionError, TypeError):
#         return "Noto'g'ri amal."
#
#
# misol = input()
# natija = kalkulator(misol)
# print(natija)
#



# def birlashtirish(*lists):
#     result = []
#     for lst in lists:
#         result.extend(lst)
#     return result
#
#
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = [7, 8, 9]
# list4 = [10,11,12]
#
# natija = birlashtirish(list1, list2, list3,list4)
# print(natija)