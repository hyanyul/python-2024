#file: p13_starPrint.py
#desc: 별 찍기

print('예제----------')
for i in range(1, 6):
    print('*' *  i)

print()

#이중 for문으로 위와 똑같이 출력
print('별찍기1----------')
for i in range(1, 6):
    for a in range(1, i + 1):
        print("*", end = '')
    print()

print()

print('별찍기2---------')
for i in range(1, 6):
    for a in range(i + 1, 6):
        print(' ', end = '')
    for a in range(6 - i, 6):
        print('*', end = '')
    print()

