'''
AoC 2023
Day 2: Cube Conundrum
'''


MAX_RED = 12
MAX_GREEM = 13
MAX_BLUE = 14


def parse_input(filename: str) -> list[str]:
    """
    Parse the input file and return its content as a list of strings.

    Args:
        filename (str): The name of the input file to be parsed.

    Returns:
        list[str]: A list of strings representing the lines of the input file.
    """
    with open('./inputs/' + filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def get_color_values(filename: str) -> dict:
    """
    Parse the input file to extract color information for each game.

    Args:
        filename (str): he name of the input file containing game and draw
        information.


    Returns:
        dict:  dictionary where keys are game IDs (int) and values are
                dictionaries representing the maximum counts of each color
                ('red', 'green', 'blue') in that game.
    """
    lines = parse_input(filename)
    game_dict = {}
    for line in lines:
        game_id, draws = line.split(':')
        game_id = int(game_id[5:])
        draws = draws.strip().split(';')
        max_colors = {'red': 0, 'green': 0, 'blue': 0}
        for draw in draws:
            colors = draw.strip().split(',')
            for color in colors:
                count, color_name = color.strip().split(' ')
                count = int(count)
                if count > max_colors[color_name]:
                    max_colors[color_name] = count
        game_dict[game_id] = max_colors
    return game_dict


def multiply_all(factors: tuple[int]) -> int:
    """
    Multiply all elements in a tuple.
    This function takes a tuple of numbers as input and returns the product of
    all the numbers in the tuple.

    Args:
        factors (tuple): A tuple of integers to be multiplied.

    Returns:
        int: The product of all integers in the input tuple.
    """
    result = 1
    for factor in factors:
        result *= factor
    return result


def get_possible_id_sum(filename: str) -> str:
    """
    Calculate the sum of game IDs where color constraints are satisfied.

    Args:
        filename (str): The name of the input file containing game and draw
        information.

    Returns:
        str: The sum of game IDs where the count of each color ('red',
        'green', 'blue') is within the specified limits.
    """

    games = get_color_values(filename)
    solutions = [(game['red'] <= MAX_RED,
                  game['green'] <= MAX_GREEM,
                  game['blue'] <= MAX_BLUE)
                 for game in games.values()]
    solution_lst = []
    for i, outcome in enumerate(solutions):
        i += 1
        if all(outcome) is True:
            solution_lst.append(int(i))

    return str((sum(solution_lst)))


def get_possible_power(filename: str) -> str:
    """
    Calculate the total possible power from the color values of games.

    This function reads the color values of games from a file, multiplies the
    color values of each game, and sums up these products to get the total
    possible power.

    Args:
        filename (str): The name of the file containing the color values of
        games.

    Returns:
        str: The total possible power as a string.
    """
    games = get_color_values(filename)
    solutions = [(game['red'],
                  game['green'],
                  game['blue'])
                 for game in games.values()]
    power_lst = []
    for game_values in solutions:
        value = multiply_all(game_values)
        power_lst.append(value)
    return str(sum(power_lst))


def main():
    input_file = "day02.txt"
    print("Day 2: Cube Conundrum")
    print("Part 1: " + get_possible_id_sum(input_file))
    print("Part 2: " + get_possible_power(input_file))


if __name__ == '__main__':
    main()
