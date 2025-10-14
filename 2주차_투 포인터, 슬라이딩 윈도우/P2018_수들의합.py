# 시간 제한 2초 / 백준 2018번
# https://www.acmicpc.net/problem/2018

# 문제 분석 ----------------------------------------------------
# 합쳐서 N이 된다는 조건의 연속 구간을 찾는 문제 = 투 포인터
# 시작 인덱스와 종료 인덱스를 사용하여 문제 접근
# 구간의 합을 구하는 문제 = start_index와 end_index가 1(자연수)에서 시작
# 구간의 합인 sum 값도 1(자연수)에서 시작
# --------------------------------------------------------------

# 슈도코드 ------------------------------------------------------
# 자연수 n 입력 받기
# start, end, sum, count 선언 (초기화 1)
#
# while end != n:
#     1) sum = n
#     count += 1
#     end += 1 (그 다음 찾기 위해)
#     sum += end (변한 구간 반영)
#     2) sum > n
#     sum -= start (이미 초과 되었기 때문에 시작점을 바꿔야 함)
#     start += 1
#     3) sum < n
#     end += 1
#     sum += end (변한 구간 반영)
#
# print(c)
# ----------------------------------------------------------------  

import sys
input = sys.stdin.readline

n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index 
    elif sum > n:
        sum -= start_index
        start_index += 1
    else: 
        end_index += 1
        sum += end_index
        
print(count)

# 시간 복잡도 = O(N)