#PF-Assgn-31
def check_palindrome(word):
    word_len=len(word)
    count=0
    for i in range(len(word)):
        if (word[i]==word[-i-1]):
            count+=1
    if(count==word_len):
        return True
    else:
        return False

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")
