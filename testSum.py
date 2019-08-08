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
