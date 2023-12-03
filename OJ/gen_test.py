cs_range = 100000


# a = []
# for i in range(1, cs_range, 2):
#     # print(j, end=' ')
#     a.append(i)

# # print(a)
# a.append(49994)

# temp = 0
# temp = a[-1]
# a[-1] = a[len(a) // 2]
# a[len(a) // 2] = temp

# # print('Sum_a = ',sum(a))
# # print('len_a = ', len(a))

# b = []
# for i in range(2, cs_range+1, 2):
#     # print(j, end=' ')
#     b.append(i)

# # print(b)
# # b.append(99994)

# temp = 0
# temp = b[-1]
# b[-1] = b[len(b) // 2]
# b[len(b) // 2] = temp

# # print('Sum_b = ',sum(b))
# # print('len_b = ', len(b))

# # print((sum(b) - sum(a)))
# # print((sum(b) - sum(a)) + 49994)


# # y = (sum(b) - sum(a) + 2*x) // 2
# # 2y = (sum(b)+y) - (sum(a)+x) + 2x
# # y = sum(b) - sum(a) + x                        


# # with open('boss.in', 'w') as f:
# #     for j in a:
# #         f.write(str(j) + ' ')
# #     f.write('\n')
# #     for j in b:
# #         f.write(str(j) + ' ')


# --------------generate 6 in ----------------

a = []
for i in range(1, cs_range, 2):
    a.append(i)

# print(a)

print('Sum_a = ',sum(a))
print('len_a = ', len(a))

b = []
for i in range(2, cs_range+1, 2):
    b.append(i)

# print(b)

print('Sum_b = ',sum(b))
print('len_b = ', len(b))

print((sum(b) - sum(a)))
                  

import random
random.shuffle(a)
random.shuffle(b)

with open('6.in', 'w') as f:
    for j in a:
        f.write(str(j) + ' ')
    f.write('\n')
    for j in b:
        f.write(str(j) + ' ')
