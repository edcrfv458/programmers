def solution(nums):
    n = len(nums)
    answer = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                num = nums[i] + nums[j] + nums[k]
                data = [i for i in range(2, int(num**0.5) + 1) if num%i == 0]
                if not data:
                    answer += 1
    return answer