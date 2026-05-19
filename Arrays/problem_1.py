
'''

1. Two Sum (Target Pair) 
Problem: Write a program to find the indices of two numbers in an array such that they 
add up to a specific target. Assume there is exactly one solution. 
• Input Format: 
1. An integer n (size of array). 
2. n space-separated integers (the array). 
3. An integer target. 
• Output Format: Print the indices of the two numbers. 
• Example: 
o Input: 
    4 
    2 7 11 15 
    9 
o Output: 0 1 
• Test Cases: 
1. Input: 3, 3 2 4, 6 → Output: 1 2 
2. Input: 2, 3 3, 6 → Output: 0 1 

'''

n = int(input())
a = list(map(int, input().split()))
b = int(input())

for i in range(n):
    for j in range(i + 1, n):
        if a[i] + a[j] == b:
            print(i, j)
            exit() 
