print('Hello World')#주석 ctrl+/, 'Hello World'출력
a = 10 #변수선언,a에 10을 넣어라.
b = 30 #b에 30을 넣어라.
c = a+b #c는 a+b의 변수의 합을 저장해라.

print(a)
print(b)
print(c)

a = 50
print(a)
print(type(a))

#a=20 이면 변수가 바뀐다.
# a = 20
# print(a)
# print(type(a))


b = 3.14 #float 소수
print(b)
print(type(b))

c = True # 참
print(c)
print(type(c))

d = False # 거짓
print(d)
print(type(d))

e = '파이썬' # ''문자열, 문자로 취급한다. ex)'1234' '숫자'
print(e)
print(type(e))

f = "파이썬" # ""문자열, 문자로 취급한다.ex)"1234" "숫자"
print(f)
print(type(f))

g = '50'
h = 50
i = int(g) + h #문자열로 바꾼다음에 연산.
i = int(g) + h #문자열로 바꾼다음에 연산.
print(i)

# int 와 숫자는 연산이 불가능:타입을 일치 시켜야 한다.
j = g + str(h) #문자열로 바꾼다음에 연산
print(j)
print(type(j))
# 문자열끼리 이어붙이기가 된다.
# 문자열에 대해서는 (+)연산 밖에 되지 않는다.
# 뺴기는 안된다.

# 문자열 인덱싱(띄어쓰기 포함)
# 문자열 내 각 문자에 대한 번호 = 인덱스
# 인덱스는 [0]부터 시작 = 첫번째 글자.
example = "Today is Happy"
print(len(example)) #len 문자열의 갯수, 띄어쓰기도 문자열임.
print(example[3]) # a
# 인덱스 번호를 이용해서 배열내의 값을 꺼내는 것을 인덱싱이라고 한다.
print(example[0:4]) #변수[:]
print(example[9:14])#글자수에서 -1하면 된다.
print(example[9:])
print(example[9:])#실행취소의 실행취소:[ctrl+shift+z]
print(len(example[:])) # last_index=len(example[])-1

#코드 라인 복사 단축키: [ctrl+d]
#실행취소 [ctrl+z]
#코드라인 삭제 [ctrl+y]

# 변수선언시 주의사항!!
type = "물 포켓몬"
print(type) # 변수선언은 덮어씌운다.
# 변수선언시 메소드선언과 중복되지 않게 주의 해야한다.
# ex)변수선언시 v_type,str_type등의 다른방법으로 알기쉽게선언한다.
