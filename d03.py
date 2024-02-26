'''
AoC 2023
Day 3: Gear Ratios
'''

import string
import os


SYMBOLS = [symbol for symbol in string.punctuation if symbol != '.']
NEIGHBORS = [-1, 0, 1]


def clear() -> None:
    """
    Clears console
    """
    os.system('cls')


def read_input(filename: str) -> list[str]:
    """
    Reads a file and returns its content as a list of strings.

    Args:
        filename (str): The name of the file to be read. The file should be
        located in the "./inputs/" directory.

    Returns:
        list[str]: A list of strings, each string corresponding to a line in
        the file.
    """
    with open("./inputs/" + filename, 'r', encoding='utf8') as file:
        matrix = [line.strip() for line in file.readlines()]
    return matrix


def part_1(filename: str) -> str:
    matrix: list[str] = read_input(filename)

    number_lst: list = []
    current_nb: str = ""
    neighbor: bool = False

    def reset_ongoing_variables():
        nonlocal current_nb, neighbor
        current_nb = ""
        neighbor = False

    def process_current_nb():
        if current_nb and neighbor:
            number_lst.append(int(current_nb))

    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell.isdigit():
                current_nb += cell
                for dy in NEIGHBORS:
                    for dx in NEIGHBORS:
                        ny, nx = y + dy, x + dx
                        if ((0 <= ny < len(matrix))
                                and (0 <= nx < len(row))
                                and (matrix[ny][nx] in SYMBOLS)):
                            neighbor = True
            else:
                process_current_nb()
                reset_ongoing_variables()

        # Check for a remaining number at the end of the line
        process_current_nb()
        reset_ongoing_variables()

    # Check for the last number in the matrix
    process_current_nb()

    return str(sum(number_lst))


def part_2(filename: str):
    matrix: list[str] = read_input(filename)

    number_lst: list = []
    current_nb: str = ""
    neighbor: bool = False

    def reset_ongoing_variables():
        nonlocal current_nb, neighbor
        current_nb = ""
        neighbor = False

    def process_current_nb():
        if current_nb and neighbor:
            number_lst.append(int(current_nb))

    for y, row in enumerate(matrix):
        for x, cell in enumerate(row):
            if cell.isdigit():
                current_nb += cell
                for dy in NEIGHBORS:
                    for dx in NEIGHBORS:
                        ny, nx = y + dy, x + dx
                        if ((0 <= ny < len(matrix))
                                and (0 <= nx < len(row))
                                and (matrix[ny][nx] == "*")):
                            neighbor = True
                            
            else:
                process_current_nb()
                reset_ongoing_variables()
        process_current_nb()
        reset_ongoing_variables()
    process_current_nb()

    # ! Still no clue :D


def main():
    clear()
    example = "_d03-1ex.txt"
    input_file = "day03.txt"
    print("Day 3: Gear Ratios")
    print("Part 1: " + part_1(input_file))
    part_2(example)


if __name__ == '__main__':
    main()
