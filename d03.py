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
    """
    Calculates the sum of all part numbers in an engine schematic.

    The engine schematic is read from a file. Each line in the file represents
    a row in the schematic. A part number is defined as a number that is
    adjacent to a symbol (any character that is not a number or a period).
    Adjacency is considered in all eight directions (up, down, left, right,
    and the four diagonals).

    Args:
        filename (str): The name of the file containing the engine schematic.

    Returns:
        str: The sum of all part numbers in the engine schematic, represented
        as a string.
    """
    matrix: list[str] = read_input(filename)

    number_lst = list()
    current_nb = str()
    has_neighbor: bool = False

    for y, row in enumerate(matrix):
        for x, _ in enumerate(row):
            if matrix[y][x].isnumeric():
                current_nb += matrix[y][x]
                for dy in NEIGHBORS:
                    for dx in NEIGHBORS:
                        ny, nx = y + dy, x + dx
                        if ((0 <= ny < len(matrix))
                                and (0 <= nx < len(row))
                                and (matrix[ny][nx] in SYMBOLS)):
                            has_neighbor = True
            else:
                if current_nb != "" and has_neighbor is True:
                    number_lst.append(int(current_nb))
                current_nb = ""
                has_neighbor = False

        # Check for a remaining number at the end of the line
        if current_nb != "" and has_neighbor is True:
            number_lst.append(int(current_nb))
        current_nb = ""
        has_neighbor = False

    # Check for the last number in the matrix
    if current_nb != "" and has_neighbor is True:
        number_lst.append(int(current_nb))

    return str(sum(number_lst))


def part_2():
    # TODO: Yet no clue how to do this
    pass


def main():
    clear()
    # example = "_d03-1ex.txt"
    input_file = "day03.txt"
    print("Day 3: Gear Ratios")
    print("Part 1: " + part_1(input_file))


if __name__ == '__main__':
    main()
