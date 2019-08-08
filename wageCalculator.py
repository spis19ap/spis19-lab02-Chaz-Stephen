# Calculates a woman's wage based on a man's wage and the gender wage gap
def convertWageMtoW(mWage):
   wageGap = 0.182
   ratio = 1-wageGap
   return mWage * ratio

# Test Case 1
print (convertWageMtoW(100))
# Test Case 2
print (convertWageMtoW(76.2))
# Test Case 3
print (convertWageMtoW(0))
# Test Case 4
print (convertWageMtoW(98.45))
# Test Case 5
print (convertWageMtoW(0.68))

