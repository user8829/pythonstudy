v_array =[]

# 1~100 사이의 숫자 중 3의 배수만 v_array에 담기
for i in range(100):    # 반복을 시키는 조건
    if i % 3 == 0:      # 찾는 조건
        v_array.append(i) # 메소드
print(v_array)            #프린트

print("\n")
# v_array 내부 값들의 전체 합
v_sum = 0
for i in v_array:
    v_sum += i
print("합:", v_sum)

# v_array 내부 값들의 평균 값
v_mean = v_sum / len(v_array) # 평균은 전체합 / 갯수
print(v_mean)



# 메소드(method), 함수(funtion)

# 배열에 대해 배열 내 값들의 평균을 계산해 주는 메소드 선언
# def 함수명(파라미터명):
def mean(p_array): # 파라미터로 들어온 배열은 p_array 에 담기고 p_array의 종합을 계산
    v_sum = 0
    for i in p_array:
        v_sum += i
    v_mean = v_sum / len(p_array)
    # 계산된 평균값을 메소드의 실행결과로서 리턴
    return v_mean
v_mean = mean(v_array)
print("평균값:", v_mean)

a_array = [1, 2, 3, 4, 5]
v_mean = mean(a_array)
print(v_mean)

print("========================================")
# 나이를 파라미터에 넣으면 세대를 리턴하는 메소드
v_age = 94 # 변수선언
v_gen = int(v_age / 10) * 10 # 계산식
print(v_gen, "대")           # 출력값


def gen(p_age):                     # 새변수
    v_gen = int(p_age / 10) * 10    # 새변수가 저장된 파라미터 계산식을 원하는 변수 값을 리턴(답)한다.
    return v_gen
v_age = 45
v_gen = gen(v_age)
print(v_gen, "대") # 40대