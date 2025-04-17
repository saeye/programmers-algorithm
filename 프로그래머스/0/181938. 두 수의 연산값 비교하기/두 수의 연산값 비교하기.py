def solution(a, b):
    ab_connect = int(str(a)+str(b))
    ab_multi = 2*a*b
    if ab_connect >= ab_multi:
        return ab_connect
    return ab_multi