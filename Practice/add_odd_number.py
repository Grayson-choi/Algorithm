T = int(input())
for test_case in range(1, T + 1):
    num_list = map(int, input().split())
    int_num_list = [x for x in num_list if x % 2 == 1]
    print(sum(int_num_list))