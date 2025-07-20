"""
Count word occurrences in given string
Goaltime: 20 min
Worktime: 19 min 44 sec
Code by: Miss Ghost/April First
"""


def main():
    """
    Get text and display word occurrences
    """
    text = input("Enter text: ")
    word_to_occurrences = {}
    for word in text.split():
        word_to_occurrences[word] = word_to_occurrences.get(word, 0) + 1
    # Sorted by number of occurrence (descending)
    # pairs = sorted(word_to_occurrences.items(), key=lambda x: x[1], reverse=True)

    # Sorted alphabetically
    pairs = sorted(word_to_occurrences.items(), key=lambda x: x[0], reverse=False)
    length = max(len(pair[0]) for pair in pairs)
    for pair in pairs:
        print(f"{pair[0]:{length}} : {pair[1]}")


if __name__ == '__main__':
    main()
