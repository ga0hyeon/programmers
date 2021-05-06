def matchAllCases(prevSet, count, N, number, repetitions):
    if count == 8:
        return -1
    curSet = set({})
    for val in prevSet:
        if val + N == number or val - N == number or val * N == number or int(val / N) == number:
            return count + 1
        else:
            curSet = curSet.union( {val + N, val - N, val * N, int(val / N)})
    if count < 5:
        curSet.add(repetitions[count])
    return matchAllCases(prevSet.union(curSet), count + 1, N, number, repetitions)


def solution(N, number):
    answer = 0
    repetitions = [ 1, 11, 111, 1111, 11111 ]
    repetitions = [ x * N for x in repetitions ]

    if number in repetitions:
        answer = repetitions.index(number) + 1
    else:
        answer = matchAllCases({N}, 1, N, number, repetitions)

    return answer


print(solution(5, 12))
print(solution(2, 11))