# 함수
'''
JAVA 예시
private int getMethods(int x, Object ym) {
    return result;
}
'''

# 함수선언 def 함수명(파라미터) [ -> any ] :
def add(x,y) -> any:
    return x + y

def minus(x,y):
    return x - y

print(add(3, 5.4))
print(minus(6, 2))
print(add('Hello', 'World')) # 입력파라미터에 제약이 없음

# 리턴값이 없는 함수
def plus(x,y) -> None: # void
    print(x+y)

plus(3, 5.4)

print(None) # NULL

# 다중 파라미터
def add_many(*args):# c/c++ pointer 처럼 보이지만 
    result=0
    for i in args:
        result += i

    return result

print(add_many(1,2,3))
print(add_many(3,6,9,12,15,18,21))
print(add_many(1,2,3,4,5,6,7,8,9,10))
print(add_many(4,3.141592,50,123.6))
# print(add_many('Life','is','short','You','need','Python'))

# 키워드 매개변수 = 결과가 딕셔너리로
def print_kwargs(**kwargs):
    print(kwargs)


result = print_kwargs(a = 1)
res = print_kwargs(name='Hugo', age=45)

# add, minus, mul, div 함수 네개가 할 일을 하나의 함수로 처리
def all_calc(x,y):
    return (x+y,x-y,x*y,x/y)
 
print(all_calc(601,45))
# 함수는 무조건 하나의 값만 리턴
# 리턴값을 튜프롤 처리하면 리턴을 한꺼번에 여러개 할 수 있음
(res_add, res_minus, res_mul, res_div) = all_calc(601, 45)
print(res_add)

# 함수 기본값 
def introduce_myself(name, age, man = True) -> None:
    print(f'나의 이름은 {name}입니다.')
    print(f'나이는 {age}세 입니다')
    if man:
        print(f'나는 남자입니다.')
    else:
        print(f'나는 여자입니다.')

introduce_myself('유숙',45,False)
introduce_myself(man=False ,name='애슐리' ,age=40) # 파라미터명 지정하면 순서에 상관없음

# 같은 이름의 변수를 사용하는 것을 지양(!)

val = 1 # 전역변수

def valtest(val): # 지역변수
    val += 1 
    return val

def valtest2():
    global val # 전역변수 val을 내가 함수내에서 잠시 가져다 쓸게!!
    val += 10

# def valtest2(tmp):
#     tmp += 1
#     return tmp

res = valtest(val)
print(val)
print(res)

valtest2()
print(val)

# lambda 함수

adds = lambda a, b: a+b
# 위에 식과 동일
# def adds(a, b):
#   return a + b
print(add(6,7))

print(abs(-3)) #절대값 abs[olute]
print(all([1, 3, 5, 7, 9])) 

