def solution(a, b):
    ab_connect = int(str(a)+str(b))
    ab = 2*a*b
    if ab_connect >= ab:
        return ab_connect
    return ab
