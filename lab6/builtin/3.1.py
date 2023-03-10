string1 = str(input())
string2 = "".join(reversed(string1))
if (string1 == string2):
    print("YES")
else:
    print("NO")    
