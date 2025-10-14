# 문제 
# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지의 합

# 입력
# 첫째 줄: 수의 개수 N, 합을 구해야 하는 횟수 M
# 둘째 줄: N개의 수 제공(~1000, 자연수)
# 셋째 줄+a: M개의 줄에는 합을 구해야 하는 구간 i(start)와 j(end)




N, M = map(int, input().split()) # 수의 개수 N, 합을 구해야 하는 횟수 M 
num_list = list(map(int, input().split())) # N개의 리스트

# 합배열 만들기
temp = 0
prefix_sum = [0] # 인덱스 조정
for i in num_list:
    temp = temp + i
    prefix_sum.append(temp)
    

result_list = [] # 결과 저장 리스트
# 구간합 구하기
# 합 배열 S의 구간 start~end = S[end]-S[start-1]
for i in range(M):
    start, end = map(int, input().split()) 
    result = prefix_sum[end]-prefix_sum[start-1]
    result_list.append(result)

for r in result_list:
    print(r)