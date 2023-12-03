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


# Loop all rows in schematic
for row_num, row in enumerate(schematics):
    print(row_num, ": ", row)

    # Find the specific symbol
    symbol_indexes: list[int] = []
    for char_idx, character in enumerate(row):
        if character in string.punctuation and character != ".":
            symbol_indexes.append(char_idx)
        elif character in "0123456789":




    # Loop all rows close to found symbols
    for symbol_idx in symbol_indexes:

        # check previous row
        # Remember to check out of range
        if row_num != 0:
            prev_row = schematics[row_num-1]
            # checkAbove(schematics[row_num-1], symbol_idx)






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