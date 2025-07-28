class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[x] will store the minimum number of coins needed to make amount x.
        # Start by assuming all amounts are impossible to form, hence we use 'infinity'.
        # Example: if amount = 11, we create a dp list of size 12 (0 to 11).
        dp = [float('inf')] * (amount + 1)

        # Base case - it takes 0 coins to make the amount 0
        dp[0] = 0

        # Go through each coin one by one
        for coin in coins:
            # We will try to build amounts from the value of the coin up to the target amount
            for current_amount in range(coin, amount + 1):
                # Check if current_amount can be formed by using the current coin
                # If we include this coin, the remaining amount is current_amount - coin
                remaining_amount = current_amount - coin

                # If the remaining amount was possible (dp[remaining_amount] is not infinity)
                if dp[remaining_amount] != float('inf'):
                    # We take the minimum coins between the current value dp[current_amount]
                    # and the value of dp[remaining_amount] + 1 (for the current coin we add)
                    dp[current_amount] = min(dp[current_amount], dp[remaining_amount] + 1)

        # After processing all coins, check dp[amount]
        # If it's still infinity, it means it's not possible to form this amount
        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]
