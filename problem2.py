'''
Khang Vinh Tran
Spotify Assessment 06/12/2018
Language: Python 3



Question 2 -- decodeString(s): Given an encoded string, return its corresponding decoded string. 

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. 
Note: k is guaranteed to be a positive integer. 

For s = "4[ab]", the output should be decodeString(s) = "abababab" 
For s = "2[b3[a]]", the output should be decodeString(s) = "baaabaaa"
'''





'''
Design:
There are 2 keys ideas in my approach: RECURSION and QUEUE

* As traversing through string s in decodeString(s), if the current element is a letter, we append it to the result.
If it is an integer, call findCorrespodingBracketIndex() to help indicate exacly the sub string that 
should be multiplied up. This function then call itself (RECURSIVE STEP) with argument as the substring

* When encounter an integer, decodeString() will call findCorrespodingBracketIndex(s, startingIndex).
This helper function will find the matching close bracket ']' for the open bracket '['
that follows the integer. This function uses a QUEUE
'''

def decodeString(s):
    result = str()
    for i, element in enumerate(s):
        if element.isalpha():
            result += element
        elif element.isdigit():
            num = int(element)
            closeBracketIndex = findCorrespodingBracketIndex(s, i+1)
            result += (num-1) * decodeString(s[i+1 : closeBracketIndex])  # Recursive call
    return(result)
        
    

def findCorrespodingBracketIndex(s, starting):
    q = list()     # treat q as a queue
    for i in range(starting, len(s)):
        if s[i] == '[':
            q.append(s[i])
        elif s[i] == ']':
            q.pop(0)
        if not q:  # if the queue is empty
            return i
    


if __name__ == '__main__':

    s = "4[ab]"
    result = decodeString(s)
    print("s = %s, result = %s" % (s, result))
    
    s = "2[b3[a]]"
    result = decodeString(s)
    print("s = %s, result = %s" % (s, result))
    
    s = "b3[a]"
    result = decodeString(s)
    print("s = %s, result = %s" % (s, result))    
    
    s = "2[abc]2[b3[a]]"
    result = decodeString(s)
    print("s = %s, result = %s" % (s, result))    
    



'''
s = 4[ab], result = abababab
s = 2[b3[a]], result = baaabaaa
s = 2[abc]2[b3[a]], result = abcabcbaaabaaa
'''