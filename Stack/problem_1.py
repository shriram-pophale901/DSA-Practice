'''
7. Valid Parentheses (Stack Based) 
Problem: Given a string containing just the characters (, ), {, }, [ and ], determine if the 
input string is valid. 
    • Input Format: A string. 
    • Output Format: true or false. 
    • Example: 
    o Input: ()[]{} 
    o Output: true 
• Test Cases: 
1. Input: (] → Output: false 
2. Input: ([)] → Output: false 
3. Input: {[]} → Output: true 

'''


s = input()

stack = []

for ch in s:

    # opening brackets
    if ch in "([{":
        stack.append(ch)

    else:

        # stack empty
        if not stack:
            print("false")
            break

        top = stack.pop()

        # matching check
        if (ch == ")" and top != "(") or \
           (ch == "]" and top != "[") or \
           (ch == "}" and top != "{"):

            print("false")
            break

else:
    
    if not stack:
        print("true")
    else:
        print("false")





