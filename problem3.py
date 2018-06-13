'''
Khang Vinh Tran
06/12/2018
Python 3

Question 3 -- changePossibilities(amount,amount): Your quirky boss collects rare, old coins.
They found out you're a programmer and asked you to solve something they've been wondering for a long time. 

Write a function that, given an amount of money and an array of coin denominations,
computes the number of ways to make the amount of money with coins of the available denominations. 

Example: for amount=4 (4¢) and denominations=[1,2,3] (1¢, 2¢ and 3¢), 
your program would output 4—the number of ways to make 4¢ with those denominations: 

1¢, 1¢, 1¢, 1¢
1¢, 1¢, 2¢
1¢, 3¢
2¢, 2¢
'''

def changePossibilities(amount, denominations):
    if not amount >= 0 or amount < min(denominations):
        print("There is no possible way.")
        print("Amount must be at least 0 and at least the minimum of denomations")
        return 0
    else:
        combinationCount = [0]*(amount+1)
        combinationCount[0] = 1
        for coinValue in denominations:
            for amount in range(len(combinationCount)):
                if amount >= coinValue:
                    combinationCount[amount] += combinationCount[amount-coinValue]
    return combinationCount[-1]
        
        


if __name__ == "__main__":
    
    print("\n* Test case ")
    amount=4 
    denominations=[1,2,3]
    print("Amount = %d" % (amount))
    print("Denomations = ", end = "")
    print(denominations)
    result = changePossibilities(amount, denominations)
    print("Result = %d" % (result))
    
    print("\n* Test with no possibilities ")
    amount = -1 
    denominations=[1,2,3]
    print("Amount = %d" % (amount))
    print("Denomations = ", end = "")
    print(denominations)
    result = changePossibilities(amount, denominations)
    print("Result = %d" % (result))
   
    print("\n* Test with no possibilities ")
    amount = 3 
    denominations=[5,10]
    print("Amount = %d" % (amount))
    print("Denomations = ", end = "")
    print(denominations)
    result = changePossibilities(amount, denominations)
    print("Result = %d" % (result))     
    
    print("\n* Test case ")
    amount = 100 
    denominations=[1,2,5, 10, 25]
    print("Amount = %d" % (amount))
    print("Denomations = ", end = "")
    print(denominations)
    result = changePossibilities(amount, denominations)
    print("Result = %d" % (result))    
    
    
    
'''

* Test case 
Amount = 4
Denomations = [1, 2, 3]
Result = 4

* Test with no possibilities 
Amount = -1
Denomations = [1, 2, 3]
There is no possible way.
Amount must be at least 0 and at least the minimum of denomations
Result = 0

* Test with no possibilities 
Amount = 3
Denomations = [5, 10]
There is no possible way.
Amount must be at least 0 and at least the minimum of denomations
Result = 0

* Test case 
Amount = 100
Denomations = [1, 2, 5, 10, 25]
Result = 3546

'''