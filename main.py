import sys
from stats import (
    count_characters,
    count_words,
    get_book_text,
    sorted_dict,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    words_count = count_words(book_text)
    char_dict = count_characters(book_text)
    dict_list = sorted_dict(char_dict)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for d in dict_list:
        if d["char"].isalpha():
            print(f"{d['char']}: {d['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()
