class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') # 최소 가격 초기화
        max_profit = 0 # 최대 이익 초기화

        for price in prices:
            if price < min_price:
                min_price = price # 최소 가격 업데이트
            elif price - min_price > max_profit:
                max_profit = price - min_price # 최대 이익 업데이트

        return max_profit