# class Shaxs:
#     def init(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
#
#     def str(self):
#         return f"Shaxs: {self.ism}, Yosh: {self.yosh}"
#
#     def eq(self, other):
#         return self.ism == other.ism and self.yosh == other.yosh
#
#
# shaxs1 = Shaxs("Ali", 25)
# shaxs2 = Shaxs("Vali", 30)
#
# print(shaxs1)
#
# print(shaxs1 == shaxs2)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# class Talaba:
#     def init(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
#
#     def str(self):
#         return f"Talaba: {self.ism}, Yosh: {self.yosh}"
#
#     def eq(self, other):
#         return self.ism == other.ism and self.yosh == other.yosh
#
#     def lt(self, other):
#         return self.yosh < other.yosh
#
#     def le(self, other):
#         return self.yosh <= other.yosh
#
#     def gt(self, other):
#         return self.yosh > other.yosh
#
#     def ge(self, other):
#         return self.yosh >= other.yosh
#
#
# talaba1 = Talaba("Ali", 20)
# talaba2 = Talaba("Vali", 25)
#
# print(talaba1)
#
# print(talaba1 == talaba2)
#
# print(talaba1 < talaba2)
#
# print(talaba1 <= talaba2)
#
#
# print(talaba1 > talaba2)
#
#
# print(talaba1 >= talaba2)



# my_object = Object()
#
#
# my_object.raqam = 10
# my_object.matn = "Salom"
#
#
# def metod():
#     return
#
# my_object.metod = metod
#
#
# if hasattr(my_object, "raqam"):
#     print("my_objectning raqam atributi mavjud")
#     if my_object.raqam < 5:
#         print("my_objectning raqami 5 dan kichik")
#     elif my_object.raqam == 5:
#         print("my_objectning raqami 5 ga teng")
#     else:
#         print("my_objectning raqami 5 dan katta")
#
# if hasattr(my_object, "matn"):
#     print("my_objectning matn atributi mavjud")
#     if len(my_object.matn) < 10:
#         print("my_objectning matni 10 belgidan kam")
#     elif len(my_object.matn) == 10:
#         print("my_objectning matni 10 belgidan teng")
#     else:
#         print("my_objectning matni 10 belgidan katta")
#
# if hasattr(my_object, "metod"):
#     print("my_objectning metod metodi mavjud")
#     result = my_object.metod()
#     print(result)