def palindrome(text):
    length = len(text)
    for i in range(0, length // 2):
        if (text[i] != text[length - i -1]):
            return False
        return True
string = str(input())
print(palindrome(string))    