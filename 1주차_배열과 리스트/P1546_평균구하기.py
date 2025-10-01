# 문제
# M: 주어진 점수들 중 최댓값
# 모든 점수를 점수/M*100으로 수정 
# 새로운 평균 산정

# 입력
# 첫째 줄: 시험 본 과목의 개수
# 둘째 줄: 현재 성적(0~99, 적어도 하나의 값은 0보다 큼)



# 점수 입력
N = input()
score_list = list(map(int, input().split()))

# 최댓값 선정
M = max(score_list)
# 새로운 점수 리스트
new_score_list = []

# 새로운 점수를 리스트에 추가
for i in score_list:
    new_score_list.append(i/M*100)

# 평균 도출
average = sum(new_score_list) / len(new_score_list)
    
print(average)