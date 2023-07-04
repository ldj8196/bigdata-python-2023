val = input('일주일 영어명을 입력해보세요. > ')

day_contain_list = ['MON', 'TUE', 'WED', 'TUR', 'FRI', 'SAT', 'SUN']
day_list = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

for i in range(len(day_contain_list)):
    if val in day_contain_list[i]:
        print(day_list[i])
    