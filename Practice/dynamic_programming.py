# 민연이는 학원 쉬는 시간에 친구들을 상대로 새꼼달꼼 장사를 합니다.

# 그러다 문뜩, 갖고 있는 새꼼달꼼으로 벌어들일 수 있는 최대 수익이 궁금해졌는데요...


# ## 문제

# 민연이가 새꼼달꼼으로 벌어들일 수 있는 최대 수익을 리턴시켜 주는 함수 `max_profit`을 작성해 보세요. `max_profit`은 파라미터로 개수별 가격이 정리되어 있는 리스트 `price_list`와 총 갖고 있는 새꼼달꼼 개수 `count`를 받습니다.

# 예를 들어 `price_list`가 `[0, 100, 400, 800, 900, 1000]`라면,


# 1. 새꼼달꼼 0개에 0원
# 2. 새꼼달꼼 1개에 100원
# 3. 새꼼달꼼 2개에 400원
# 4. 새꼼달꼼 3개에 800원
# 5. 새꼼달꼼 4개에 900원
# 6. 새꼼달꼼 5개에 1000원

# 이렇게 가격 책정이 된 것입니다.

# 만약 오늘 민연이가 새꼼달꼼 5개를 판매한다면, 최대로 얼마를 벌 수 있을까요? 한 친구에게 3개 팔고, 한 친구에게 2개를 팔면 $800 + 400$을 해서 총 1200원의 수익을 낼 수 있습니다.





def max_profit(price_list, num):
        result= [0,price_list[1]]

        for i in range(2, num + 1):
                result_cache=[]
                if i < len(price_list):
                        result_cache.append(price_list[i])
                for j in range(1, i // 2 + 1):
                        result_cache.append(result[i - j] + result[j])
                result.append(max(result_cache))
        return result[num]


print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000], 9))
print(max_profit([0, 100, 400, 800, 900, 1000], 8))
print(max_profit([0, 100, 400, 800, 900, 1000], 7))
print(max_profit([0, 100, 400, 800, 900, 1000], 6))
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 4))
print(max_profit([0, 100, 400, 800, 900, 1000], 3))