def chooseCity(n, city):
    result = []
    for i in city:
        temp = 0
        for j in city:
            if i[0] != j[0]:
                temp += abs(i[0] - j[0]) * j[1]
        result.append([i[0], temp])

    answer = sorted(result, key=lambda x: x[1])[:1][0][0]
    return answer


print(chooseCity(5, [[1, 2], [2, 1], [3, 1], [4, 1], [5, 15]]))
