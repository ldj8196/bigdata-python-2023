# 딕셔너리
iron_man = {'name':'TonyStark','address':'New York','armer':'Repluser Arm'} # Json과도 일치

print(iron_man)

# 아래 두개 결과 동일
print(iron_man.get('name'))
print(iron_man['name'])

# 딕셔너리는 Key 중복 불가
d1 = {1:'a',1:'b'}
print(d1)

# Value 중복 허용
d2 = {1:'test', 2:'test'}
print(d2)

# 딕셔너리 함수들
print(iron_man.keys())

for item in iron_man.keys() :
    print(item)

print(iron_man.values())

print(iron_man.items()) # values(), items() 많이 사용안함

