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
    
    result = []
    if x_result > 0:
        if x_result == 1:
            result.append("x")
        else:
            result.append(f"{x_result}x")
    if int_result > 0:
        result.append(str(int_result))
    
    return ' + '.join(result)
    # if x_result == 0 and int_result != 0:
    #     return f"{int_result}"
    # elif x_result != 0 and int_result == 0:
    #     return f"{x_result}x"
    # elif x_result != 0 and int_result != 0:
    #     return f"{x_result}x + {int_result}"
    # else:
    #     return f"0"