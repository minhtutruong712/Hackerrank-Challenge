def palindromeIndex(s):
    def isPalindrome(s): 
        return s == s[::-1]
        
    def Solve (s): 
        i = 0
        j = len(s)-1
        while i<j and s[i] == s[j]: # while will loop when no different pattern is found
            i += 1                  
            j -= 1
        if i>=j:                    
            return -1               # when while condition is not met and the string is loop all      
        else: 
            if isPalindrome(s[i+1:j+1]): 
                return i
            if isPalindrome(s[i:j]):
                return j
        return -1
    return Solve(s)

    
            


