'''
AoC 2023
Day 1: Trebuchet?!
'''


def read_input(filename: str) -> list[str]:
    """
    Reads the contents of a text file and returns a list of strings, where each
    string represents a line from the file.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        list[str]: A list containing the lines of text from the file. Each
        element of the list corresponds to a line in the file, and trailing
        whitespaces are removed.
    """
    with open("./inputs/" + filename, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def get_calibration_value_1(filename: str) -> str:
    """
    Read calibration data from the specified file, extract numeric values from
    each line, calculate the sum of the extracted values, and return the result
    as a string.

    Args:
        filename (str): The name of the file containing calibration data.

    Returns:
        str: The sum of the extracted calibration values as a string.
    """
    calibration_list = read_input(filename)
    calibration_values = []
    for line in calibration_list:
        _chache = ""
        for char in line:
            if char.isnumeric():
                _chache += char
        calibration_values.append(int(_chache[0] + _chache[-1]))
    return str(sum(calibration_values))


# def get_calibration_value_2(filename: str) -> str:
#     calibration_list = read_input(filename)


def main():
    # example_1 = "_d1-1ex.txt"
    # example_2 = "_d1-2ex.txt"
    input_file = 'day01.txt'
    print("Day 1: Trebuchet?!")
    print("Part 1: " + get_calibration_value_1(input_file))

    # TODO: PART 2: Find a way to find the number words in the strings in
    # TODO: order, even if the number words share a letter: e.g. xtwone3four
    # print("Part 2: " + get_calibration_value_2(example_2))


if __name__ == '__main__':
    main()
