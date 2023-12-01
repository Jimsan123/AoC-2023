# Open the file
file_path = 'file.txt'  # Replace with your file path
# file_path = 'testfile.txt'  # Replace with your file path

def isDigit(input: int):
    for i in range(10):
        if i == input:
            return True
        
content = ""
with open(file_path, 'r') as file:
    # Read the contents
    content = file.read()

first_digits = ""
last_digits = ""

content = content.split()

for word in content:
    # print("word :?", word)

    # first digits
    for letter in word:
        try:
            if isDigit(int(letter)):
                first_digits += letter
                # print("ok")
                break
        except:
            # print("wrong")
            pass

print("test1: ")
for word in content:
    # last digits
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