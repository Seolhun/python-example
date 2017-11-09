def chooseCity(n, city):
    # 좌표의 범위는 음수가 포함됩니다. 또한 좌표는 정렬되어 있지 않습니다.
    city.sort(key=lambda x: x[0])
    total = sum([x[1] for x in city])
    s = 0
    for i in range(n):
        s += city[i][1]
        if s >= total // 2:
            break
    return city[i][0]


# 아래 코드는 출력을 위한 테스트 코드입니다.
print(chooseCity(3, [[1, 5], [2, 2], [3, 3]]))


# def myFn(s):
#     return s[0]
#
#
# def chooseCity(n, city):
#     answer = 0
#     bfrval = 0
#     left = [0 for x in city]
#     leftd = [0 for x in city]
#     right = [0 for x in city]
#     rightd = [0 for x in city]
#
#     cities = sorted(city, key=myFn)
#
#     for i in range(n):
#         if i == 0:
#             left[i] = 0
#             leftd[i] = 0
#         else:
#             leftd[i] = leftd[i - 1] + cities[i - 1][1]
#             left[i] = left[i - 1] + leftd[i] * (cities[i][0] - cities[i - 1][0])
#         j = n - 1 - i
#         if j == n - 1:
#             right[j] = 0
#             rightd[j] = 0
#         else:
#             rightd[j] = rightd[j + 1] + cities[j + 1][1]
#             right[j] = right[j + 1] + rightd[j] * (cities[j + 1][0] - cities[j][0])
#
#     for i in range(n):
#         val = left[i] + right[i]
#         if bfrval == 0:
#             bfrval = val
#         elif val < bfrval:
#             bfrval = val
#             answer = i
#
#     return cities[answer][0]
#
#
# # 아래 코드는 출력을 위한 테스트 코드입니다.
#
# print(chooseCity(3, [[1, 5], [2, 2], [3, 3]]))
