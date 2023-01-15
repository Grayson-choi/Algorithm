import q

def rotate(y, x, height, width):
    global copy_arr
    q = deque()

    # 가로 줄 돌기
    for i in range(x, x + width):
        q.append(copy_arr[y][i])

    # 오른쪽 돌기
    for i in range(y + 1, y + height):
        q.append(copy_arr[i][x + width - 1])
        # print(i, x + width - 1)
        # print("--")


    for i in range(x + width - 2, x, -1):
        q.append(copy_arr[y + height - 1][i])
        print(y + height - 1, i)



    for i in range(y + height - 1, y, -1):
        q.append(copy_arr[i][x])

    q.rotate(1)  # 한칸 이동

    for i in range(x, x + width):
        copy_arr[y][i] = q.popleft()

    for i in range(y + 1, y + height):
        copy_arr[i][x + width - 1] = q.popleft()

    for i in range(x + width - 2, x, -1):
        copy_arr[y + height - 1][i] = q.popleft()

    for i in range(y + height - 1, y, -1):
        copy_arr[i][x] = q.popleft()

