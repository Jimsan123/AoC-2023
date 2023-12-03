file_path = "file.txt"

schematics = ""
with open(file_path, 'r') as file:
    schematics = file.readlines()

# Find all symbols in the schematic
symbol_indexes: list[(int, int)] = []
for row_num, row in enumerate(schematics):
    # Find the specific symbols
    for char_idx, character in enumerate(row):
        if character in "#-*=+@&%$/" and character != ".":
            symbol_indexes.append((row_num, char_idx))

# print("all found symbols: \n", symbol_indexes)

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

# print("All found numbers \n", numbers)

# Find all numbers that are close to symbols
approved_numbers: list[int] = []

for row_num, last_char_idx, value in numbers:

    first_char_idx: int = int(last_char_idx - len(value) + 1)
    first_search: int = first_char_idx - 1
    last_search: int =  last_char_idx + 1

    # above
    for coordinate in symbol_indexes:
        if coordinate[0] == row_num-1:
            if coordinate[1] >= first_search \
            and coordinate[1] <= last_search:
                approved_numbers.append(int(value))
                # print(f"value {value} approved for above")

    # same row
    for coordinate in symbol_indexes:
        if coordinate[0] == row_num:
            if coordinate[1] == first_search or coordinate[1] == last_search:
                approved_numbers.append(int(value))
                # print(f"value {value} approved for same row")

    # bellow
    for coordinate in symbol_indexes:
        if coordinate[0] == row_num+1:
            if coordinate[1] >= first_search \
            and coordinate[1] <= last_search:
                approved_numbers.append(int(value))
                # print(f"value {value} approved for bellow")

print(sum(approved_numbers))

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