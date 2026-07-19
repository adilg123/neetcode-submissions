class Solution:
    '''
U: buy and sell stocks, goal is to get max profit
    looking at example, you want to keep track of the max number and the min number
    edge case - if max num is first number then return right away 
    *Correction, misunderstanding, scrap this part* 
    else -> use a R and L (two pointer approach) and keep track using
    a possible max variable, constantly update and return 
    note: no sorting, because order matters here


M: cover all the cases (greedy?) and return
P: implementation
    maxprf = 0
    two pointers, r, l (both start at index 0)

'''
    def maxProfit(self, prices: List[int]) -> int:
       # if max(prices[i]) == prices[1]:
        #    return prices[1]
        curMax = 0
        l, r = 0, 1
        while r < len(prices):
            if prices[r] > prices[l]:
                curMax += (prices[r] - prices[l])
            r += 1
            l += 1
        return curMax
