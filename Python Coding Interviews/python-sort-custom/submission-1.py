from typing import List

def sort_by_length(word: str) -> int:
    return len(word)

def sort_by_absolute_value(num: int) -> int:
    return abs(num)

def sort_words(words: List[str]) -> List[str]:
    words.sort(key=sort_by_length, reverse = True)
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    numbers.sort(key=sort_by_absolute_value)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
