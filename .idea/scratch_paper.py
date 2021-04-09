# from sys import exit
#
# scores = input("Enter scores: ").split(sep=" ")
# grades = ["A", "B", "C", "D", "F",]
#
# for score in scores:
#     if not score.isdigit():
#         print("Invalid Input")
#         exit()
# for i in range(0, len(scores)):
#     scores[i] = int(scores[i])
# for i in range(0, len(scores)):
#     for n in range(1, 5):
#         if scores[i] >= max(scores) - (10 * n):
#             print(f"Student {i} score is {scores[i]} and grade is {grades[n - 1]}")
#             break
#     if scores[i] < max(scores) - 40:
#         print(f"Student {i} score is {scores[i]} and grade is F")
# ----------------------------------------------------------------------
# from sys import exit
#
# user_in = input("Enter integers between 1 and 100, inclusive: ")\
#     .strip().split(sep=" ")
#
# for ind, entry in enumerate(user_in):
#     if not entry.isdigit():
#         print(f"'{entry}' is invalid input.")
#         exit()
#     else:
#         user_in[ind] = int(user_in[ind])
# user_in.sort()
#
# chopped = []
# while user_in != []:
#     if chopped == []:
#         chopped.append(user_in[0])
#         del user_in[0]
#         if user_in == []:
#             num = chopped.count(chopped[0])
#             if num > 1:
#                 print(f"{str(chopped[0])} occurs {str(num)} times")
#             elif num == 1:
#                 print(f"{str(chopped[0])} occurs {str(num)} time")
#             del chopped[:]
#         continue
#     if user_in[0] == chopped[0]:
#         chopped.append((user_in[0]))
#         del user_in[0]
#         continue
#     elif user_in[0] != chopped[0]:
#         num = chopped.count(chopped[0])
#         if num > 1:
#             print(f"{str(chopped[0])} occurs {str(num)} times")
#         elif num == 1:
#             print(f"{str(chopped[0])} occurs {str(num)} time")
#         del chopped[:]
# ----------------------------------------------------------------------
# from sys import exit
#
# user_in = input("Enter numbers: ").strip().split(sep=" ")
# for ind, entry in enumerate(user_in):
#     if not entry.isdigit():
#         print(f"'{entry}' is invalid input.")
#         exit()
#     else:
#         user_in[ind] = int(user_in[ind])
#
# product = []
# for entry in user_in:
#     if entry not in product:
#         product.append(entry)
#
# print("The distinct numbers are: ", end="")
# for entry in product:
#     print(str(entry), end=" ")
# ----------------------------------------------------------------------
# from math import sqrt
#
# user_in = input("Enter numbers: ").strip().split(sep=" ")
# for ind, entry in enumerate(user_in):
#     user_in[ind] = float(user_in[ind])
#
# total = sum(user_in)
# num = len(user_in)
#
# mean = round(total / num, 2)
# print(f"The mean is {str(mean)}")
#
# squared_sum = 0
# for entry in user_in:
#     squared_sum += entry ** 2
# root = (squared_sum - (((total) ** 2)/ num)) / (num - 1)
# dev = round(sqrt(root), 5)
# print(f"The standard deviation is {str(dev)}")
# ----------------------------------------------------------------------
# def isSorted(lst):
#     copy = []
#     copy.extend(lst)
#     copy.sort()
#     if copy == lst:
#         return True
#     else:
#         return False
#
#
# def main():
#     user_in = input("Enter list: ").strip().split(sep=" ")
#     for ind, entry in enumerate(user_in):
#         user_in[ind] = int(user_in[ind])
#     if isSorted(user_in):
#         print("The list is already sorted")
#     elif not isSorted(user_in):
#         print("The list is not sorted")
#
#
# main()
















