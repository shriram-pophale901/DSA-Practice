'''

5. Valid Palindrome
Problem: Check if a given string is a palindrome, considering only alphanumeric
characters and ignoring cases.
• Input Format: A single line of string (may contain spaces/symbols).
• Output Format: true if palindrome, else false.
• Example:
o Input: A man, a plan, a canal: Panama
o Output: true
• Test Cases:
o Input: race a car → Output: false
o Input: (empty string) → Output: true

'''

inp = input()
print(inp)
clean = ""
for ch in inp:
    
    if ch.isalnum():
        clean+=ch.lower()

if clean == clean[::-1]:
    print("true")

else:
    print("false")


