def solution(triangle):
    answer = 0
    height = len(triangle)
    for h in range(0, height - 1):
        width = len(triangle[h])
        memory = [ 0 for x in range(width+1)]
        for w in range(0, width):
            memory[w] = max( memory[w] , triangle[h][w] + triangle[h+1][w])
            memory[w+1] = max(  memory[w+1] ,triangle[h][w]  + triangle[h+1][w+1])
        triangle[h+1] = memory

    answer = max(triangle[height - 1])

    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))