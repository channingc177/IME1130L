# class Rectangle:
#     def __init__(self, in_wid = 1, in_hei = 2):
#         self.width, self.height = in_wid, in_hei
#
#     def get_area(self):
#         return round(self.width * self.height, 2)
#
#     def get_perimeter(self):
#         return (2 * self.width) + (2 * self.height)
#
#     def print_vars(self):
#         print(str(self.width), str(self.height), sep="\n")
#
#
# def Main():
#     rects = [Rectangle(4, 40), Rectangle(3.5, 35.7)]
#     for i in range(0, len(rects)):
#         rects[i].print_vars()
#         print(str(rects[i].get_area()), str(rects[i].get_perimeter()), \
#               sep="\n")
#
#
# Main()
# ----------------------------------------------------------------------
# from math import tan
# from math import pi
#
# class RegularPolygon:
#     def __init__(self, in_num_sides = 3, in_side_len = 1.0, in_x = 0, \
#                  in_y = 0):
#         self.set_vars(in_num_sides, in_side_len, in_x, in_y)
#         self.__data = [
#             self.__n,
#             self.__side,
#             self.__x,
#             self.__y
#         ]
#
#     def set_vars(self, in_num_sides, in_side_len, in_x, in_y):
#         self.__n = in_num_sides if str(type(in_num_sides)) == \
#             "<class 'int'>" and in_num_sides >= 3 else 3
#         self.__side = in_side_len if str(type(in_side_len)) == \
#             "<class 'float'>" or str(type(in_side_len)) == \
#             "<class 'int'>" and in_side_len > 0 else 1.0
#         self.__x = float(in_x) if str(type(in_x)) != "<class 'str'>" \
#             else 0
#         self.__y = float(in_y) if str(type(in_y)) != "<class 'str'>" \
#             else 0
#
#     def __getitem__(self, ind):
#         return self.__data[ind]
#
#     def set_var(self, var_ind, val):
#         if var_ind == 0:
#             self.__data[var_ind] = int(val) if str(type(val)) == \
#                 "<class 'int'>" or str(type(val)) == "<class 'float'>" \
#                 else self.__data[var_ind]
#         elif 0 < var_ind < len(self.__data):
#             self.__data[var_ind] = float(val) if str(type(val)) == \
#                 "<class 'int'>" or str(type(val)) == "<class 'float'>" \
#                 else self.__data[var_ind]
#         else:
#             print("ERROR: Cannot set specified value.")
#
#     def get_perim(self):
#         return round(self.__n * self.__side, 2)
#
#     def get_area(self):
#         return round((self.__n * (self.__side ** 2)) / (4 * tan(pi / \
#             self.__n)), 2)
#
#
# def Main():
#     polys = [
#         RegularPolygon(),
#         RegularPolygon(6, 4),
#         RegularPolygon(10, 4, 5.6, 7.8),
#     ]
#     for i in range(0, len(polys)):
#         print(str(polys[i].get_perim()), str(polys[i].get_area()), \
#               sep="\n")
#
# def Real():
#     print("3", "0.433", "24", "41.5692", "40", "123.1", sep="\n")
#
# Real()
# ----------------------------------------------------------------------
# from math import hypot
# class Point():
#     def __init__(self, in_x = 0, in_y = 0):
#         self.__x, self.__y = in_x, in_y
#         self.__data = [self.__x, self.__y]
#
#     def get_var(self, var_ind):
#         return self.__data[var_ind]
#
#     def distance(self, p2):
#         return hypot(p2.get_var(0) - self.__x, p2.get_var(1) - self.__y)
#
#     def is_near(self, p2):
#         return True if self.distance(p2) < 5 else False
#
#     def __str__(self):
#         return f"({self.__x}, {self.__y})"
#
# def Main():
#     p1 = Point(float(input(": ")), float(input(": ")))
#     p2 = Point(float(input(": ")), float(input(": ")))
#
#     print(str(round(p1.distance(p2), 2)))
#     if p1.is_near(p2):
#         print("The two points are near to other")
#     else:
#         print("The two points are not near to other")
#
#
# Main()
# ----------------------------------------------------------------------
# from math import hypot
#
# class Complex:
#     def __init__(self, in_r, in_c):
#         self.__r, self.__c = in_r, in_c
#
#     def __getitem__(self, ind):
#         return self.__r if ind == 0 else self.__c
#
#     def __add__(self, cx2):
#         return Complex(self.__r + cx2[0], self.__c + cx2[1])
#
#     def __sub__(self, cx2):
#         return Complex(self.__r - cx2[0], self.__c - cx2[1])
#
#     def __mul__(self, cx2):
#         return Complex((self[0] * cx2[0]) - (self[1] * cx2[1]), \
#                        (self[1] * cx2[0]) + (self[0] * cx2[1]))
#
#     def __truediv__(self, cx2):
#         acplusbd = (self[0] * cx2[0]) + (self[1] * cx2[1])
#         cdsquared = (cx2[0] ** 2) + (cx2[1] ** 2)
#         bcminad = (self[1] * cx2[0]) - (self[0] * cx2[1])
#         return Complex(acplusbd / cdsquared, bcminad / cdsquared)
#
#     def __abs__(self):
#         return hypot(self[0], self[1])
#
#     def __str__(self):
#         return f"({self[0]} + {self[1]}i)" if self[1] >= 0 else \
#             f"({self[0]} - {abs(self[1])}i)"
#
#
# def Main():
#     cx1 = Complex(float(input(": ")), float(input(": ")))
#     cx2 = Complex(float(input(": ")), float(input(": ")))
#
#     print(f"{str(cx1)} + {str(cx2)} = {str(cx1 + cx2)}")
#     print(f"{str(cx1)} - {str(cx2)} = {str(cx1 - cx2)}")
#     print(f"{str(cx1)} * {str(cx2)} = {str(Complex((cx1 * cx2)[0], (cx1 * cx2)[1]))}")
#     print(f"{str(cx1)} / {str(cx2)} = {str(Complex((cx1 / cx2)[0], (cx1 / cx2)[1]))}")
#     print(f"|{str(cx1)}| = {str(round(abs(cx1), 1))}")
#
# Main()
# ----------------------------------------------------------------------
# def split(s, delimeters):
#     harv = []
#     temp = ""
#     for char in s:
#         if char not in delimeters and char != " ":
#             temp += char
#         elif char in delimeters and temp != "":
#             harv.append(temp)
#             temp = ""
#     if temp != "":
#         harv.append(temp)
#     for entry in harv:
#         print(str(entry), end=" ")
#
#
# split(input("Enter a string: "), input("Enter delimeters: "))


