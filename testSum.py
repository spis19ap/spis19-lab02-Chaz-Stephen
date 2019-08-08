# The goal of this program is to practice Python constructs
def getNumber():
#empty string to add numbers
   allSymbols = ""
#while loop to repeat the digit prompt
   while True:
     symbols = input("Enter a digit: ")
#in the case a user enters a negative digit, the operation breaks
     if int(symbols) < 0:
         break
     allSymbols += symbols
#once the operation is broken, this code presents the user with all the digits they entered prior as one number 		
   number = int(allSymbols)
   return number

print (getNumber())

#this code here gets the digits from the program above and adds the digits
def sumDigits (x):
#variables with equations for getting each individual digit
    ones = x%10
    tens = x//10%10
    hundreds = x//100
#equation to add each of these individual digits together    
    sum = ones + tens + hundreds
    return sum

print (sumDigits(getNumber()))
