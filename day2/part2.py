from functools import reduce
file_path = "file.txt"

games = ""
with open(file_path, 'r') as file:
    games = file.read().strip().split("\n")

sum_of_power_sets = 0
for game in games:
    smalest_values = {"red": 1, "green": 1, "blue":1}

    game_title, game_data = game.split(':')
    bag_draws = game_data.split(";")

    for draw in bag_draws:
        draw = draw.split(",")
        for color_and_amount in draw:
            amount, color = color_and_amount.split()

            smalest_value_for_color = smalest_values.get(color)
            if int(amount) > smalest_value_for_color:
                smalest_values[color] = int(amount)

    sum_of_power_sets += reduce(lambda x, y: x * y, list(smalest_values.values()))

print("result: ", sum_of_power_sets)
