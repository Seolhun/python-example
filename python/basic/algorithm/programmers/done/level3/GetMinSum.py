def getMinSum(A, B):
    # zip(iterable*)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])


# 아래 코드는 출력을 위한 테스트 코드입니다.

print(getMinSum([1, 2], [3, 4]))
