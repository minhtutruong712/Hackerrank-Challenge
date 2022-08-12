def palindromeIndex(s):
    def isPalindrome(s): 
        return s == s[::-1]
        
    def Solve (s): 
        i = 0
        j = len(s)
        while i<j and s[i] == s[j-1]:
            i += 1
            j -= 1
        if i>=j:
            return -1
        else: 
            if isPalindrome(s[i+1:j]): 
                return i
            if isPalindrome(s[i:j-1]):
                return j-1
        return -1
    return Solve(s)

    
            


