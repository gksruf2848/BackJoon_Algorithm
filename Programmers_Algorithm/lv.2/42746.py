def solution(numbers):
    answer = list(map(str,numbers))
    answer.sort(key=lambda x: x*4, reverse=True)
    
    return str(int(''.join(answer)))