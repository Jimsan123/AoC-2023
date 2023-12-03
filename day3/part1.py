import string
file_path = "testfile.txt"

schematics = ""
with open(file_path, 'r') as file:
    schematics = file.readlines()

# print(len(schematics))
# def checkAbove(row_above: str, curr_idx):
#     found_numbers = []
#     if curr_idx == 0:
#         if row_above[curr_idx] in "0123456789":
#             searchWholeNumber()

#     elif curr_idx == len(schematics):

#     else:

# def searchWholeNumber():
#     pass


# Find all symbols in the schematic
symbol_indexes: list[(int, int)] = []
for row_num, row in enumerate(schematics):
    print(row_num, ": ", row)

    # Find the specific symbols
    for char_idx, character in enumerate(row):
        if character in string.punctuation and character != ".":
            symbol_indexes.append((row_num, char_idx))


print("all found symbols: \n", symbol_indexes)

# Find all numbers
numbers: list[(int, int, str)] = []
for row_num, row in enumerate(schematics):
    current_number: str = ""
    for char_idx, character in enumerate(row):
        
        if character in "0123456789":
            current_number += character
        elif current_number != "":
            numbers.append((row_num, char_idx-1, current_number))
            current_number = ""

print("All found numbers \n", numbers)

# Find all numbers that are close to symbols

for row_num, last_char_idx, value in numbers:

    first_char_idx: int = last_char_idx - len(value) - 1
    # check above
    if row_num != 0:
        if first_char_idx == 0:
            for symbol_coordinate in symbol_indexes:
                print(symbol_coordinate)
                print("row_num-1: ", row_num-1)
                print("first_char_idx-1: ", first_char_idx-1)
                if symbol_coordinate[0] == row_num-1 and \
                    symbol_coordinate[1] == first_char_idx-1:
                    print("Found a symbol above???")
                    print("symbol: ", symbol_coordinate, \
                          "row_num, last_char_idx, value: ", row_num, last_char_idx, value)




"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""