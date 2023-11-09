#Task 1.1
import string

upMap = string.ascii_uppercase
lowMap = string.ascii_lowercase
#print(upMap, lowMap)

def ROTchar(char):
    if char in upMap:
        index = upMap.index(char)
        return ord(upMap[(index+13)%26])
    if char in lowMap:
        index = lowMap.index(char)
        return ord(lowMap[(index+13)%26])
    else:
        return ord(char)

print(ROTchar("A"))
print(ROTchar("a"))
print(ROTchar("3"))
print(ROTchar("#"))

#Task 1.2
userChar = input("Enter a single character") #assume user only inputs single characters
print(ROTchar(userChar))

#Task 1.3
userText = input("Enter a text message")
output = ''
for c in userText:
    output += chr(ROTchar(c))
print(output)
