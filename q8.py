"""Module for string operations."""


def no_of_occurences_in_string(input_str):
    """
    Find occurrences of all the letters in a string. [Linear search]
    input: string = "elephant"
    output: "e2 l1 p1 h1 a1 n1 t1"
    """
    char_count = {}

    # Count occurrences of each character (skip spaces)
    for char in input_str:
        if char != ' ':
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    result = ""
    for char in input_str:
        if char in char_count:
            result += char + str(char_count[char]) + " "
            del char_count[char]

    return result.strip()


if __name__ == "__main__":
    no_of_occurences_in_string("elephant")
