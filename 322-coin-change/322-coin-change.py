class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [10001] * (amount + 1)
        arr[0] = 0
        for coin in coins:
            for i in range(coin, amount+1):
                if arr[i-coin] != 10001:
                    arr[i] = min(arr[i], arr[i-coin] + 1)

        if arr[amount] == 10001:
            return -1
        
        return arr[amount]