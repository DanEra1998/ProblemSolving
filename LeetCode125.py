def getCharacterizedString(s):
    converted_str = ""
    for letter in s:
        ascii_value = ord(letter)

        if (ascii_value >= 65 and ascii_value <= 90) or (ascii_value >= 97 and ascii_value <=122):
            converted_str += letter  # Accumulating the letters in converted_str
    return converted_str  # Return the accumulated string

def isPalindrome(s:str) -> bool:
    new_str = getCharacterizedString(s)
    left = 0
    right = len(new_str) - 1
    while left < right:
        if new_str[left] != new_str[right]:
            return False
        left+=1
        right-=1
    return True

s = "lDADFol"
print(getCharacterizedString(s))
print(isPalindrome(s))


