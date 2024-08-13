def solution(polynomial):
    data = polynomial.split(' + ')
    x_result = 0
    int_result = 0
    for i in data:
        if 'x' in i:
            if len(i) == 1:
                x_result += 1
            else:
                x_result += int(i.replace('x', ''))
        else:
            int_result += int(i)
    
    if int_result > 0 and x_result > 1:
        return f"{x_result}x + {int_result}"
    
    # x가 1일 경우에는 1x 가 아닌 x 가 출력되야 함
    elif int_result > 0 and x_result == 1:
        return f"x + {int_result}"
    
    elif int_result > 0 and x_result == 0:
        return f"{int_result}"

    elif int_result == 0 and x_result > 1:
        return f"{x_result}x"
    
    elif int_result == 0 and x_result == 1:
        return f"x"
    
    elif int_result == 0 and x_result == 0:
        return f"0"