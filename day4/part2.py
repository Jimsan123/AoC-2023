file_path = "testfile.txt"

scratch_cards = []
with open(file_path, 'r') as file:
    scratch_cards = list(file.read().strip().split("\n"))

total_card_count = 0

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
            print(f"card_wins: {card_wins}")

    # Find all winning numbers from copies
    sum_from_copies = 0

    for card_copy_idx in range(card_idx+1, card_idx+card_wins+1):
        card_copy_wins = 0
        card_copy = scratch_cards[card_copy_idx]

        print(f"card_copy: {card_copy}")

        card_copy_title, copy_values = card_copy.split(":")
        copy_winning_numbers, copy_my_numbers = values.split("|")
        copy_winning_numbers = copy_winning_numbers.split()
        copy_my_numbers = copy_my_numbers.split()

        for number in copy_my_numbers:
            if number in copy_winning_numbers:
                card_copy_wins += 1
        sum_from_copies += card_copy_wins

    total_card_count += sum_from_copies


print(total_card_count)
