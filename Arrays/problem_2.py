'''
Problem: A company wants to check if any Employee ID has been entered twice in their
database. Return true if any value appears at least twice, and false if every element is
distinct.
• Input Format:
1. An integer n.
2. n space-separated integers.
• Output Format: true or false.
• Example:
o Input:
4
1 2 3 1
o Output: true
• Test Cases:
1. Input: 4, 1 2 3 4 → Output: false
2. Input: 6, 1 1 1 3 3 4 → Output: true

'''

n = int(input())

data = list(map(int , input().split()))
count = 0
for i in range(n):
    for j in range(i+1 ,n ):
        if data[i] == data[j]:
            count+=1

if count>0:
    print(True)

else:
    print(False)


