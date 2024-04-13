Jonibek Uralov, [13.04.2024 14:37]
# def tub_sonlar(n, m):
#     tub = []
#     while n <= m:
#         i = n
#         j = 1
#         boluvchi = 0
#         while j <= i:
#             if i % j == 0:
#                 boluvchi += 1
#             j += 1
#         if boluvchi == 2:
#             tub.append(i)
#         n += 1
#     return tub
# n = int(input("n="))
# m = int(input("m="))
# print(tub_sonlar(n,m))



# def fibonachi(n):
#     sonlar = []
#     for x in range(n):
#         if x == 0 or x == 1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1] + sonlar[x-2])
#     return sonlar
# print(fibonachi(100))

Jonibek Uralov, [13.04.2024 14:37]
# def aylana_hisobla(radius):
#     diameter = 2*radius
#     perimeter = 2*3.14*radius
#     javob = {
#     'diameter':diameter,
#     'perimeter':perimeter,
#     'yuza':None
#     }
#     return javob
# n = float(input("Aylana radiusini kiriting: "))
# aylana_malumotlari = aylana_hisobla(n)
# print(aylana_malumotlari)


