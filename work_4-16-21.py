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
