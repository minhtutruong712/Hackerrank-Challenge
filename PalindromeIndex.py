def palindromeIndex(s):
    def isPalindrome(s): 
        print(1)
        return s == s[::-1]
        
    def Solve(s): 
        i = 0
        j = len(s)
        while i < j: 
            if isPalindrome (s[i:j]): 
                print (i,j)
                return -1
            if isPalindrome (s[i+1:j]):
                print(i,j)
                return i
            if isPalindrome (s[i:j-1]):
                print(i,j)
                return j-1
            i += 1
            j -= 1
    return Solve(s)

i = palindromeIndex('bcdefghijklmnopqrstuvwxyza')
print(i)

