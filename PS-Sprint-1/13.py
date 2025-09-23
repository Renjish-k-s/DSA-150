# 13. **Reversing a String**  

string=input("Enter the string to reverse")
def reverse(string):
    rev=""
    for i in range(len(string)-1,-1,-1):
        rev+=string[i]
    return rev

print(reverse(string))
