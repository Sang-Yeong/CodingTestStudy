# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = []
    
    answer = [x+x*i for i in range(n)]
    
    return answer

print(solution(-4, 2))