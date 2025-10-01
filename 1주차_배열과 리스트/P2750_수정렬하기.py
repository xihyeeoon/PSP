#문제
# N개의 수가 주어졌을 때 이를 오름차순 정렬

#입력
# 1번째 줄에 수의 개수 N(1~1,000,000)
# 2번째 줄부터는 N개의 줄에 숫자 부여
# (단 이 수는 절댓값이 1,000,000보다 작거나 같음 / 수는 중복X)

# 정렬할 수의 개수(N)
# 정렬 수들(N개)


# 기본 리스트 입력
N = int(input())
num = []

for i in range(N):
    num.append(int(input()))


# 분할
def division(num):
    # 하나 남을 시 반환 
    if len(num) <= 1:
        return num
    # 2분할 
    mid = len(num)//2
    left = num[:mid]
    right = num[mid:]
    
    left2 = division(left)
    right2 = division(right)
    
    return merge(left2, right2)

# 합병
def merge(left, right):
    i, j = 0, 0
    sorted_num = []
    # 메인 비교
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_num.append(left[i])
            i += 1
        else: 
            sorted_num.append(right[j])
            j += 1
    # 남은 원소 비교 
    while i < len(left):
        sorted_num.append(left[i])
        i += 1
    while j < len(right):
        sorted_num.append(right[j])
        j += 1        
    return sorted_num

#리스트로 재저장
sorted_list = division(num)

#형식에 맞게 출력
for i in sorted_list:
    print(i)