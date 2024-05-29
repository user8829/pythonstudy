# 연산자( +,-,*,/)
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b) # 소수점 세째자리까지 표현한다.
print(a % b) # 나머지

naver_point = 20000

naver_point = naver_point - 5000
print(naver_point)

naver_point = naver_point + 10000
print(naver_point)

naver_point = naver_point - 5000

naver_point -= 10000 # naver_point = naver_point - 5000
print(naver_point)

# 비교연산자
a = 10
b = 3
# a 와 b가 같습니까?
print(a == b)
c = a == b
print(type(c))

# a 와 b와 다릅니까?
print(a != b)

# a 가 b 보다 큽니까?
print(a > b)

# a 가 b 보다 작습니까?
print(a < b)

# a 가 b 보다 크거나 같습니까?
print(a >= b)

# a 가 b 보다 작거나 같습니까?
print(a <= b)

print("================배열=========================")

# 배열은 데이터들을 담을 수 있는 그릇
# 파이썬  배열

# 배열(Array) 선언
v_array = [] # 빈 배열 생성

print(type(v_array)) # <class 'list'>
print(v_array)

#값 추가하기
#자동완성(assist) [ctrl + space]
v_array.append(1) # 배열 내에 값 1 추가
v_array.append(5) # 배열 내에 값 5 추가
v_array.append(3) # 배열 내에 값 3 추가

# 값을 넣은 순서대로 배열에 들어가 있음
print(v_array) # [1, 5, 3]

# 배열 내 값의 개수 확인
print(len(v_array))

# 배열의 인덱싱
print(v_array[1])
print(v_array[1:2]) # 슬라이스
print(v_array[0:2]) # 0~1

# 배열 정렬
v_array.sort()
print(v_array) # 오름차순 정렬

v_array.sort(reverse=True)
print(v_array)

# 값을 넣은 채로 배열 선언
v_array = [3, 6, 1, 7, 4, 2]

# 배열 내 최소값, 최대값 꺼내기

v_array.sort()
print(v_array)

v_min = v_array[0]
print(v_min)

last_index =v_array[len(v_array) - 1]
print(last_index)
v_max = v_array[5]
print(v_max)

v_min = min(v_array)
v_max = max(v_array)
#v_array.sort(reverse=True)
#v_max_1 = v_array[0]
#print(v_max_1)

print("=================조건문================")

#주민번호 뒷자리의 첫번째 숫자
id_num = 2

# id_num 홀수이면 남성, 짝수면 여성
# 1, 2 ->1900년대
# 3, 4 ->2000년대
# 5, 6 ->1900년대 외국인
# 7, 8 ->2000년대 외국인
# 9, 0 ->1800년대

# print(id_num % 2)

if id_num % 2 == 1: #조건
    print('남자') #True -> 실행, False -> 실행되지 않음
else:
    print('여자') #False -> 실행되지 않음

# 나이 입력
v_age = 48

# 20~29 일때 ->20 으로 변경, v_age/10 -> 소수점 제거 하면 2 *10 =20
v_gen = int(v_age/10)*10
print(v_gen)

# True 실행 False 는 다음 실행 계속 즉, True 가 될때 까지, True 이면 종료
if v_age == 10:
    print('10대')
elif v_gen == 20:
    print('20대')
elif v_gen == 30:
    print('30대')
else: # 그 외 나머지
    print('40대이상')

print("\n ================반복문=====================\n")

print(1)
print(2)
print(3)
print('......')
print("\n다음은\n")
for a in range(1,10): #1~9까지
   print(a)  # range(1,10)=[1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a,end='')

#print('반복끝')이 반복문 안에 들어간다면?

for a in range(1,10): #1~9까지
   print(a)  # range(1,10)=[1, 2, 3, 4, 5, 6, 7, 8, 9]
   print('반복 끝')

test_range = range(1, 11)
print(test_range)
print(test_range[3])
#range함수는 끝값은 표기하지 않는다?=10이되면 멈춘다. range(start,stop,step)
print("====================")
for i in range(2,4):
    print(i)
print("========배열============")


v_array = list(range(1, 11))
print(v_array)

for i in v_array:
    print(i, end="  ")

print()
# 배열의 인덱스로 순환
print('\n')
for i in range(10): # range(0,10) == range(10)
    print(i,end=" ")

v_array.append(11)
for i in range(10):
    print(v_array[i], end=' ')
print(' 끝 ')
print('========================특정숫자제거====================================')
v_array.pop(3)
print(v_array)

print("===============리스트100까지 'v_array'======================")

v_array = list(range(100))
print(v_array)

# 배열내의 값을 수정
# v_array 인덱스 0번 값을 100으로 바꾸고자 한다.
v_array[0] = 100


print(v_array)


print("===================3을 곱하고자 한다==============")
for i in range(len(v_array)):
    v_array[i] = v_array[i]*3
print(v_array)

print("\n배열내의 홀수 개수 세기\n")
v_count = 0
# for문을 이용 v_array 배열 순회
# 각 값이 홀수일때만 v_count 를 1 증가시키기

for num in v_array:
    if num % 2 == 1: #홀수
        v_count += 1 #1 증가시켜라
print(v_count)

print("\n v_sum 값\n")
# 배열 내 짝수 값들만 골라서 더한 값 얻기
# 해당짝수를 v_sum에 더하기
v_sum = 0
for num in v_array:
    if num % 2 == 0:
        v_sum += num

print(v_sum)