def Jaden_Case(s):
    r = ''
    for i, e in enumerate(s.strip().split()):
        r += e.capitalize()
        if i < len(s.split(' ')) - 1:
            r += ' '
    return r

# def Jaden_Case(s):
#     return s.title().strip()


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))
