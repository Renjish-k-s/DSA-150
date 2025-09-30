"""
Bubble sort
✅ Time Complexity (Optimized):

Best Case (already sorted): O(n)

Worst Case (completely reversed): O(n²)

Space: O(1)
array=[4,3,1,6,5,2]

for i in range(len(array)):
    swapped=False
    for j in range(1,len(array)):
        if array[j]<array[j-1]:
            array[j],array[j-1]=array[j-1],array[j]
            swapped=True
    if not swapped:
        break
print(array) """

"""
Selection sort

array=[4,3,1,6,5,2]
for i in range(len(array)):
    mind=i
    for j in range(i+1,len(array)):
        if array[mind]>array[j]:
            mind=j
    array[mind],array[i]=array[i],array[mind]
print(array)

"""

array=[4,3,1,6,5,2]

res=[]

for i in range(len(array)):
    mini=min(array)
    array.remove(mini)
    res.append(mini)

print(res)




    
