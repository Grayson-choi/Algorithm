# 순열
# 서로 다른 정수를 입력받아 가능한 모든 순열을 리턴
import itertools

nums = [1, 2, 3]

n = 4
k = 2


print(list(map(list, itertools.permutations(nums))))

# 전체 수 n을 입력받아서 k 개의 조합을 만듬
print(list(itertools.combinations(range(1, n+1), k)))