file_path = "testfile.txt"

scratch_cards = []
with open(file_path, 'r') as file:
    scratch_cards = file.read().strip().split("\n")

total_card_count = 0
card_left_to_look = 0


for card_idx, card in enumerate(scratch_cards):
    card_points = 0
    card_wins = 0
    # print("card: ", card)

    card_title, values = card.split(":")
    winning_numbers, my_numbers = values.split("|")
    winning_numbers = winning_numbers.split()
    my_numbers = my_numbers.split()

    # print(f"card_title: {card_title}, values: {values}")
    # print(f"winning_numbers: {winning_numbers}, my_numbers: {my_numbers}")

    # Find all the winning numbers
    for number in my_numbers:
        if number in winning_numbers: # Winning number
            card_wins += 1
            print(f"card_points: {card_points}")
    
    # Find all winning numbers from copies
    sum_from_copies = 0

    for card_copy_idx in range(card_idx, card_idx+card_wins):
        card_copy_points = 0
        card_wins = 0
        card_copy = card[card_copy_idx]

        card_copy_title, copy_values = card_copy.split(":")
        copy_winning_numbers, copy_my_numbers = values.split("|")
        copy_winning_numbers = copy_winning_numbers.split()
        copy_my_numbers = copy_my_numbers.split()

        for number in copy_my_numbers:
            if number in copy_winning_numbers:
                # todo: card_wins += 1
                print(f"card_copy_points: {card_copy_points}")
        sum_from_copies += card_copy_points


print(total_card_count)
