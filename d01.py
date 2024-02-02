'''
AoC 2023
Day 1: Trebuchet?!
'''
import regex as re


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


def extract_numbers(text: str) -> str:
    """
    This function extracts numbers from a given text. The numbers can be in
    both digit and word forms. For example, 'one' will be converted to '1',
    'two' to '2', and so on up to 'nine' to '9'. The function returns a string
    of the extracted numbers.

    Args:
        text (str): The input text from which numbers are to be extracted.

    Returns:
        str: A string of the extracted numbers. If a number is represented as
        a word in the text, it is converted to its digit form
    """
    number_map = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    pattern = "|".join(number_map.keys()) + "|" + "|".join(number_map.values())
    words_and_numbers = re.findall(pattern, text, overlapped=True)
    extracted_string = ""
    for number_string in words_and_numbers:
        if number_string.isnumeric():
            extracted_string += number_string
        else:
            number_string = number_string.replace(number_string,
                                                  number_map[number_string])
            extracted_string += number_string

    return extracted_string


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
    calibration_list_1 = read_input(filename)
    calibration_values_1 = []
    for line in calibration_list_1:
        _chache_1 = ""
        for char in line:
            if char.isnumeric():
                _chache_1 += char
        calibration_values_1.append(int(_chache_1[0] + _chache_1[-1]))
    return str(sum(calibration_values_1))


def get_calibration_value_2(filename: str) -> str:
    """
    This function reads a file, extracts numbers from each line, and
    calculates a calibration value. The calibration value is calculated as the
    sum of the first and last digit of the extracted numbers from each line.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        str: The calculated calibration value as a string.
    """
    calibration_list_2 = read_input(filename)
    calibration_value_2 = []
    for line in calibration_list_2:
        _cache_2 = extract_numbers(line)
        calibration_value_2.append(int(_cache_2[0] + _cache_2[-1]))
    return str(sum(calibration_value_2))


def main():
    input_file = 'day01.txt'
    print("Day 1: Trebuchet?!")
    print("Part 1: " + get_calibration_value_1(input_file))
    print("Part 2: " + get_calibration_value_2(input_file))


if __name__ == '__main__':
    main()
