#Given a string, write a python function to check if it is palindrome or not. 
#string is said to be palindrome if the reverse of the string is the same as string. 
#For example, “radar” is a palindrome, but “radix” is not a palindrome.

def isPalindrome(s):
    #s = s.lower()
    return s == s[::-1]

def isPalindrome1(s):
    for i in range(0,int(len(s)/2)):
        if s[i] != s[(len(s) -i - 1)]:
            return False
    return True
 
# Driver code
s = "malayalam"
ans = isPalindrome(s)
if ans:
    print("Yes")
else:
    print("No")

############

ans = isPalindrome1(s)
if ans:
    print("Yes")
else:
    print("No")

