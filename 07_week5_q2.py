def solution(s):
    # 문자열은 변경 불가능 --> list로 변환
    
    list_s = list(s)
    
    for i in range(len(list_s)):
        for j in range(len(list_s)-1):

            if list_s[j+1] > list_s[j]:
                temp = list_s[j]
                list_s[j] = list_s[j+1]
                list_s[j+1] = temp
            
    return ''.join(list_s)


print(solution('Zbcdefg'))