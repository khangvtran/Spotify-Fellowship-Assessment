
"""
Khang Vinh Tran
Spotify Assessment 06/12/2018
Language: Python 3

Question 1 -- sortByStrings(s,t): Sort the letters in the string s by the order they occur in the string t. 
You can assume t will not have repetitive characters.
For s = "weather" and t = "therapyw", the output should be sortByString(s, t) = "theeraw".
For s = "good" and t = "odg", the output should be sortByString(s, t) = "oodg".
"""



def sortByStrings(s, t):
    """
    Design: from t, create a list newT of letters that are also in s
    Create a result string, append to that string each letter in newT multiplied by its repeatation in s
    """
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
