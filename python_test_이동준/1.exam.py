val = input('주민번호를 입력하세요(******-*******) > ')
male = [1, 3, 5]
female = [2, 4, 6]

for i in range(len(male)):
    if int(val.split('-')[1][0]) == male[i]:
        print('남성입니다.')
    elif int(val.split('-')[1][0]) == female[i]:
        print('여성입니다.')

print(val.split('-')[1][0])