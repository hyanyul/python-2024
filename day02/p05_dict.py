#file: p05_dict.py
#desc: 딕셔너리 자료형 학습


#딕셔너리 구성
spiderMan = {'name': 'Peter Parker', 'age': 18, 'weapon': 'Web shooter', 'friends': ['ironman', 'Thor', 'Captain America']}

#딕셔너리 출력
print(spiderMan)
print(spiderMan['name'])   #딕셔너리 키값으로 안의 값 출력 가능

#값 추가
spiderMan['job'] = 'CameraMan'
print(spiderMan)    #제일 마지막에 값 추가됨

#값 삭제
del spiderMan['friends']
print(spiderMan)    #friends값 다 날라감

#키값 중복 사용 시 하나만 입력됨, 키값은 되도록 문자열(숫자도 사용 가능하나 권장x)


#딕셔너리 함수
print(spiderMan.keys())   #딕셔너리에 현재 존재하는 키 목록
print(list(spiderMan.keys()))   #키 목록을 리스트 형태로 형 변환
print(spiderMan.items())    #딕셔너리 모든 아이템 출력
print(spiderMan.get('job'))  #딕셔너리 값 가져오기
print('friends' in spiderMan)   #딕셔너리 안에 키가 있는지 확인
print(spiderMan.values())   #딕셔너리 안에 있는 값들만 나옴(키값 안나옴)

res = spiderMan.pop('job')  #딕셔너리 안 제일 마지막 키값 꺼냄
print(res)
print(spiderMan)    #job 없어져 있음
print(spiderMan.pop('age'))
print(spiderMan)    #age 없어져 있음

#데이터 삭제
spiderMan.clear()
print(spiderMan)    #스파이더맨 내의 데이터값 다 날라감

#완전 삭제
del spiderMan   
print(spiderMan)    #스파이더맨 딕셔너리 삭제됨


#집합: 중복 허용 X, 순서 X
#set([1, 2, 3, 4, 3, 4, 2, 1]) = {1, 2, 3, 4} -> 순서가 없기 때문에 다음에 출력 시 어떤 순서로 나올지 모름