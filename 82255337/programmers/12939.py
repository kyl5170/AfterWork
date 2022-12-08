def solution(s):
    mylist = list(map(int, list(s.split())))
    a = min(mylist)
    b = max(mylist)
    return str(a)+' '+str(b)
            