import random

num = 1
cs_range = 100000
flag = 0
while num < 2 and flag == 0:
    aliceSizes = []
    a_length = random.randint(1,  cs_range)
    print('a_length = ', a_length)

    for i in range(a_length):
        aliceSizes.append(random.randint(1,  cs_range))

    bobSizes = []
    b_length = random.randint(1,  cs_range)
    print('b_length = ', b_length)

    for i in range(b_length):
        bobSizes.append(random.randint(1,  cs_range))

    with open(f'{str(num)}.in', 'w') as f:
        for j in aliceSizes:
            f.write(str(j) + ' ')
        f.write('\n')
        for j in bobSizes:
            f.write(str(j) + ' ')

    # --------------generate output----------------
    sum_a = sum(aliceSizes)
    sum_b = sum(bobSizes)

    # sum_a -i + j = sum_b -j + i
    # 2j = sum_b - sum_a + 2i
    # j = (sum_b - sum_a + 2i)/2

    b = set(bobSizes)
    solve = 0

    if (sum_b - sum_a) % 2 != 0:
        with open(f'{str(num)}.out', 'w') as f:
            f.write('No -1 -1')
    else:
        for i in aliceSizes:
            j = (sum_b - sum_a + 2*i) // 2
            if j in b:
                with open(f'{str(num)}.out', 'w') as f:
                    f.write(str(i) + ' ' + str(j))
                solve = 1
                break

        if solve == 0:
            with open(f'{str(num)}.out', 'w') as f:
                f.write('-1 -1')
        else:
            num += 1
    print('------------------')