# 2. **Checking for Prime Numbers**  

# if a number is prime it will be not not have more than two divisors
# A prime number is a positive integer greater than 1 and has no positive divisors other than 1 and itself

import math
def checkprime(num):
    if num<=0:
        return "invalid number"
    elif num==1:
        return "Non Prime"
    elif num==2:
        return "Prime"
    else:
        for i in range(2,(num//2)+1):
            if num%i==0:
                return "Prime"
    return "Non Prime"


num=int(input("Enter the number to check= "))
print(checkprime(num))

        