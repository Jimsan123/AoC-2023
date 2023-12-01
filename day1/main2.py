# Open the file
# file_path = 'file.txt'  # Replace with your file path
file_path = 'testfile2.txt'  # Replace with your file path

def isDigit(input: int):
    for i in range(10):
        if i == input:
            return True
        
def containsDigitInStr(input: str):
    for strDigit in digitsInStr:
        if strDigit in input:
            return strDigit

digitsInStr = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
        
content = ""
with open(file_path, 'r') as file:
    # Read the contents
    content = file.read()

first_digits = ""
last_digits = ""

content = content.split()

# first digits
for word in content:
    print("first word :?", word)

    concat_letters: str = ""
    for letter in word:
        concat_letters += letter

        # check if digit
        try:
            if isDigit(int(letter)):
                first_digits += letter
                print("first ok")
                break
        except:
            print("first wrong")
            pass
        
        # check if digit in str


# last digits
for word in content:
    for letter_index in range(len(word)-1, -1, -1):
        
        try:
            if isDigit(int(word[letter_index])):
                last_digits += word[letter_index]
                print("ok")
                break
        except:
            print("wrong")


print("first digits: ", first_digits)
print("last digits: ", last_digits)

answer = 0
for i in range(len(first_digits)):
    answer += int(first_digits[i] + last_digits[i])
    
print("Solution: ", answer)