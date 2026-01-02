import sys

from stats import (
    get_letters_appearance,
    get_num_words,
    sort_dictionaries,
)


def get_book_text(path):
    with open(path) as file:
        file_contents = file.read()
    return file_contents


def main():
    if len(sys.argv) == 2:
        path_to_file = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path_to_file}...")
        print("----------- Word Count ----------")
        num_words = get_num_words(get_book_text(path_to_file))
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        # get_letters_appearance(get_book_text(path_to_file))
        letter_counts = get_letters_appearance(get_book_text(path_to_file))
        for char in sort_dictionaries(letter_counts):
            if not char["char"].isalpha():
                continue
            else:
                print(f"{char['char']}: {char['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
