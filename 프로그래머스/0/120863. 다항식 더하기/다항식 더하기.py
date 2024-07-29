def solution(polynomial):
    answer = polynomial.replace(' ','').split('+')
    
    x_data = [i for i in answer if "x" in i]
    int_data = [i for i in answer if "x" not in i]
    
    x_result = 0
    int_result = 0
    
    for i in x_data:
        if i == 'x':
            x_result += 1
        else:
            x_result += int(i.replace('x',''))
            
    int_result = sum(int(i) for i in int_data)
    
    ## x 계수가 0, 정수 계수가 0이 아님
    ## x 계수가 1, 정수 계수가 0임
    ## x 계수가 1, 정수 계수가 0이 아님
    ## x 계수가 2이상, 정수 계수가 0임
    ## x 계수가 2이상, 정수 계수가 0이 아님
    
    if x_result == 0 and int_result != 0:
        return f"{int_result}"
    elif x_result > 0:
        if x_result == 1 and int_result == 0:
            return f"x"
        elif x_result == 1 and int_result != 0:
            return f"x + {int_result}"
        elif x_result > 1 and int_result == 0:
            return f"{x_result}x"
        elif x_result > 1 and int_result != 0:
            return f"{x_result}x + {int_result}"