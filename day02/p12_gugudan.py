#file: p12_gugudan.py
#desc: 구구단 프로그램

print('구구단 프로그램 v99')
for i in range(2, 10):  #구구단 2단부터 9단까지 출력 / 이중 for문
    print(f"<{i}단>")
    for a in range(1, 10):
        print(f"{i} X {a} = {i * a:2d}", end = '\t')
    print()    #단 끝날 때마다 개행
    print()
