def solution(age):
    str_age = str(age)
    answer = ""
    data = {
        '0':'a',
        '1':'b',
        '2':'c',
        '3':'d',
        '4':'e',
        '5':'f',
        '6':'g',
        '7':'h',
        '8':'i',
        '9':'j'
    }
    for s in str_age:
        answer += data[s]
    return answer