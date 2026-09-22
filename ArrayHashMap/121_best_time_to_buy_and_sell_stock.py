"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""

"""
My first idea is to iterate through the prices array. 
During this process, I keep track of the minimum price I have seen so far. 
For each day, I calculate the profit by subtracting the minimum price from the current price, and store each day's profit in an array. 
Finally, I return the maximum value in the profit array.
"""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        profits = []

        min_price = prices[0]
        for price in prices:
            profit = price - min_price
            profits.append(profit)

            if price < min_price:
                min_price = price

        return max(profits)


"""
My second idea is to optimize the space complexity. It is not necessary to use an array to store the profit for every day. 
Instead, I can use a variable to keep track of the maximum profit. 
During the iteration, I update the minimum price and the maximum profit whenever necessary. Finally, I return the maximum profit."""
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        min_price = prices[0]
        max_profit = 0
        for price in prices:
            profit = price - min_price

            if price < min_price:
                min_price = price

            if profit > max_profit:
                max_profit = profit

        return max_profit