'''
4. Majority Element
Problem: Find the element that appears more than $n/2$ times in an array of size n. You
may assume that the majority element always exists.
• Input Format:
1. An integer n.
2. n space-separated integers.
• Output Format: The majority element.
• Example:
o Input:
    3
   3 2 3
o Output: 3
• Test Cases:
1. Input: 7, 2 2 1 1 1 2 2 → Output: 2
2. Input: 1, 5 → Output: 5

'''
import time

n = int(input("size"))
arr = list(map(int, input("ele: ").split()))
start =time.time()
for i in range(n):
    k = 1
    for j in range(i+1 , n):
        if arr[i] == arr[j]:
            k+=1
    if k > (n//2):
        print(arr[i])
        break

end = time.time()

print("time: ",end-start)





n = int(input())

arr = list(map(int, input().split()))
st = time.time()
count = {}

for num in arr:

    if num in count:
        count[num] += 1
    else:
        count[num] = 1

for key, value in count.items():

    if value > n // 2:
        print(key)
        break

en = time.time()

print("time: ",en-st)
