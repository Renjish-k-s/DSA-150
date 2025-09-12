# odd or even
# A number becomes odd we could write it in the form of 2K+1 and even in the from of 2k 

# method 1

# num=int(input("Enter the number to check"))
# if num%2:
#     print(f"The number {num} is odd")
# else:
#     print(f"The number {num} is even")

# method 2

# num=int(input("Enter the number to check"))
# options=("Even","Odd")
# print(f"The number {num} is {options[num%2]}")

#method 3

def check(num):
    if num%2:
        return "odd"
    else:
        return "Even"
num=int(input("Enter the number to check"))
print(f"The number {num} is {check(num)}")


