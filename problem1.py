
"""
Khang Vinh Tran
Spotify Assessment 06/12/2018
Language: Python 3

Question 1 -- sortByStrings(s,t): Sort the letters in the string s by the order they occur in the string t. 
You can assume t will not have repetitive characters.
For s = "weather" and t = "therapyw", the output should be sortByString(s, t) = "theeraw".
For s = "good" and t = "odg", the output should be sortByString(s, t) = "oodg".
"""




"""
Design:
First, make sure that any letter that is in s must also be in t
from t, create a list newT of letters that are also in s
Create a result string, append to that string each letter in newT multiplied by its repeatation in s
"""

def sortByStrings(s, t):  
    newS = [letter for letter in s if not letter in t]
    if (newS):
        print("* There exists at least 1 letter in s that is not in t. Function aborted.")
        return
    
    newT = [letter for letter in t if letter in s]
    result = str()
    for letter in newT:
        result += letter*s.count(letter)
    return(result)
    
    

if __name__ == "__main__":
    s1 = "weather"
    t1 = "therapyw"  
    result1 = sortByStrings(s1, t1)
    print("s = %s, t = %s, result = %s" % (s1, t1, result1))

    s2 = "good" 
    t2 = "odg"
    result2 = sortByStrings(s2, t2)
    print("s = %s, t = %s, result = %s" % (s2, t2, result2))
    
    print("\nEdge Case")
    s3 = "weatherq"
    t3 = "therapyw"
    result3 = sortByStrings(s3, t3)
    print("s = %s, t = %s, result = %s" % (s3, t3, result3))


'''
Test Cases
s = weather, t = therapyw, result = theeraw
s = good, t = odg, result = oodg

Edge Case
* There exists at least 1 letter in s that is not in t. Function aborted.
s = weatherq, t = therapyw, result = None
'''