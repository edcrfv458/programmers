def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                s = nums[i] + nums[j] + nums[k]
                c = 0
                for t in range(2, int(s**0.5) + 1):
                    if s % t == 0:
                        c += 1
                if c == 0:
                    answer += 1
    return answer