def solution(nums):
    answer = 0
    l = len(nums)
    for i in range(l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                s = nums[i] + nums[j] + nums[k]
                s_sosu = []
                for h in range(2, int(s**0.5)+1):
                    if s % h == 0:
                        s_sosu.append(h)
                if not s_sosu:
                    answer += 1
    return answer