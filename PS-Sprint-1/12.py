# 12. **Counting Vowels and Consonants in a String**  


vowels = 'aeiouAEIOU'
string = input("Enter a string: ")
vow=0
con=0
for i in string:
    if i in vowels:
        vow+=1
    else:
        con+=1
print(f"The string {string} contains {vow} number of vowels and {con} number of consonents")


