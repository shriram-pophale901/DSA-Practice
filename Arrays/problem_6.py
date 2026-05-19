'''

6. Best Time to Buy and Sell Stock
Problem: You are given an array prices where prices[i] is the price of a given stock on the
$i^{th}$ day. You want to maximize your profit by choosing a single day to buy and a
different day in the future to sell.
• Input Format:
1. An integer n.
2. n space-separated integers.
• Output Format: Maximum profit possible.
• Example:
o Input:
    6
    7 1 5 3 6 4
o Output: 5 (Buy on day 2 at 1, sell on day 5 at 6).
• Test Cases:
1. Input: 5, 7 6 4 3 1 → Output: 0
2. Input: 2, 1 5 → Output: 4

'''
x = [7,1,5,3,6,4]

for i in range(len(x)):
    k = 1
    for j in range(i+1 , len(x)-1):
        if x[i] < x[j]:
            k+=1
        
        else:
            break

    if k> i:
        print(f"buy on day {i} at {x[i]}")

    else:
        print(0)
