# Write a program that takes an array denoting the daily stock price, and returns the maximum profit that
# could be made by buying and then selling one share of that stock.There is no need to buy if no profit is possible.

def buy_and_sell_stock_once_solution (daily_prices):

    max_profit = 0
    min_so_far = daily_prices[0]

    for price in daily_prices:
        curr_profit = price - min_so_far
        max_profit = max(curr_profit, max_profit)
        min_so_far = min(min_so_far, price)

    return max_profit


