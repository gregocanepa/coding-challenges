from typing import List


def solution(S: str, grid: List[str]):
    # check edge case
    grid_as_string = "".join(grid)
    print(grid_as_string.strip("."))
    dict_of_letters = dict()
    for letter in S:
        letter_counter = 0
        if letter in dict_of_letters:
            letter_counter += 1
            dict_of_letters[f"{letter}_{letter_counter}"] = {"row": 0, "cell": 0}
        else:
            dict_of_letters[letter] = {"row": 0, "cell": 0}
    row_number = 0
    for row in grid:
        cell_number = 0
        for cell in row:
            if cell in S:
                dict_of_letters[cell]["row"] = row_number
                dict_of_letters[cell]["cell"] = cell_number
                continue
            cell_number += 1
        row_number += 1
    print(dict_of_letters)
    return 1
