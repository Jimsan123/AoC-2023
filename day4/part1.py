file_path = "file.txt"

scratch_cards = []
with open(file_path, 'r') as file:
    scratch_cards = file.read().strip().split("\n")

total_points = 0

for card in scratch_cards:
    card_points = 0
    # print("card: ", card)

    card_title, values = card.split(":")
    winning_numbers, my_numbers = values.split("|")
    winning_numbers = winning_numbers.split()
    my_numbers = my_numbers.split()

    # print(f"card_title: {card_title}, values: {values}")
    # print(f"winning_numbers: {winning_numbers}, my_numbers: {my_numbers}")



    for number in my_numbers:
        if number in winning_numbers:
            if card_points == 0:
                card_points = 1
            else:
                card_points *= 2
    
    total_points += card_points

print(total_points)
