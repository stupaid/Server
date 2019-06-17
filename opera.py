str01 = "python is good language"
# p  y  t  h  o  n     i  s     g  o  o  d     l  a  n  g  u  a  g  e
# 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22

# print(len(str01))
# print(str01[0:3])
# print(str01[0:])
# print(str01[:-1])
#
# for index in range(len(str01)):
#   print(str01[index])
#
# for i in str01:
#     print(i)

str01_split = str01.split()
print(str01_split, type(str01_split))

str01_replace = str01.replace('o', '0')
print(str01_replace)

if "o" in str01:
    print("o exist in str01")
else:
    print("o not exist in str01")
