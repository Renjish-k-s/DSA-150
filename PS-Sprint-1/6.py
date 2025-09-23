# Identifying Palindromes

# method 1
string=input("Enter a string: ")
# if string==string[::-1]:
#     print("String is palidrome")
# else:
#     print("String is not palindrome")


# method 2

low=0
high=len(string)-1
c=0
while low<high:
    if string[low]!=string[high]:
        c=1
        break
    low+=1
    high-=1
if c:
    print("It is not palindrome")
else:
    print("it is palindrome")

        