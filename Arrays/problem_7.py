'''
8. Missing Number 
Problem: Given an array containing n distinct numbers in the range $[0, n]$, find the one 
number that is missing from the array. 
• Input Format: 
1. An integer n. 
2. n space-separated integers. 
• Output Format: The missing integer. 
• Example: 
o Input: 
3 
3 0 1 
o Output: 2 
• Test Cases: 
1. Input: 2, 0 1 → Output: 2 
2. Input: 9, 9 6 4 2 3 5 7 0 1 → Output: 8

'''


n = int(input())

lst = list(map(int , input().split()))
a=min(lst)
for i in range(n + 1):

    if i not in lst:
        print(i)
        break



