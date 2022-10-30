# ls = [1,2,3,2,1]
# set_1 = set(ls)
# print(ls)
# set_2 = set (ls.reverse())
# print(ls)
#
# if set_1 == set_2:
#     print(True)
# else:
#     print(False)


ls_1 = [1,2,3,2,1]
ls_2 = ls_1[:]
ls_2.reverse()

print(ls_1,ls_2)

if ls_1 == ls_2:
    print(True)
else:
    print(False)