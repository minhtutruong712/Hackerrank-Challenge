import string 
"""
Complete the caesarCipher function in the editor below.

caesarCipher has the following parameter(s):

string s: cleartext
int k: the alphabet rotation factor
Returns

string: the encrypted string


Sample Input
11
middle-Outz
2


Sample Output
okffng-Qwvb

Explanation
Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab

m -> o
i -> k
d -> f
d -> f
l -> n
e -> g
-    -
O -> Q
u -> w
t -> v
z -> b

"""

def caesarCipher(s, k):     
    k = k%26                        # 26 is the length of alphabet string 
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase  
    s1_change = s1[k:] + s1[:k]     # string slice to get the rotated string for the lower
    s2_change = s2[k:] + s2[:k]     # string slice to get the rotated string for the upper
    s = list(s)                     # convert string to a list to replace element according its index
    s_new = ''

    for k in range(len(s)): 
        for i,j in enumerate(s1):
            if s[k] == j: 
                s[k] = s1_change[i]
                break
        for i,j in enumerate(s2):
            if s[k] == j: 
                s[k] = s2_change[i]            
                break
    for i in s: 
        s_new +=i
    return s_new

if __name__ == '__main__':
    """Enter the length of the string."""
    print('Please enter n')
    n = int(input().strip())

    """Enter the string."""
    print('Please enter the string')
    s = input()

    """Enter the rotated number."""
    print('Please enter k - the rotated number')
    k = int(input().strip())

    result = caesarCipher(s, k)
    print(result)

