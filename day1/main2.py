file_path = 'file.txt'  # Replace with your file path
# file_path = 'testfile2.txt'  # Replace with your file path

def isDigit(input: int):
    for i in range(10):
        if i == input:
            return True

def containsDigitInStr(input: str) -> int | None:
    for i, strDigit in enumerate(digitsInStr):
        found_str_idx: int = input.find(strDigit)
        if found_str_idx != -1:
            return digit1to9[i]

digitsInStr = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
digit1to9 = [1,2,3,4,5,6,7,8,9]


content = ""
with open(file_path, 'r') as file:
    content = file.read()

first_digits = ""
last_digits = ""

content = content.split()

# first digits
for word in content:
    concat_letters: str = ""

    for letter in word:
        concat_letters += letter

        # check if str digit
        str_digit: int | None = containsDigitInStr(concat_letters)
        if str_digit != None and str_digit != -1:
            first_digits += str(str_digit)
            break

        # check if digit
        try:
            if isDigit(int(letter)):
                first_digits += letter
                break
        except:
            pass

# last digits
for word in content:
    concat_letters: str = ""
    for letter_index in range(len(word)-1, -1, -1):
        concat_letters = word[letter_index] + concat_letters

        # check if str digit
        str_digit: int | None = containsDigitInStr(concat_letters)
        if str_digit != None and str_digit != -1:
            last_digits += str(str_digit)
            break

        try:
            if isDigit(int(word[letter_index])):
                last_digits += word[letter_index]
                break
        except:
            pass

print("first digits: ", first_digits)
print("last digits: ", last_digits)

answer = 0
for i in range(len(first_digits)):
    answer += int(first_digits[i] + last_digits[i])

print("Solution: ", answer)
