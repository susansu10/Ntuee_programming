a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()

sum_a = sum(a)
sum_b = sum(b)

solve = 0
for i in a:
    for j in b:
        news_a = sum_a - i + j
        news_b = sum_b - j + i
        if news_a == news_b:
            solve = 1
            print(i, j)
            break
    if solve == 1:
        break    

if solve == 0:
    print("-1 -1")