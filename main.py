class Solution:
    def maxProfit(self, prices: [int]) -> int:
        profit = 0
        buy = 0
        sell = 0
        has_stocks = False
        sold = False

        if len(prices) < 2:
            return 0

        for i in range(len(prices)-1):
            if not has_stocks and prices[i] < prices[i + 1]:
                buy = prices[i]
                has_stocks = True
            elif has_stocks and prices[i] > prices[i + 1]:
                sell = prices[i]
                has_stocks = False
                sold = True

            if sold:
                sold = False
                profit += sell - buy

        if has_stocks:
            profit += prices[-1] - buy

        return profit


if __name__ == '__main__':
    s = Solution()
    test = [7,6,4,3,1]
    print(s.maxProfit(test))
