#14. **Finding the Largest and Smallest Numbers in an Array**  

array=[2,3,4,1,5]
"""def finder(array):
    return[max(array),min(array)]
maxi,mini=finder(array)"""


#Method 2


def maximum(array):
    num=float('-inf')
    for i in array:
        if i>num:
            num=i
    return num

def minimum(array):
    num=float('inf')
    for i in array:
        if i<num:
            num=i
    return num


print(maximum(array))
print(minimum(array))





