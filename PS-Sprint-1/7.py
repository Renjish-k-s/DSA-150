row=10
# for i in range(1,row+1):
#     print((row-i)*" ",(2*i-1)*"1")
# for i in range(row-1,0,-1):
#     print((row-i)*" ",(2*i-1)*"1")

"""
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
"""

for i in range(row):
    for j in range(row):
        if i==0 or j==0 or j==row-1  or i==row//2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    