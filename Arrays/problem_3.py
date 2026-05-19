'''

3. Move Zeroes (Common TCS Question)
Problem: Given an array of integers, move all 0's to the end of it while maintaining the
relative order of the non-zero elements. You must do this in-place.
• Input Format:
1. An integer n.
2. n integers.
• Output Format: The modified array separated by spaces.
• Example:
o Input:
5
0 1 0 3 12
o Output: 1 3 12 0 0
• Test Cases:
1. Input: 1, 0 → Output: 0
2. Input: 2, 4 0 → Output: 4 0


'''

n = int(input("Enter len"))
arr = list(map(int , input("enter ele").split()))

arr1 = [0]*n
print(arr1)
j = 0
for i in range(n):
    if arr[i]!=0:
        arr1[j] = arr[i]
        j+=1
print(arr1)

