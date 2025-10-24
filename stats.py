def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def count_words(book_text):
    return len(book_text.split())


def count_characters(book_text):
    char_dict = {}

    for character in book_text.lower():
        if character not in char_dict:
            char_dict[character] = 1
        else:
            char_dict[character] += 1

    return char_dict
