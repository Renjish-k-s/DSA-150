# 5. **Generating the Fibonacci Series**  

def fibo(num):
    if num == 0 or num ==1:
        return num
    else:
        return fibo(num-2)+fibo(num-1)
    
limit=int(input("Enter the limit"))
for i in range(limit+1):
    print(fibo(i),end=",")