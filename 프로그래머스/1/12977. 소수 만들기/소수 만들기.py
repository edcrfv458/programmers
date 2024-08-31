def solution(nums):
    count = 0   # 3개 요소 합쳐서 소수인 묶음의 수를 저장할 변수
    # i는 0부터 len(nums)-3의 인덱스까지
    for i in range(len(nums)-2):
        # j는 i+1부터 len(nums) - 2의 인덱스까지
        for j in range(i+1, len(nums)-1):
            # k는 j+1부터 len(nums) - 1의 인덱스까지
            for k in range(j+1, len(nums)):
                s = nums[i] + nums[j] + nums[k]     # 3개 요소를 합침
                a = [t for t in range(1, s+1) if s % t == 0]    # 약수가 2개이면 소수
                if len(a) == 2:
                    count += 1
    return count