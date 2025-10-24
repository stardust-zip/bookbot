from stats import get_book_text, count_words, count_characters


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    book_text_count = count_words(book_text)
    print(f"Found {book_text_count} total words")
    print(count_characters(book_text))


if __name__ == "__main__":
    main()
