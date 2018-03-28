def count_items(input_string):
    counts = {}
    for character in input_string:
        counts[character] = counts.get(character, 0) + 1
    return counts

def is_anagram(str_1, str_2):
    print(count_items(str_1.lower()))
    print(count_items(str_2.lower()))
    return count_items(str_1.lower()) == count_items(str_2.lower())

if(__name__ == '__main__'):
    print(is_anagram('sample', 'palmes'))
