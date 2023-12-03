with open('boss.in', 'r') as f:
    lines = f.readlines()

# print(lines)

a = list(map(int, lines[0].split()))
b = list(map(int, lines[1].split()))

# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
a.sort()

sum_a = sum(a)
sum_b = sum(b)

# sum_a -i + j = sum_b -j + i
# 2j = sum_b - sum_a + 2i
# j = (sum_b - sum_a + 2i)/2

b = set(b)
solve = 0

if (sum_b - sum_a) % 2 != 0:
    print("NoNo -1 -1")
    exit()

for i in a:
    j = (sum_b - sum_a + 2*i) // 2
    if j in b:
        print(i, int(j))
        solve = 1
        break
        

if solve == 0:
    print("-1 -1")