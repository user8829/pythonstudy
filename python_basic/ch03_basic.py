# 다른 사람이 만들어 놓은 라이브러리(모듈) 가져오기(import)
import random

# 랜덤 숫자를 얻고 싶다.
# 로또 번호 6개를 얻고 싶다.
#1~45 사이의 랜덤 숫자 리턴
v_num = random.randint(1, 45)
print(v_num)
print("==========================")
# 라이브러리를 가져올 때 이름 설정
import random as rd
v_num = rd.randint(1,45)
print(v_num)

# myutill 가져오기
import library1

arr = [34, 5, 66, 32, 12]
v_mean = library1.mean(arr)
print(v_mean)

import library1 as mu
print(mu.gen(23))
