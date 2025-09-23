# 10. **Finding the Greatest Common Divisor (GCD)**  


input1=int(input("Enter the first number"))
input2=int(input("Enter the second number"))

a=max(input1,input2)
b=min(input1,input2)

while b:
    a,b=b,a%b
print(a)

