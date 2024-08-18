def solution(todo_list, finished):
    result = []
    for i, f in enumerate(finished):
        if f == False:
            result.append(todo_list[i])
    return result