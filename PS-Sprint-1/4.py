# 4. **Calculating Armstrong Numbers**  

num=int(input("Enter the number to check"))
res=0
while num:
    lastdig=num%10
    num//=10
    res+=lastdig**3
print(res)
