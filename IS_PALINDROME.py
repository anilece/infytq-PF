#PF-Assgn-40
def is_palindrome(word):
    word=word.lower()
    while(len(word)!=0):
        i=0
        if word[i]==word[-i-1]:
            word=word[i+1:-i-1]
            is_palindrome(word)
            if (len(word)==0):
                return True
        else:
            return False



result=is_palindrome("MadAM")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
