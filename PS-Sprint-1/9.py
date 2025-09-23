# 9. **Summing Digits of a Number**  


number=int(input("Enter the number"))

res=0
while number:
    dig=number%10
    res+=dig
    number//=10

print(res)