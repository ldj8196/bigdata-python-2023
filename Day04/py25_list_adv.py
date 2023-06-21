# 리스트 고급사용
# 1 ~ 1000까지 사이의 3의 배수값 리스트
list_3rd = []
for n in range(1, 1000+1):
    if n % 3 == 0: # 3의 배수
        list_3rd.append(n)

#print(list_3rd)

# 1~1000 까지 사이의 3의 배수값
list_3rd_2 = [n for n in range(3, 1000+1, 3)]
#print(list_3rd_2)

list_3rd.clear()
for n in range(3, 1000+1, 3):
    list_3rd.append(n)

#print(list_3rd)

# 2의 배수 구하기
#print([2*x for x in range(1, 10+1)])
# 3. 3의 배수 구하기
#print([3*x for x in range(1, 333+1)])

# 4. 1 ~ 1000까지 사이의 3의 배수값 리스트
list_3rd = []
for n in range(1, 1000+1):
    if n % 3 == 0: # 3의 배수
        list_3rd.append(n)

print([x for x in range(1, 1000+1) if x % 3 == 0]) # for문 if문 전부 처리

# zip함수 하고 유사 ( 2중 포문 )
print([(x,y) for x in ['광어', '고등어', '참치'] for y in ['한돈', '한우', '한계']])

l1=[]
for x in ['광어', '고등어', '참치']:
    for y in ['한돈', '한우', '한계']:
        l1.append((x,y))

print(l1)

print([x for x in range(10+1) if x < 5 if x % 2 == 0])

l1.clear()
for x in range(10+1):
    if x < 5:
        if x % 2 == 0 :
            l1.append(x)

print(l1)

print(tuple([x*2 for x in range(1,5+1)]))
