def solution(board, moves):
    answer = 0
    line = []
    for move in moves:
        # print(f"move: {move}")
        for i in board:
            if i[move-1] != 0:
                # print(board)
                line.append(i[move-1])
                i[move-1] = 0
                # print(board)
                # print(line)
                if len(line) > 1 and line[-2] == line[-1]:
                    answer += 2
                    line.pop()
                    line.pop()
                break
            # line.append()
    return answer