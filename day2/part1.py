file_path = "file.txt"

games = ""
with open(file_path, 'r') as file:
    games = file.read().strip().split("\n")

max_color_amount = {"red": 12, "green": 13, "blue":14}

possible_game_ids = 0
for game in games:
    game_ok = True

    game_title, game_data = game.split(':')
    bag_draws = game_data.split(";")

    for draw in bag_draws:
        draw = draw.split(",")
        for color_and_amount in draw:
            amount, color = color_and_amount.split()

            max_value_for_color = max_color_amount.get(color)
            if int(amount) > max_value_for_color:
                game_ok = False

    if game_ok:
        possible_game_ids += int(game_title.split("Game ")[1])

print("result: ", possible_game_ids)
