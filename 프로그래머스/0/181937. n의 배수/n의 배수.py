def solution(num, n):
    if num % n == 0:
        return 1
    return 0

'''
int(True)는 1, int(False)는 0 이니까

def solution(num, n):
    return int(num % n == 0)

이렇게 쓰면 더 깔끔하다.

'''